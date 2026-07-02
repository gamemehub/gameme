extends Node2D
# RewriteMemory 1部屋プロトタイプ（Phase1 / Go-No-Go）
# 白い広場を歩き、ミオと話し、小包で記憶断片(Lv3)、5席目の跡でログ逆流、時計塔入口でエリア遷移。
# 仕様: docs/project/PROTOTYPE_GODOT_1ROOM.md
# シーンはコードで構築（.tscnの壊れやすさを避けるため）。操作: 矢印/WASD 移動、Space/Enter 調べる・送る。

const SPEED := 220.0
const WORLD := Vector2(2600, 1500)      # 部屋の広さ(px)
const WALL := 40.0                       # 外周の壁厚

var player: CharacterBody2D
var player_spr: Sprite2D
var _walk_t := 0.0
var cam: Camera2D
var ui_root: Control
var hud: Label
var prompt: Label
var panel: Panel
var name_lbl: Label
var text_lbl: Label
var face: TextureRect
var overlay: ColorRect
var bust: TextureRect
var choices: VBoxContainer
var title_card: Label

var interactables: Array = []            # {pos:Vector2, radius:float, cb:Callable, prompt:String, id:String}
var state := "explore"                    # explore / dialogue / choice / busy
var dq: Array = []                         # dialogue queue
var dq_end: Callable
var near = null
var flags := {}

func _ready() -> void:
	_setup_input()
	_build_world()
	_build_player()
	_build_ui()
	_place_objects()

# 矢印＋WASD を移動アクションに登録（project.godotの入力定義を書かず、コードで確実に）
func _setup_input() -> void:
	var binds := {
		"move_left": [KEY_LEFT, KEY_A],
		"move_right": [KEY_RIGHT, KEY_D],
		"move_up": [KEY_UP, KEY_W],
		"move_down": [KEY_DOWN, KEY_S],
	}
	for action in binds.keys():
		if not InputMap.has_action(action):
			InputMap.add_action(action)
		for kc in binds[action]:
			var ev := InputEventKey.new()
			ev.physical_keycode = kc
			InputMap.action_add_event(action, ev)

# ---------- 構築 ----------
func _build_world() -> void:
	# 床（仮・単色）
	var floor := ColorRect.new()
	floor.color = Color(0.83, 0.84, 0.90)   # 白い広場: くすんだ白青
	floor.size = WORLD
	floor.position = Vector2.ZERO
	floor.z_index = -10
	add_child(floor)
	# 外周の壁（当たり判定）
	_add_wall(Vector2(WORLD.x/2, -WALL/2), Vector2(WORLD.x, WALL))          # 上
	_add_wall(Vector2(WORLD.x/2, WORLD.y+WALL/2), Vector2(WORLD.x, WALL))   # 下
	_add_wall(Vector2(-WALL/2, WORLD.y/2), Vector2(WALL, WORLD.y))          # 左
	_add_wall(Vector2(WORLD.x+WALL/2, WORLD.y/2), Vector2(WALL, WORLD.y))   # 右
	# 噴水（中央の障害物）
	var fount := ColorRect.new()
	fount.color = Color(0.62, 0.66, 0.78)
	fount.size = Vector2(260, 200)
	fount.position = Vector2(1200 - 130, 750 - 100)
	add_child(fount)
	_add_wall(Vector2(1200, 750), Vector2(260, 200))

func _add_wall(center: Vector2, size: Vector2) -> void:
	var body := StaticBody2D.new()
	body.position = center
	var col := CollisionShape2D.new()
	var shape := RectangleShape2D.new()
	shape.size = size
	col.shape = shape
	body.add_child(col)
	add_child(body)

func _build_player() -> void:
	player = CharacterBody2D.new()
	player.position = Vector2(300, 760)   # PLAYER_START(白い広場の左)
	player.motion_mode = CharacterBody2D.MOTION_MODE_FLOATING  # トップダウン: 全方向で素直に壁ずり
	player.z_index = 1                                          # オブジェクトより手前に描く
	player_spr = Sprite2D.new()
	player_spr.texture = _tex("res://assets/tou_sprite_front.png")
	player_spr.scale = Vector2(0.35, 0.35)
	player.add_child(player_spr)
	var col := CollisionShape2D.new()
	var shape := CircleShape2D.new()
	shape.radius = 26.0
	col.shape = shape
	player.add_child(col)
	add_child(player)
	# カメラ追従
	cam = Camera2D.new()
	cam.position_smoothing_enabled = true
	cam.position_smoothing_speed = 6.0
	cam.limit_left = 0
	cam.limit_top = 0
	cam.limit_right = int(WORLD.x)
	cam.limit_bottom = int(WORLD.y)
	player.add_child(cam)
	cam.make_current()
	cam.reset_smoothing()   # 起動直後のカメラ滑り出しを防ぐ

