#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_vertical_slice.py — 縦スライス(M02→M03A→M04→Map復帰)の完了条件チェック
                          （python3 のみ・依存なし）

対象仕様: docs/spec/VERTICAL_SLICE_M02_M03_M04_SPEC.md
使い方:
    python3 tools/check_vertical_slice.py [docs/rewrite-dev/index.html] [--scene slice_ch01_walk]

判定(C1〜C10):
    C1  SCENES が JSON 解析でき、シーン数>0
    C2  参照整合（scene/next/skip/sceneIfFlag.scene/objects[].scene が既存id・id重複なし）
    C3  スライス walk シーン(既定 id: slice_ch01_walk)が type:"walk" で存在、startX/worldWidth/objects(>=3)
    C4  同 objects に talk(配列・各要素 text あり)を持つ要素が >=1   … M03A 導線
    C5  同 objects に vn(配列・各要素 text あり)を持つ要素が >=1     … M04 導線
    C6  HTML に id: walk-vn / walk-vn-portrait / walk-vn-name / walk-vn-text / walk-vn-white
    C7  HTML に VNO.start / VNO.end の定義
    C8  WK.doAction 内で t.vn を参照し VNO.start( を呼ぶ
    C9  M04 経路で WK.resume( を呼ぶ（Map 復帰）
    C10 既存 walk シーン ch01_walk_plaza が存在（非破壊）

全項目合格で PASS(exit 0)。1件でも不合格で FAIL(exit 1)。
"""
import sys
import re
import json

SLICE_ID_DEFAULT = "slice_ch01_walk"
BASELINE_WALK_ID = "ch01_walk_plaza"
REQUIRED_DOM_IDS = ["walk-vn", "walk-vn-portrait", "walk-vn-name", "walk-vn-text", "walk-vn-white"]


# ── SCENES 抽出（check_scenes.py と同じ堅牢な括弧マッチ）──────────────
def _match_array(html, start):
    depth = 0
    in_str = False
    esc = False
    for i in range(start, len(html)):
        c = html[i]
        if in_str:
            if esc:
                esc = False
            elif c == '\\':
                esc = True
            elif c == '"':
                in_str = False
            continue
        if c == '"':
            in_str = True
        elif c == '[':
            depth += 1
        elif c == ']':
            depth -= 1
            if depth == 0:
                return html[start:i + 1]
    return None


def extract_scenes_literal(html):
    best = None
    best_n = -1
    for m in re.finditer(r'SCENES\s*=\s*\[', html):
        start = html.index('[', m.start())
        lit = _match_array(html, start)
        if not lit:
            continue
        try:
            n = len(json.loads(lit))
        except json.JSONDecodeError:
            n = -1
        if n > best_n:
            best_n, best = n, lit
    return best


def scene_links(s):
    out = []
    sid = s.get('id', '?')
    for o in s.get('objects', []) or []:
        if o.get('scene'):
            out.append((sid + '/obj[' + str(o.get('name') or o.get('icon') or '?') + ']', o['scene']))
        sif = o.get('sceneIfFlag')
        if isinstance(sif, dict) and sif.get('scene'):
            out.append((sid + '/obj/ifFlag', sif['scene']))
    for h in s.get('hotspots', []) or []:
        if h.get('next'):
            out.append((sid + '/hs', h['next']))
    for o in s.get('options', []) or []:
        if o.get('next'):
            out.append((sid + '/opt', o['next']))
    if s.get('next'):
        out.append((sid + '/next', s['next']))
    if s.get('skip'):
        out.append((sid + '/skip', s['skip']))
    return out


def _has_text_array(v):
    """v が配列で、全要素が dict かつ text を持つなら True。"""
    if not isinstance(v, list) or not v:
        return False
    return all(isinstance(x, dict) and str(x.get('text', '')).strip() for x in v)


def main():
    args = [a for a in sys.argv[1:]]
    path = 'docs/rewrite-dev/index.html'
    slice_id = SLICE_ID_DEFAULT
    i = 0
    positional = []
    while i < len(args):
        if args[i] == '--scene' and i + 1 < len(args):
            slice_id = args[i + 1]
            i += 2
            continue
        positional.append(args[i])
        i += 1
    if positional:
        path = positional[0]

    try:
        html = open(path, encoding='utf-8').read()
    except OSError as e:
        print('❌ ファイルを開けません:', e)
        return 2

    results = []  # (code, ok, detail)

    def add(code, ok, detail):
        results.append((code, ok, detail))

    # ── C1: SCENES 解析 ──
    lit = extract_scenes_literal(html)
    scenes = None
    if lit is None:
        add('C1', False, 'SCENES 配列が見つからない')
    else:
        try:
            scenes = json.loads(lit)
            add('C1', len(scenes) > 0, 'シーン数 %d' % len(scenes))
        except json.JSONDecodeError as e:
            add('C1', False, 'JSON 解析失敗: %s' % e)

    idset = set()
    slice_scene = None
    if scenes is not None:
        ids = [s.get('id') for s in scenes]
        idset = set(ids)
        dups = sorted({x for x in ids if ids.count(x) > 1})
        missing = []
        for s in scenes:
            for label, target in scene_links(s):
                if target not in idset:
                    missing.append((label, target))
        c2_ok = (not dups) and (not missing)
        det = 'id重複 %d件 / 参照切れ %d件' % (len(dups), len(missing))
        if missing:
            det += ' — ' + ', '.join('%s→%s' % (l, t) for l, t in missing[:5])
        add('C2', c2_ok, det)

        slice_scene = next((s for s in scenes if s.get('id') == slice_id), None)
        # ── C3 ──
        if slice_scene is None:
            add('C3', False, 'walk シーン id=%s が無い' % slice_id)
        else:
            objs = slice_scene.get('objects') or []
            ok = (
                slice_scene.get('type') == 'walk'
                and isinstance(slice_scene.get('startX'), (int, float))
                and isinstance(slice_scene.get('worldWidth'), (int, float))
                and isinstance(objs, list) and len(objs) >= 3
            )
            add('C3', ok, 'type=%s startX=%s worldWidth=%s objects=%d'
                % (slice_scene.get('type'), slice_scene.get('startX'),
                   slice_scene.get('worldWidth'), len(objs)))

        # ── C4 / C5 ──
        if slice_scene is None:
            add('C4', False, 'スライス未存在のため判定不可')
            add('C5', False, 'スライス未存在のため判定不可')
        else:
            objs = slice_scene.get('objects') or []
            talk_objs = [o for o in objs if _has_text_array(o.get('talk'))]
            vn_objs = [o for o in objs if _has_text_array(o.get('vn'))]
            add('C4', len(talk_objs) >= 1, 'talk 導線 %d件' % len(talk_objs))
            add('C5', len(vn_objs) >= 1, 'vn 導線 %d件' % len(vn_objs))

        # ── C10 ──
        add('C10', BASELINE_WALK_ID in idset,
            '既存 %s %s' % (BASELINE_WALK_ID, '存在' if BASELINE_WALK_ID in idset else '欠落'))
    else:
        for c in ('C2', 'C3', 'C4', 'C5', 'C10'):
            add(c, False, 'SCENES 未解析のため判定不可')

    # ── C6: DOM id（HTML 生文字列で確認）──
    missing_ids = [i for i in REQUIRED_DOM_IDS
                   if not re.search(r'id\s*=\s*["\']%s["\']' % re.escape(i), html)]
    add('C6', not missing_ids,
        '全DOM id 存在' if not missing_ids else '欠落: ' + ', '.join(missing_ids))

    # ── C7: VNO エンジン ──
    has_start = re.search(r'VNO\.start\s*=', html) is not None
    has_end = re.search(r'VNO\.end\s*=', html) is not None
    add('C7', has_start and has_end,
        'VNO.start=%s VNO.end=%s' % (has_start, has_end))

    # ── C8: doAction 結線（t.vn 参照 + VNO.start( 呼び出し）──
    m = re.search(r'WK\.doAction\s*=\s*function', html)
    c8_ok = False
    c8_det = 'WK.doAction が見つからない'
    if m:
        body = html[m.end(): m.end() + 2000]  # doAction 本体近傍
        refs_vn = re.search(r'\bt\.vn\b', body) is not None
        calls = re.search(r'VNO\.start\s*\(', body) is not None
        c8_ok = refs_vn and calls
        c8_det = 't.vn参照=%s VNO.start()呼出=%s' % (refs_vn, calls)
    add('C8', c8_ok, c8_det)

    # ── C9: Map 復帰（VNO 経路で WK.resume( ）──
    #   VNO.start に渡す onDone 内、または doAction の vn 分岐内に WK.resume( があること。
    c9_ok = False
    c9_det = 'WK.resume( が M04 経路に見当たらない'
    if m:
        body = html[m.end(): m.end() + 2000]
        vn_idx = body.find('t.vn')
        if vn_idx >= 0 and re.search(r'WK\.resume\s*\(', body[vn_idx: vn_idx + 800]):
            c9_ok = True
            c9_det = 'doAction の vn 分岐内に WK.resume( あり'
    add('C9', c9_ok, c9_det)

    # ── 出力 ──
    order = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10']
    labels = {
        'C1': 'SCENES 解析可能',
        'C2': '参照整合（切れ/重複なし）',
        'C3': 'スライス walk シーン存在(%s)' % slice_id,
        'C4': 'M03A 導線(talk>=1)',
        'C5': 'M04 導線(vn>=1)',
        'C6': 'M04 DOM id 一式',
        'C7': 'M04 エンジン VNO.start/end',
        'C8': 'doAction が vn→VNO.start 結線',
        'C9': 'M04 経路で Map 復帰(WK.resume)',
        'C10': '非破壊(既存 %s 保持)' % BASELINE_WALK_ID,
    }
    rmap = {c: (ok, det) for c, ok, det in results}
    print('対象ファイル :', path)
    print('スライス id  :', slice_id)
    print('─' * 60)
    all_ok = True
    for c in order:
        ok, det = rmap.get(c, (False, '未評価'))
        all_ok = all_ok and ok
        print('%s %-3s %-30s : %s' % ('✅' if ok else '❌', c, labels[c], det))
    print('─' * 60)
    print('判定         :', 'PASS ✅ 全条件クリア' if all_ok else 'FAIL ❌ 未達あり')
    return 0 if all_ok else 1


if __name__ == '__main__':
    sys.exit(main())
