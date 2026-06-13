#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_scenes.py — rewrite-dev / index.html のシーン整合性チェック（python3のみ・依存なし）

使い方:
    python3 tools/check_scenes.py docs/rewrite-dev/index.html

判定:
    SCENES 内の全参照（objects[].scene / hotspots[].next / options[].next /
    next / skip / sceneIfFlag.scene）が既存 id に解決できれば PASS。
    1件でも未解決、id重複、またはシーン0件なら FAIL（exit code 1）。
"""
import sys
import re
import json


def _match_array(html, start):
    """html[start] が '[' の位置。文字列・エスケープを考慮した括弧マッチで
    対応する ']' までの配列リテラルを返す。"""
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
    """`SCENES = [ ... ]` の配列リテラルを取り出す。
    `var SCENES = [];` のような空宣言と実データ代入が両方ある場合に備え、
    全候補を解析して最も要素数の多いものを採用する。"""
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
    """1シーンから (ラベル, 参照先id) のリストを返す。"""
    out = []
    sid = s.get('id', '?')
    for o in s.get('objects', []) or []:
        if o.get('scene'):
            out.append((sid + '/obj[' + str(o.get('name') or o.get('icon') or '?') + ']', o['scene']))
        sif = o.get('sceneIfFlag')
        if isinstance(sif, dict) and sif.get('scene'):
            out.append((sid + '/obj[' + str(o.get('name') or '?') + ']/ifFlag', sif['scene']))
    for h in s.get('hotspots', []) or []:
        if h.get('next'):
            out.append((sid + '/hs[' + str(h.get('label', '?')) + ']', h['next']))
    for o in s.get('options', []) or []:
        if o.get('next'):
            out.append((sid + '/opt', o['next']))
    if s.get('next'):
        out.append((sid + '/next', s['next']))
    if s.get('skip'):
        out.append((sid + '/skip', s['skip']))
    return out


def main():
    if len(sys.argv) < 2:
        print('使い方: python3 tools/check_scenes.py <index.html>')
        return 2
    path = sys.argv[1]
    try:
        html = open(path, encoding='utf-8').read()
    except OSError as e:
        print('❌ ファイルを開けません:', e)
        return 2

    lit = extract_scenes_literal(html)
    if lit is None:
        print('❌ SCENES 配列が見つかりません')
        return 1
    try:
        scenes = json.loads(lit)
    except json.JSONDecodeError as e:
        print('❌ SCENES の JSON 解析に失敗:', e)
        return 1

    ids = [s.get('id') for s in scenes]
    idset = set(ids)
    dups = sorted({i for i in ids if ids.count(i) > 1})

    missing = []
    for s in scenes:
        for label, target in scene_links(s):
            if target not in idset:
                missing.append((label, target))

    print('対象ファイル :', path)
    print('総シーン数   :', len(scenes))
    print('id 重複      :', 'なし' if not dups else ('%d件 ' % len(dups)) + ', '.join(dups))
    print('参照切れ     :', '%d件' % len(missing))
    for label, target in missing:
        print('   ❌', label, '→', target, '(未定義)')

    empty = (len(scenes) == 0)
    if empty:
        print('   ❌ シーンが0件です（SCENESデータを取得できていない可能性）')
    ok = (not missing) and (not dups) and (not empty)
    print('判定         :', 'PASS ✅ 参照切れ0件' if ok else 'FAIL ❌')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