func _place_objects() -> void:
	# ミオ（会話 Lv1→Lv2）
	_add_actor("res://assets/mio_sprite_front.png", Vector2(900, 660), 0.35)
	_add_sparkle(Vector2(900, 560))
	interactables.append({
		"pos": Vector2(900, 660), "radius": 120.0, "id": "mio",
		"prompt": "ミオに話しかける",
		"cb": Callable(self, "_talk_mio")
	})
	# 小包（記憶断片 Lv3）
	_add_actor("res://assets/package_object.png", Vector2(1500, 900), 0.5)
	_add_sparkle(Vector2(1500, 820))
	interactables.append({
		"pos": Vector2(1500, 900), "radius": 110.0, "id": "package",
		"prompt": "小包を調べる",
		"cb": Callable(self, "_open_package")
	})
	# 5席目の跡（見る/見ない → ログ逆流）
	var trace := ColorRect.new()
	trace.color = Color(0.72, 0.74, 0.82)
	trace.size = Vector2(90, 60)
	trace.position = Vector2(1950 - 45, 700 - 30)
	add_child(trace)
	interactables.append({
		"pos": Vector2(1950, 700), "radius": 120.0, "id": "seat",
		"prompt": "五つ目の席の跡…",
		"cb": Callable(self, "_seat_trace")
	})
	# 時計塔入口（エリア遷移）
	var gate := ColorRect.new()
	gate.color = Color(0.35, 0.36, 0.46)
	gate.size = Vector2(120, 180)
	gate.position = Vector2(2400 - 60, 420 - 90)
	add_child(gate)
	interactables.append({
		"pos": Vector2(2400, 420), "radius": 130.0, "id": "gate",
		"prompt": "時計塔へ向かう",
		"cb": Callable(self, "_go_clocktower")
	})

func _add_actor(path: String, pos: Vector2, s: float) -> Sprite2D:
	var spr := Sprite2D.new()
	spr.texture = _tex(path)
	spr.scale = Vector2(s, s)
	spr.position = pos
	add_child(spr)
	return spr

func _add_sparkle(pos: Vector2) -> void:
	var spr := Sprite2D.new()
	spr.texture = _tex("res://assets/interact_sparkle.png")
	spr.scale = Vector2(0.5, 0.5)
	spr.position = pos
	spr.modulate = Color(1, 1, 1, 0.85)
	add_child(spr)
	var tw := create_tween().set_loops()
	tw.tween_property(spr, "modulate:a", 0.35, 0.9)
	tw.tween_property(spr, "modulate:a", 0.85, 0.9)

func _tex(path: String) -> Texture2D:
	if ResourceLoader.exists(path):
		return load(path)
	return null

# ---------- UI ----------
func _build_ui() -> void:
	var layer := CanvasLayer.new()
	add_child(layer)
	ui_root = Control.new()
	ui_root.set_anchors_preset(Control.PRESET_FULL_RECT)
	ui_root.mouse_filter = Control.MOUSE_FILTER_IGNORE
	ui_root.theme = _theme()
	layer.add_child(ui_root)

	# 恒常HUD（現在地・時計のみ）
	hud = Label.new()
	hud.text = "現在地：白い広場 ／ 17:17"
	hud.position = Vector2(0, 16)
	hud.size = Vector2(1264, 28)
	hud.horizontal_alignment = HORIZONTAL_ALIGNMENT_RIGHT
	ui_root.add_child(hud)

	# 近接プロンプト（近づいた時だけ）
	prompt = Label.new()
	prompt.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	prompt.size = Vector2(1280, 30)
	prompt.position = Vector2(0, 560)
	prompt.visible = false
	ui_root.add_child(prompt)

	# 暗幕（Lv3/遷移用）
	overlay = ColorRect.new()
	overlay.color = Color(0, 0, 0, 0)
	overlay.set_anchors_preset(Control.PRESET_FULL_RECT)
	overlay.mouse_filter = Control.MOUSE_FILTER_IGNORE
	ui_root.add_child(overlay)

	# バストアップ（Lv3）
	bust = TextureRect.new()
	bust.texture = _tex("res://assets/mio_sprite_front.png")
	bust.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	bust.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
	bust.size = Vector2(400, 470)
	bust.position = Vector2(440, 40)   # 会話パネル(y=540)の上に収める
	bust.visible = false
	ui_root.add_child(bust)

	# 会話パネル
	panel = Panel.new()
	panel.size = Vector2(1120, 150)
	panel.position = Vector2(80, 540)
	panel.visible = false
	panel.clip_contents = true
	ui_root.add_child(panel)
	face = TextureRect.new()
	face.size = Vector2(96, 96)
	face.position = Vector2(20, 27)
	face.expand_mode = TextureRect.EXPAND_IGNORE_SIZE      # 枠(96x96)に必ず収める
	face.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
	face.clip_contents = true
	panel.add_child(face)
	name_lbl = Label.new()
	name_lbl.position = Vector2(140, 12)
	panel.add_child(name_lbl)
	text_lbl = Label.new()
	text_lbl.position = Vector2(140, 46)
	text_lbl.size = Vector2(950, 90)
	text_lbl.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	panel.add_child(text_lbl)

	# 選択肢
	choices = VBoxContainer.new()
	choices.position = Vector2(440, 300)
	choices.size = Vector2(400, 200)
	choices.add_theme_constant_override("separation", 12)
	choices.visible = false
	ui_root.add_child(choices)

	# タイトルカード（遷移）
	title_card = Label.new()
	title_card.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	title_card.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
	title_card.set_anchors_preset(Control.PRESET_FULL_RECT)
	title_card.visible = false
	title_card.add_theme_font_size_override("font_size", 40)
	ui_root.add_child(title_card)

func _theme() -> Theme:
	var t := Theme.new()
	var fp := "res://assets/font_jp.ttf"
	if FileAccess.file_exists(fp):
		# import不要で生TTFを直接読む（ヘッドレスでもGUIでも動く）
		var f := FontFile.new()
		f.load_dynamic_font(fp)
		t.set_default_font(f)
	t.set_default_font_size(20)
	return t

# ---------- ループ ----------
func _physics_process(_dt: float) -> void:
	if state != "explore":
		player.velocity = Vector2.ZERO
		return
	var dir := Input.get_vector("move_left", "move_right", "move_up", "move_down")
	player.velocity = dir * SPEED
	player.move_and_slide()
	# 歩行の"生き"付け: 進行方向で反転＋軽い上下バウンド（仮アニメ）
	if dir.x != 0.0:
		player_spr.flip_h = dir.x < 0.0
	if dir != Vector2.ZERO:
		_walk_t += _dt * 12.0
		player_spr.position.y = -absf(sin(_walk_t)) * 4.0
	else:
		_walk_t = 0.0
		player_spr.position.y = 0.0

func _process(_dt: float) -> void:
	if state != "explore":
		return
	# 近接判定（最も近い対象）
	near = null
	var best := INF
	for it in interactables:
		var d: float = player.position.distance_to(it["pos"])
		if d <= it["radius"] and d < best:
			best = d
			near = it
	if near:
		prompt.text = "[ Space ] " + near["prompt"]
		prompt.visible = true
	else:
		prompt.visible = false

func _unhandled_input(e: InputEvent) -> void:
	if not e.is_action_pressed("ui_accept"):
		return
	match state:
		"explore":
			if near:
				var it = near
				near = null
				prompt.visible = false
				(it["cb"] as Callable).call()
		"dialogue":
			_advance_dialogue()

# ---------- 会話 ----------
func _say(face_path: String, who: String, lines: Array, level: int, on_end := Callable()) -> void:
	state = "dialogue"
	dq = lines.duplicate()
	dq_end = on_end
	panel.visible = true
	face.texture = _tex(face_path) if face_path != "" else null
	name_lbl.text = who
	# Lv2は不穏さ: 名前色をくすませ、顔をわずかに暗く
	if level >= 2:
		name_lbl.modulate = Color(0.75, 0.78, 0.85)
		face.modulate = Color(0.85, 0.85, 0.9)
	else:
		name_lbl.modulate = Color(1, 1, 1)
		face.modulate = Color(1, 1, 1)
	_advance_dialogue()

func _advance_dialogue() -> void:
	if dq.is_empty():
		panel.visible = false
		bust.visible = false
		_fade_overlay(0.0)
		state = "explore"
		if dq_end.is_valid():
			dq_end.call()
		return
	text_lbl.text = String(dq.pop_front())

# ---------- 各インタラクション ----------
func _talk_mio() -> void:
	var f := "res://assets/mio_sprite_front.png"
	if flags.get("package_opened", false):
		# 開封後は不穏な反応版(Lv2)
		_say(f, "ミオ", [
			"……それ、どこで見つけたの。",
			"変だね。知らないはずなのに、怖い。",
			"名前を呼ばれると、少しだけ戻ってこられる気がする。",
		], 2)
	else:
		_say(f, "ミオ", [
			"……ここ、静かだね。",
			"あのね、五分だけ。いつもそう言ってる気がする。",
			"最初の日だけ、思い出せないの。",
		], 1)

func _open_package() -> void:
	flags["package_opened"] = true
	# Lv3: 暗幕＋バストアップの記憶シーン
	_fade_overlay(0.6)
	bust.visible = true
	_say("res://assets/mio_sprite_front.png", "記憶の断片", [
		"白いリボン。",
		"髪と、リボンと、白紙の手紙。",
		"（誰かの気配が、指先に残っている）",
	], 3)

func _seat_trace() -> void:
	_choice("五つ目の席の跡がある。", [
		{ "text": "よく見る", "cb": Callable(self, "_seat_look") },
		{ "text": "見ないでおく", "cb": Callable(self, "_seat_avoid") },
	])

func _seat_avoid() -> void:
	_say("res://assets/mio_sprite_front.png", "ミオ", [
		"……見ないの？",
		"うん。今のは、たぶん正しい。",
	], 2)

func _seat_look() -> void:
	# ログ逆流演出（1回）
	state = "busy"
	_hide_all_dialogue()
	_fade_overlay(0.85)
	title_card.visible = true
	title_card.add_theme_font_size_override("font_size", 22)
	var seq := [
		"17:17  通知を受信",
		"17:14  「見た」",
		"17:11  ████（名前）████",
		"17:08  ……文字が、逆順に解ける",
		"17:04  五つ目の席：存在してはいけない",
	]
	title_card.text = ""
	for i in range(seq.size()):
		title_card.text = ""
		for j in range(i + 1):
			title_card.text += seq[j] + "\n"
		await get_tree().create_timer(0.6).timeout
	title_card.text += "\n── ミオの名前が、白く抜ける ──"
	await get_tree().create_timer(1.2).timeout
	title_card.visible = false
	_fade_overlay(0.0)
	state = "explore"

func _go_clocktower() -> void:
	state = "busy"
	_hide_all_dialogue()
	# フェード＋タイトルカード＋スタブ
	await _fade_overlay_async(1.0, 0.6)
	title_card.add_theme_font_size_override("font_size", 40)
	title_card.text = "⑤ 時計塔前\n17:17"
	title_card.visible = true
	await get_tree().create_timer(1.0).timeout
	title_card.text = "（スタブ）\nこの先は Chapter01 本実装で"
	await get_tree().create_timer(1.4).timeout
	title_card.visible = false
	await _fade_overlay_async(0.0, 0.6)
	# 部屋に戻す（プロト範囲）
	player.position = Vector2(2260, 420)
	state = "explore"

# ---------- 選択肢 ----------
func _choice(prompt_text: String, opts: Array) -> void:
	state = "choice"
	_hide_all_dialogue()
	for c in choices.get_children():
		c.queue_free()
	var head := Label.new()
	head.text = prompt_text
	head.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	choices.add_child(head)
	for o in opts:
		var b := Button.new()
		b.text = String(o["text"])
		var cb: Callable = o["cb"]
		b.pressed.connect(func():
			choices.visible = false
			state = "explore"
			cb.call()
		)
		choices.add_child(b)
	choices.visible = true
	# キーボード/パッドで選択肢を確定できるよう先頭ボタンにフォーカス
	for c in choices.get_children():
		if c is Button:
			(c as Button).grab_focus()
			break

# ---------- 補助 ----------
func _hide_all_dialogue() -> void:
	panel.visible = false
	bust.visible = false
	choices.visible = false
	prompt.visible = false

func _fade_overlay(a: float) -> void:
	create_tween().tween_property(overlay, "color:a", a, 0.4)

func _fade_overlay_async(a: float, t: float) -> void:
	var tw := create_tween()
	tw.tween_property(overlay, "color:a", a, t)
	await tw.finished
