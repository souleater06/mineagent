import math
from pathlib import Path

import bpy
from mathutils import Vector


AUTO_RENDER_STILL = False
AUTO_RENDER_ANIMATION = False
STILL_PREVIEW_FRAME = 205

ROOT_DIR = Path(__file__).resolve().parent
RENDER_DIR = ROOT_DIR / "renders"
STILL_PATH = RENDER_DIR / "rubikflow_agent_still.png"
ANIMATION_PATH = RENDER_DIR / "rubikflow_agent_demo.mp4"

MOVES = ["U", "F", "R", "F", "D", "B"]
FRAMES_PER_MOVE = 35
TOTAL_FRAMES = 210

CANVAS_WIDTH = 13.35
CANVAS_HEIGHT = 7.35
APP_SHELL = {"x": 0.00, "z": -0.02, "w": 13.10, "h": 7.15}
GAP = 0.22
PADDING = 0.20

# Fit-to-canvas ratios inside the app shell:
# left 26%, center 40%, right 34%, with a bottom timeline band.
LEFT_PANEL = {"x": -4.77, "z": 0.48, "w": 3.25, "h": 5.75}
CENTER_PANEL = {"x": -0.62, "z": 0.48, "w": 4.90, "h": 5.75}
RIGHT_PANEL = {"x": 4.32, "z": 0.48, "w": 4.50, "h": 5.75}
TIMELINE_PANEL = {"x": 0.00, "z": -3.05, "w": 12.55, "h": 0.78}

# The camera looks along world +Y, so smaller Y values are closer.
Z_BACKGROUND = 0.34
Z_CARD = 0.10
Z_TILE = -0.02
Z_HIGHLIGHT = -0.10
Z_OUTPUT = -0.18
Z_ARROW = -0.25
Z_ICON = -0.32
Z_TEXT = -0.42

UI_ROTATION = (math.radians(90), 0, 0)
CUBE_Y = -0.62

FACE_COLORS = {
    "U": "cube_green",
    "D": "cube_yellow",
    "F": "cube_blue",
    "B": "cube_white",
    "R": "cube_red",
    "L": "cube_orange",
}

MOVE_CONFIG = {
    "U": {"axis": "z", "value": 1, "turn_axis": "z", "degrees": 90, "face": "TOP", "color": FACE_COLORS["U"]},
    "D": {"axis": "z", "value": -1, "turn_axis": "z", "degrees": -90, "face": "DOWN", "color": FACE_COLORS["D"]},
    "F": {"axis": "y", "value": -1, "turn_axis": "y", "degrees": -90, "face": "FRONT", "color": FACE_COLORS["F"]},
    "B": {"axis": "y", "value": 1, "turn_axis": "y", "degrees": 90, "face": "BACK", "color": FACE_COLORS["B"]},
    "R": {"axis": "x", "value": 1, "turn_axis": "x", "degrees": -90, "face": "RIGHT", "color": FACE_COLORS["R"]},
    "L": {"axis": "x", "value": -1, "turn_axis": "x", "degrees": 90, "face": "LEFT", "color": FACE_COLORS["L"]},
}

MODULES = [
    "+BLOCK", "CLAY", "VOXEL", "JOINT", "MIRROR",
    "SCALE", "COLOR", "SCAN", "AGENT", "PRINT",
    "EXPORT", "SHELL", "HOLLOW", "STACK", "LOCK",
    "LOOP", "CHECK", "FIX", "BUILD", "SAVE",
]

TIMELINE = ["SELECT", "BLOCK", "LOGIC", "CLAY", "LOCK", "PRINT"]

MODULE_STYLE = {
    "+BLOCK": ("blue", "B"),
    "CLAY": ("orange", "C"),
    "VOXEL": ("teal", "V"),
    "JOINT": ("red", "J"),
    "MIRROR": ("red", "M"),
    "SCALE": ("green", "S"),
    "COLOR": ("orange", "C"),
    "SCAN": ("teal", "S"),
    "AGENT": ("purple", "A"),
    "PRINT": ("purple", "P"),
    "EXPORT": ("blue", "E"),
    "SHELL": ("teal", "S"),
    "HOLLOW": ("orange", "H"),
    "STACK": ("blue", "S"),
    "LOCK": ("yellow", "L"),
    "LOOP": ("teal", "L"),
    "CHECK": ("green", "C"),
    "FIX": ("red", "F"),
    "BUILD": ("blue", "B"),
    "SAVE": ("blue", "S"),
}

STAGE_STYLE = {
    "SELECT": ("blue", "S"),
    "BLOCK": ("blue", "B"),
    "LOGIC": ("red", "L"),
    "CLAY": ("orange", "C"),
    "LOCK": ("yellow", "L"),
    "PRINT": ("purple", "P"),
}

ACTIONS = [
    {
        "move": "U",
        "module": "AGENT",
        "timeline": "SELECT",
        "command": "SELECT",
        "output": "READY",
        "score": "1600",
        "combo": "x1",
        "printability": "WAIT",
        "status": "READY",
        "mode": "SELECT",
        "progress": "0%",
        "progress_value": 0.00,
    },
    {
        "move": "F",
        "module": "+BLOCK",
        "timeline": "BLOCK",
        "command": "BLOCK",
        "output": "BASIC BLOCK",
        "score": "2500",
        "combo": "x2",
        "printability": "PROTO",
        "status": "ACTIVE",
        "mode": "BLOCK",
        "progress": "24%",
        "progress_value": 0.24,
    },
    {
        "move": "R",
        "module": "JOINT",
        "timeline": "LOGIC",
        "command": "UPGRADE LOGIC",
        "output": "LOGIC NETWORK",
        "score": "3600",
        "combo": "x3",
        "printability": "PROTO",
        "status": "ACTIVE",
        "mode": "LOGIC",
        "progress": "45%",
        "progress_value": 0.45,
    },
    {
        "move": "F",
        "module": "CLAY",
        "timeline": "CLAY",
        "command": "ADD CLAY",
        "output": "CLAY SHELL",
        "score": "5200",
        "combo": "x4",
        "printability": "PROTO",
        "status": "ACTIVE",
        "mode": "CLAY",
        "progress": "68%",
        "progress_value": 0.68,
    },
    {
        "move": "D",
        "module": "LOCK",
        "timeline": "LOCK",
        "command": "CONFIRM LOCK",
        "output": "LOCKED",
        "score": "6800",
        "combo": "x5",
        "printability": "STABLE",
        "status": "ACTIVE",
        "mode": "LOCK",
        "progress": "84%",
        "progress_value": 0.84,
    },
    {
        "move": "B",
        "module": "PRINT",
        "timeline": "PRINT",
        "command": "PREPARE PRINT",
        "output": "PRINT READY",
        "score": "8200",
        "combo": "x6",
        "printability": "READY",
        "status": "READY",
        "mode": "PRINT",
        "progress": "100%",
        "progress_value": 1.00,
    },
]


def clear_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def make_mat(name, color, roughness=0.86):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = color
    bsdf.inputs["Roughness"].default_value = roughness
    if "Alpha" in bsdf.inputs:
        bsdf.inputs["Alpha"].default_value = color[3]
    mat.diffuse_color = color
    return mat


def create_materials():
    return {
        "bg": make_mat("cream background", (0.94, 0.92, 0.86, 1)),
        "app": make_mat("warm app panel", (0.985, 0.975, 0.940, 1)),
        "card": make_mat("clean white card", (1.0, 0.995, 0.965, 1)),
        "tile": make_mat("soft tile", (0.980, 0.970, 0.930, 1)),
        "tile_alt": make_mat("soft tile alt", (0.955, 0.972, 0.955, 1)),
        "border": make_mat("thin warm border", (0.78, 0.75, 0.68, 1)),
        "ink": make_mat("ink black", (0.035, 0.034, 0.030, 1)),
        "muted": make_mat("muted text", (0.33, 0.35, 0.38, 1)),
        "white": make_mat("white text", (1.0, 1.0, 0.96, 1)),
        "blue": make_mat("soft blue", (0.22, 0.52, 0.88, 1)),
        "blue_fill": make_mat("pale blue fill", (0.78, 0.88, 0.98, 1)),
        "green": make_mat("success green", (0.22, 0.64, 0.26, 1)),
        "green_fill": make_mat("pale green fill", (0.82, 0.94, 0.80, 1)),
        "purple": make_mat("soft purple", (0.42, 0.24, 0.78, 1)),
        "purple_fill": make_mat("pale purple fill", (0.89, 0.84, 0.97, 1)),
        "orange": make_mat("soft orange", (0.96, 0.45, 0.08, 1)),
        "orange_fill": make_mat("pale orange fill", (0.98, 0.86, 0.68, 1)),
        "yellow": make_mat("soft yellow", (0.96, 0.70, 0.14, 1)),
        "yellow_fill": make_mat("pale yellow fill", (0.98, 0.91, 0.60, 1)),
        "red": make_mat("logic red", (0.90, 0.16, 0.10, 1)),
        "red_fill": make_mat("pale red fill", (0.98, 0.80, 0.76, 1)),
        "teal": make_mat("soft teal", (0.10, 0.62, 0.62, 1)),
        "gray_block": make_mat("output gray block", (0.56, 0.57, 0.55, 1)),
        "gray_block_dark": make_mat("output dark gray block", (0.38, 0.39, 0.38, 1)),
        "work": make_mat("output work area", (0.935, 0.940, 0.920, 1)),
        "cube_dark": make_mat("cube black plastic", (0.035, 0.035, 0.035, 1)),
        "cube_green": make_mat("cube green face", (0.46, 0.78, 0.40, 1)),
        "cube_yellow": make_mat("cube yellow face", (0.98, 0.78, 0.18, 1)),
        "cube_blue": make_mat("cube blue face", (0.15, 0.45, 0.88, 1)),
        "cube_red": make_mat("cube red face", (0.90, 0.24, 0.17, 1)),
        "cube_orange": make_mat("cube orange face", (0.95, 0.50, 0.12, 1)),
        "cube_white": make_mat("cube white face", (0.94, 0.94, 0.90, 1)),
    }


def panel(name, x, z, w, h, material, y=Z_CARD, radius=0.08, depth=0.020, shadow=False):
    bpy.ops.mesh.primitive_cube_add(size=1, location=(x, y, z))
    obj = bpy.context.object
    obj.name = name
    obj.scale = (w / 2, depth, h / 2)
    obj.data.materials.append(material)
    bevel = obj.modifiers.new(name="soft radius", type="BEVEL")
    bevel.width = radius
    bevel.segments = 6
    obj.modifiers.new(name="weighted normals", type="WEIGHTED_NORMAL")
    if shadow:
        obj.location.y = y + 0.010
    return obj


def text(name, body, x, z, size, material, align="CENTER"):
    bpy.ops.object.text_add(location=(x, Z_TEXT, z), rotation=UI_ROTATION)
    obj = bpy.context.object
    obj.name = name
    obj.data.body = body
    obj.data.align_x = align
    obj.data.align_y = "CENTER"
    obj.data.size = size
    obj.data.extrude = 0.001
    obj.data.materials.append(material)
    return obj


def line(name, points, material, width=0.012):
    curve = bpy.data.curves.new(name, type="CURVE")
    curve.dimensions = "3D"
    curve.resolution_u = 2
    curve.bevel_depth = width
    curve.bevel_resolution = 3
    spline = curve.splines.new("POLY")
    spline.points.add(len(points) - 1)
    for point, co in zip(spline.points, points):
        point.co = (co[0], co[1], co[2], 1)
    obj = bpy.data.objects.new(name, curve)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(material)
    return obj


def set_visible(obj, frame, visible):
    obj.hide_viewport = not visible
    obj.hide_render = not visible
    obj.keyframe_insert(data_path="hide_viewport", frame=frame)
    obj.keyframe_insert(data_path="hide_render", frame=frame)


def set_group_visible(group, frame, visible):
    for obj in group:
        set_visible(obj, frame, visible)


def remember_scale(obj):
    obj["sx"] = obj.scale.x
    obj["sy"] = obj.scale.y
    obj["sz"] = obj.scale.z
    return obj


def reveal_group(group, frame):
    for obj in group:
        final_scale = (obj.get("sx", obj.scale.x), obj.get("sy", obj.scale.y), obj.get("sz", obj.scale.z))
        obj.scale = (0.001, 0.001, 0.001)
        obj.keyframe_insert(data_path="scale", frame=max(1, frame - 1))
        obj.scale = final_scale
        obj.keyframe_insert(data_path="scale", frame=frame + 8)


def parent_local(child, parent, local_location):
    child.parent = parent
    child.location = local_location
    return child


def cube_sticker(name, parent, local_location, scale, material):
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0))
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    obj.data.materials.append(material)
    bevel = obj.modifiers.new(name="sticker radius", type="BEVEL")
    bevel.width = 0.006
    bevel.segments = 2
    obj.modifiers.new(name="sticker normals", type="WEIGHTED_NORMAL")
    return parent_local(obj, parent, local_location)


def create_cube(materials):
    root = bpy.data.objects.new("Smart Cube Digital Twin", None)
    bpy.context.collection.objects.link(root)
    root.location = (LEFT_PANEL["x"], CUBE_Y, 0.70)
    root.rotation_euler = (math.radians(-18), math.radians(28), math.radians(-10))
    cubelets = []
    spacing = 0.375
    size = 0.320
    sticker = 0.240
    thick = 0.011
    face_mats = {move: materials[mat] for move, mat in FACE_COLORS.items()}
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            for z in [-1, 0, 1]:
                bpy.ops.mesh.primitive_cube_add(size=size, location=(0, 0, 0))
                c = bpy.context.object
                c.name = f"clean_cubelet_{x}_{y}_{z}"
                c.data.materials.append(materials["cube_dark"])
                bevel = c.modifiers.new(name="cubelet radius", type="BEVEL")
                bevel.width = 0.014
                bevel.segments = 3
                c.modifiers.new(name="cubelet normals", type="WEIGHTED_NORMAL")
                loc = (x * spacing, y * spacing, z * spacing)
                parent_local(c, root, loc)
                c["cube_coord_x"] = x
                c["cube_coord_y"] = y
                c["cube_coord_z"] = z
                c["home_x"] = loc[0]
                c["home_y"] = loc[1]
                c["home_z"] = loc[2]
                cubelets.append(c)
                if z == 1:
                    cube_sticker(f"U_clean_sticker_{x}_{y}_{z}", c, (0, 0, size / 2 + thick), (sticker / 2, sticker / 2, thick), face_mats["U"])
                if z == -1:
                    cube_sticker(f"D_clean_sticker_{x}_{y}_{z}", c, (0, 0, -size / 2 - thick), (sticker / 2, sticker / 2, thick), face_mats["D"])
                if x == 1:
                    cube_sticker(f"R_clean_sticker_{x}_{y}_{z}", c, (size / 2 + thick, 0, 0), (thick, sticker / 2, sticker / 2), face_mats["R"])
                if x == -1:
                    cube_sticker(f"L_clean_sticker_{x}_{y}_{z}", c, (-size / 2 - thick, 0, 0), (thick, sticker / 2, sticker / 2), face_mats["L"])
                if y == -1:
                    cube_sticker(f"F_clean_sticker_{x}_{y}_{z}", c, (0, -size / 2 - thick, 0), (sticker / 2, thick, sticker / 2), face_mats["F"])
                if y == 1:
                    cube_sticker(f"B_clean_sticker_{x}_{y}_{z}", c, (0, size / 2 + thick, 0), (sticker / 2, thick, sticker / 2), face_mats["B"])
    return {"root": root, "cubelets": cubelets}


def create_left_panel(materials):
    data = {"move_active": [], "move_done": [], "face_groups": [], "lens_groups": [], "map_groups": [], "arrows": []}
    x = LEFT_PANEL["x"]
    panel("left_shell", x, LEFT_PANEL["z"], LEFT_PANEL["w"], LEFT_PANEL["h"], materials["app"], y=Z_CARD, radius=0.14, depth=0.050, shadow=True)
    text("left_title", "Smart Cube Input", x, 3.08, 0.205, materials["ink"])

    start_x = x - 1.13
    for i, move in enumerate(MOVES):
        cx = start_x + i * 0.45
        panel(f"clean_move_chip_{i}", cx, 2.62, 0.39, 0.39, materials["tile"], y=Z_TILE, radius=0.075)
        data["move_active"].append([panel(f"clean_move_active_{i}", cx, 2.62, 0.47, 0.47, materials["green_fill"], y=Z_HIGHLIGHT, radius=0.090)])
        data["move_done"].append([
            panel(f"clean_move_done_{i}", cx, 2.62, 0.43, 0.43, materials["green_fill"], y=Z_HIGHLIGHT, radius=0.080),
            panel(f"clean_move_check_badge_{i}", cx + 0.15, 2.47, 0.15, 0.15, materials["green"], y=Z_ICON, radius=0.040),
            text(f"clean_move_check_{i}", "v", cx + 0.15, 2.47, 0.060, materials["white"]),
        ])
        text(f"clean_move_text_{i}", move, cx, 2.62, 0.135, materials["ink"])

    panel("active_face_card", x, 2.02, 2.76, 0.72, materials["card"], y=Z_TILE, radius=0.10)
    for i, action in enumerate(ACTIONS):
        cfg = MOVE_CONFIG[action["move"]]
        mat = materials[cfg["color"]]
        data["face_groups"].append([
            panel(f"active_face_color_{i}", x - 0.88, 2.00, 0.66, 0.50, mat, y=Z_ICON, radius=0.075),
            text(f"active_face_move_{i}", action["move"], x - 0.88, 2.00, 0.170, materials["ink"]),
            text(f"active_face_label_{i}", f"{action['move']} FACE", x - 0.30, 2.08, 0.140, materials["ink"], align="LEFT"),
            text(f"active_face_hint_{i}", cfg["face"], x - 0.30, 1.82, 0.084, materials["muted"], align="LEFT"),
        ])

    panel("cube_display_card", x, 0.70, 2.76, 1.92, materials["card"], y=Z_TILE, radius=0.12)
    panel("cube_shadow", x, -0.10, 1.70, 0.20, materials["cube_dark"], y=Z_HIGHLIGHT, radius=0.045, depth=0.030)
    cube = create_cube(materials)

    arrow_specs = [
        ("U", [(x - 0.52, Z_ARROW, 1.34), (x - 0.02, Z_ARROW, 1.50), (x + 0.50, Z_ARROW, 1.32)], materials["green"]),
        ("F", [(x - 1.10, Z_ARROW, 0.58), (x - 1.22, Z_ARROW, 0.18), (x - 1.06, Z_ARROW, -0.20)], materials["blue"]),
        ("R", [(x + 1.06, Z_ARROW, 1.12), (x + 1.25, Z_ARROW, 0.64), (x + 1.06, Z_ARROW, 0.16)], materials["red"]),
        ("D", [(x - 0.55, Z_ARROW, -0.35), (x - 0.02, Z_ARROW, -0.52), (x + 0.52, Z_ARROW, -0.35)], materials["yellow"]),
        ("B", [(x + 0.88, Z_ARROW, 0.98), (x + 1.04, Z_ARROW, 0.50), (x + 0.86, Z_ARROW, 0.04)], materials["purple"]),
    ]
    for i, action in enumerate(ACTIONS):
        points, mat = next((pts, m) for move, pts, m in arrow_specs if move == action["move"])
        data["arrows"].append([line(f"clean_cube_arrow_{i}", points, mat, width=0.014)])

    panel("lens_card", x, -1.25, 2.76, 0.96, materials["card"], y=Z_TILE, radius=0.11)
    text("lens_title", "Cube Command Lens", x - 1.25, -0.88, 0.078, materials["ink"], align="LEFT")
    for i, action in enumerate(ACTIONS):
        cfg = MOVE_CONFIG[action["move"]]
        rows = [
            f"Move: {action['move']}",
            f"Face: {cfg['face']}",
            f"Command: {action['command']}",
            f"Output: {action['output']}",
        ]
        group = []
        for row, body in enumerate(rows):
            group.append(text(f"lens_clean_{i}_{row}", body, x - 1.25, -1.09 - row * 0.20, 0.066, materials["ink"], align="LEFT"))
        data["lens_groups"].append(group)

    panel("mapping_button", x, -2.32, 2.76, 0.42, materials["blue_fill"], y=Z_HIGHLIGHT, radius=0.10)
    for i, action in enumerate(ACTIONS):
        cfg = MOVE_CONFIG[action["move"]]
        data["map_groups"].append([text(f"mapping_clean_{i}", f"FACE TURN ({cfg['face']}) -> {action['command']}", x, -2.32, 0.056, materials["ink"])])

    data.update(cube)
    return data


def create_center_panel(materials):
    data = {"active_tiles": [], "info_groups": []}
    x = CENTER_PANEL["x"]
    panel("center_shell", x, CENTER_PANEL["z"], CENTER_PANEL["w"], CENTER_PANEL["h"], materials["app"], y=Z_CARD, radius=0.14, depth=0.050, shadow=True)
    text("clean_main_title", "RubikFlow Agent", x - 2.18, 3.08, 0.255, materials["ink"], align="LEFT")
    text("clean_main_subtitle", "cube move -> workflow tile -> agent output", x - 2.18, 2.77, 0.086, materials["muted"], align="LEFT")
    panel("opedia_clean_card", x, 0.80, 4.62, 3.92, materials["card"], y=Z_TILE, radius=0.12)
    text("opedia_clean_title", "Workflow-o-pedia", x - 2.05, 2.40, 0.145, materials["ink"], align="LEFT")

    tile_positions = {}
    start_x = x - 1.78
    start_z = 1.78
    gap_x = 0.89
    gap_z = 0.66
    for idx, label in enumerate(MODULES):
        col = idx % 5
        row = idx // 5
        tx = start_x + col * gap_x
        tz = start_z - row * gap_z
        tile_positions[label] = (tx, tz)
        panel(f"clean_tile_{idx}", tx, tz, 0.74, 0.50, materials["tile_alt"] if idx % 2 else materials["tile"], y=Z_TILE, radius=0.080)
        style, glyph = MODULE_STYLE[label]
        panel(f"clean_tile_icon_{idx}", tx, tz + 0.105, 0.30, 0.22, materials[style], y=Z_ICON, radius=0.055)
        text(f"clean_tile_glyph_{idx}", glyph, tx, tz + 0.105, 0.112, materials["white"])
        text(f"clean_tile_label_{idx}", label, tx, tz - 0.145, 0.084 if len(label) <= 5 else 0.070, materials["ink"])

    for i, action in enumerate(ACTIONS):
        tx, tz = tile_positions[action["module"]]
        style, _glyph = MODULE_STYLE[action["module"]]
        data["active_tiles"].append([panel(f"clean_active_tile_{i}", tx, tz, 0.88, 0.62, materials[f"{style}_fill"] if f"{style}_fill" in materials else materials["blue_fill"], y=Z_HIGHLIGHT, radius=0.100)])

    panel("clean_info_strip", x, -1.82, 4.62, 0.75, materials["card"], y=Z_TILE, radius=0.12)
    cols = [x - 1.48, x, x + 1.48]
    labels = ["Triggered Tile", "Agent Command", "Result"]
    for idx, label in enumerate(labels):
        text(f"clean_info_label_{idx}", label, cols[idx], -1.61, 0.062, materials["muted"])
    for i, action in enumerate(ACTIONS):
        vals = [action["module"], action["command"], action["output"] if action["timeline"] != "LOGIC" else "ACTIVE"]
        data["info_groups"].append([text(f"clean_info_value_{i}_{j}", vals[j], cols[j], -1.95, 0.083 if j != 1 else 0.074, materials["ink"]) for j in range(3)])
    return data


def create_right_panel(materials):
    data = {"metric_groups": {"score": [], "combo": [], "printability": []}, "state_groups": [], "pipeline_active": [], "pipeline_done": [], "output_groups": {}, "output_status": []}
    x = RIGHT_PANEL["x"]
    panel("right_shell", x, RIGHT_PANEL["z"], RIGHT_PANEL["w"], RIGHT_PANEL["h"], materials["app"], y=Z_CARD, radius=0.14, depth=0.050, shadow=True)

    metric_specs = [("SCORE", "score", x - 1.30), ("COMBO", "combo", x), ("PRINTABILITY", "printability", x + 1.30)]
    for label, key, mx in metric_specs:
        panel(f"metric_card_{key}", mx, 2.88, 1.12, 0.58, materials["card"], y=Z_TILE, radius=0.095)
        text(f"metric_label_{key}", label, mx, 3.05, 0.056 if key != "printability" else 0.047, materials["ink"])
        for i, action in enumerate(ACTIONS):
            data["metric_groups"][key].append(text(f"metric_value_{key}_{i}", action[key], mx, 2.76, 0.132 if key != "printability" else 0.086, materials["green"] if key == "printability" else materials["ink"]))

    panel("agent_state_card", x, 2.04, 4.10, 0.82, materials["card"], y=Z_TILE, radius=0.11)
    text("agent_state_title", "Agent State", x - 1.86, 2.31, 0.100, materials["ink"], align="LEFT")
    for row, label in enumerate(["Status", "Mode", "Progress"]):
        text(f"agent_state_label_{row}", label, x - 1.78, 2.10 - row * 0.22, 0.070, materials["muted"], align="LEFT")
    for i, action in enumerate(ACTIONS):
        vals = [action["status"], action["mode"], action["progress"]]
        group = []
        for row, val in enumerate(vals):
            group.append(text(f"agent_state_value_{i}_{row}", val, x - 0.70, 2.10 - row * 0.22, 0.082, materials["ink"], align="LEFT"))
        group.append(panel(f"state_progress_track_{i}", x + 0.78, 1.66, 1.32, 0.07, materials["border"], y=Z_HIGHLIGHT, radius=0.032))
        width = max(0.05, 1.32 * action["progress_value"])
        group.append(panel(f"state_progress_fill_{i}", x + 0.12 + width / 2, 1.66, width, 0.07, materials["blue"], y=Z_ARROW, radius=0.032))
        data["state_groups"].append(group)

    panel("pipeline_card", x, 1.05, 4.10, 0.78, materials["card"], y=Z_TILE, radius=0.11)
    text("pipeline_title", "Agent Function Pipeline", x - 1.86, 1.34, 0.082, materials["ink"], align="LEFT")
    chain_positions = {}
    for idx, label in enumerate(TIMELINE):
        cx = x - 1.30 + (idx % 3) * 1.30
        cz = 1.10 - (idx // 3) * 0.32
        style, glyph = STAGE_STYLE[label]
        panel(f"pipeline_chip_{idx}", cx, cz, 1.08, 0.25, materials["tile"], y=Z_TILE, radius=0.070)
        text(f"pipeline_text_{idx}", label, cx, cz, 0.066, materials["ink"])
        data["pipeline_done"].append([panel(f"pipeline_done_{idx}", cx, cz, 1.12, 0.29, materials["green_fill"], y=Z_HIGHLIGHT, radius=0.080)])
        data["pipeline_active"].append([panel(f"pipeline_active_{idx}", cx, cz, 1.18, 0.33, materials[f"{style}_fill"], y=Z_HIGHLIGHT, radius=0.085)])
        chain_positions[label] = idx

    data["pipeline_index"] = chain_positions
    create_output_preview(x, materials, data)
    return data


def create_output_preview(x, materials, data):
    panel("output_clean_card", x, -1.12, 4.10, 2.82, materials["card"], y=Z_TILE, radius=0.12)
    text("output_clean_title", "Output Preview", x - 1.86, 0.08, 0.118, materials["ink"], align="LEFT")
    model_x = x - 0.72
    status_x = x + 1.38
    panel("output_model_lane", model_x, -1.27, 2.55, 1.94, materials["work"], y=Z_TILE, radius=0.10)
    panel("output_status_lane", status_x, -1.27, 1.05, 1.94, materials["tile"], y=Z_TILE, radius=0.10)
    panel("output_status_command_chip", status_x, -0.94, 0.92, 0.44, materials["purple_fill"], y=Z_HIGHLIGHT, radius=0.090)
    panel("output_status_result_chip", status_x, -1.58, 0.92, 0.42, materials["blue_fill"], y=Z_HIGHLIGHT, radius=0.090)

    data["output_status"] = []
    for i, action in enumerate(ACTIONS):
        cmd = action["command"]
        if cmd == "UPGRADE LOGIC":
            cmd = "UPGRADE\nLOGIC"
        elif cmd == "CONFIRM LOCK":
            cmd = "CONFIRM\nLOCK"
        elif cmd == "PREPARE PRINT":
            cmd = "PREPARE\nPRINT"
        result = "ACTIVE" if action["timeline"] == "LOGIC" else ("BUILDING" if action["timeline"] == "CLAY" else action["output"])
        data["output_status"].append([
            text(f"output_status_cmd_{i}", cmd, status_x, -0.94, 0.058, materials["ink"]),
            text(f"output_status_result_{i}", result, status_x, -1.58, 0.074, materials["ink"]),
        ])

    ready = [text("output_ready_clean", "READY", model_x, -1.25, 0.125, materials["muted"])]
    basic = []
    origin_x = model_x - 0.88
    origin_z = -1.78
    for row in range(4):
        for col in range(5):
            basic.append(panel(f"clean_base_block_{row}_{col}", origin_x + col * 0.36, origin_z + row * 0.23, 0.32, 0.20, materials["gray_block"], y=Z_OUTPUT, radius=0.025, depth=0.045))
    for loc in [(model_x - 0.30, -1.22), (model_x + 0.05, -1.22), (model_x - 0.30, -1.48), (model_x + 0.05, -1.48)]:
        basic.append(panel(f"clean_center_block_{len(basic)}", loc[0], loc[1], 0.34, 0.23, materials["gray_block_dark"], y=Z_OUTPUT - 0.020, radius=0.030, depth=0.060))

    logic = [
        line("clean_logic_line_a", [(model_x - 0.90, Z_OUTPUT - 0.050, -1.65), (model_x - 0.42, Z_OUTPUT - 0.050, -1.36), (model_x + 0.40, Z_OUTPUT - 0.050, -1.62)], materials["red"], width=0.022),
        line("clean_logic_line_b", [(model_x - 0.42, Z_OUTPUT - 0.055, -1.36), (model_x - 0.22, Z_OUTPUT - 0.055, -0.84), (model_x + 0.48, Z_OUTPUT - 0.055, -0.98)], materials["red"], width=0.019),
    ]
    for idx, loc in enumerate([(model_x - 0.90, -1.65), (model_x - 0.42, -1.36), (model_x + 0.40, -1.62), (model_x - 0.22, -0.84), (model_x + 0.48, -0.98)]):
        logic.append(panel(f"clean_logic_node_{idx}", loc[0], loc[1], 0.21, 0.21, materials["red"], y=Z_OUTPUT - 0.070, radius=0.055, depth=0.035))

    clay = [panel("clean_clay_shell_wash", model_x - 0.16, -1.34, 1.68, 1.18, materials["orange_fill"], y=Z_OUTPUT - 0.090, radius=0.130, depth=0.030)]
    for idx, loc in enumerate([
        (model_x - 0.88, -0.96), (model_x - 0.52, -0.80), (model_x - 0.16, -0.80), (model_x + 0.36, -0.96),
        (model_x - 0.92, -1.30), (model_x + 0.42, -1.30), (model_x - 0.92, -1.62), (model_x + 0.42, -1.62),
        (model_x - 0.78, -1.92), (model_x - 0.42, -2.02), (model_x - 0.06, -2.02), (model_x + 0.34, -1.92),
    ]):
        clay.append(panel(f"clean_clay_voxel_{idx}", loc[0], loc[1], 0.28, 0.20, materials["orange"], y=Z_OUTPUT - 0.100, radius=0.040, depth=0.040))

    lock = []
    for idx, loc in enumerate([(model_x - 0.82, -1.04), (model_x - 0.46, -0.84), (model_x + 0.32, -0.90), (model_x + 0.36, -1.72), (model_x - 0.46, -1.84)]):
        lock.append(panel(f"clean_lock_icon_{idx}", loc[0], loc[1], 0.24, 0.24, materials["yellow"], y=Z_OUTPUT - 0.125, radius=0.065, depth=0.040))
        lock.append(text(f"clean_lock_text_{idx}", "L", loc[0], loc[1], 0.082, materials["ink"]))
    lock.append(panel("clean_locked_badge", model_x, -2.10, 1.10, 0.32, materials["yellow_fill"], y=Z_OUTPUT - 0.130, radius=0.080))
    lock.append(text("clean_locked_text", "LOCKED", model_x, -2.10, 0.082, materials["ink"]))

    print_group = [panel("clean_print_bed", model_x, -2.04, 2.08, 0.24, materials["ink"], y=Z_OUTPUT, radius=0.045, depth=0.060)]
    for i in range(7):
        print_group.append(panel(f"clean_slice_line_{i}", model_x, -1.82 + i * 0.14, 1.86, 0.018, materials["blue"], y=Z_OUTPUT - 0.050, radius=0.004, depth=0.008))
    print_group.append(panel("clean_print_ready_badge", model_x, -0.72, 1.24, 0.32, materials["green_fill"], y=Z_OUTPUT - 0.040, radius=0.080))
    print_group.append(text("clean_print_ready_text", "PRINT READY", model_x, -0.72, 0.080, materials["ink"]))

    data["output_groups"] = {
        "ready": ready,
        "basic": basic,
        "logic": logic,
        "clay": clay,
        "lock": lock,
        "print": print_group,
    }
    for group_name, group in data["output_groups"].items():
        if group_name == "ready":
            continue
        for obj in group:
            remember_scale(obj)
            obj.scale = (0.001, 0.001, 0.001)
            obj.keyframe_insert(data_path="scale", frame=1)


def create_timeline(materials):
    data = {"active": [], "done": []}
    x = TIMELINE_PANEL["x"]
    z = TIMELINE_PANEL["z"]
    panel("timeline_clean_shell", x, z, TIMELINE_PANEL["w"], TIMELINE_PANEL["h"], materials["app"], y=Z_CARD, radius=0.13, depth=0.040, shadow=True)
    text("timeline_clean_title", "Workflow Timeline", -5.95, z, 0.085, materials["ink"], align="LEFT")
    start_x = -4.45
    gap = 1.72
    for i, label in enumerate(TIMELINE):
        cx = start_x + i * gap
        style, glyph = STAGE_STYLE[label]
        panel(f"timeline_clean_node_{i}", cx, z, 1.18, 0.44, materials["tile"], y=Z_TILE, radius=0.115)
        panel(f"timeline_clean_icon_{i}", cx - 0.36, z, 0.23, 0.23, materials[style], y=Z_ICON, radius=0.055)
        text(f"timeline_clean_glyph_{i}", glyph, cx - 0.36, z, 0.070, materials["white"])
        text(f"timeline_clean_text_{i}", label, cx + 0.15, z, 0.075, materials["ink"])
        data["done"].append([
            panel(f"timeline_clean_done_fill_{i}", cx, z, 1.22, 0.48, materials["green_fill"], y=Z_HIGHLIGHT, radius=0.125),
            panel(f"timeline_clean_done_badge_{i}", cx + 0.49, z - 0.15, 0.16, 0.16, materials["green"], y=Z_ICON, radius=0.045),
            text(f"timeline_clean_done_check_{i}", "v", cx + 0.49, z - 0.15, 0.062, materials["white"]),
        ])
        data["active"].append([panel(f"timeline_clean_active_{i}", cx, z, 1.30, 0.54, materials[f"{style}_fill"], y=Z_HIGHLIGHT, radius=0.140)])
    return data


def rotate_vector_quarter_turn(vector, axis, direction):
    x, y, z = vector.x, vector.y, vector.z
    if axis == "x":
        return Vector((x, -direction * z, direction * y))
    if axis == "y":
        return Vector((direction * z, y, -direction * x))
    return Vector((-direction * y, direction * x, z))


def animate_cube_layer(cube_data, move, start_frame, end_frame):
    cfg = MOVE_CONFIG[move]
    selected = [c for c in cube_data["cubelets"] if int(c[f"cube_coord_{cfg['axis']}"]) == cfg["value"]]
    axis = cfg["turn_axis"]
    direction = 1 if cfg["degrees"] > 0 else -1
    angle = math.radians(cfg["degrees"])
    rot = {"x": (angle, 0, 0), "y": (0, angle, 0), "z": (0, 0, angle)}[axis]
    mid = start_frame + 18
    for c in selected:
        home = Vector((c["home_x"], c["home_y"], c["home_z"]))
        c.location = home
        c.rotation_euler = (0, 0, 0)
        c.keyframe_insert(data_path="location", frame=start_frame)
        c.keyframe_insert(data_path="rotation_euler", frame=start_frame)
        c.location = rotate_vector_quarter_turn(home, axis, direction)
        c.rotation_euler = rot
        c.keyframe_insert(data_path="location", frame=mid)
        c.keyframe_insert(data_path="rotation_euler", frame=mid)
        c.location = home
        c.rotation_euler = (0, 0, 0)
        c.keyframe_insert(data_path="location", frame=end_frame)
        c.keyframe_insert(data_path="rotation_euler", frame=end_frame)


def stage_index(label):
    return TIMELINE.index(label)


def animate_scene(left, center, right, timeline):
    for i, action in enumerate(ACTIONS):
        frame = 1 + i * FRAMES_PER_MOVE
        end = min(TOTAL_FRAMES, frame + FRAMES_PER_MOVE - 1)
        animate_cube_layer(left, action["move"], frame, end)
        for idx in range(len(ACTIONS)):
            set_group_visible(left["move_active"][idx], frame, idx == i)
            set_group_visible(left["move_done"][idx], frame, idx < i)
            set_group_visible(left["face_groups"][idx], frame, idx == i)
            set_group_visible(left["lens_groups"][idx], frame, idx == i)
            set_group_visible(left["map_groups"][idx], frame, idx == i)
            set_group_visible(left["arrows"][idx], frame, idx == i)
            set_group_visible(center["active_tiles"][idx], frame, idx == i)
            set_group_visible(center["info_groups"][idx], frame, idx == i)
            set_group_visible(right["state_groups"][idx], frame, idx == i)
            set_group_visible(right["output_status"][idx], frame, idx == i)
            for metric_group in right["metric_groups"].values():
                set_visible(metric_group[idx], frame, idx == i)
        current_stage = stage_index(action["timeline"])
        for idx in range(len(TIMELINE)):
            set_group_visible(timeline["active"][idx], frame, idx == current_stage)
            set_group_visible(timeline["done"][idx], frame, idx < current_stage)
            set_group_visible(right["pipeline_active"][idx], frame, idx == current_stage)
            set_group_visible(right["pipeline_done"][idx], frame, idx < current_stage)
        if action["timeline"] == "BLOCK":
            reveal_group(right["output_groups"]["basic"], frame)
        elif action["timeline"] == "LOGIC":
            reveal_group(right["output_groups"]["logic"], frame)
        elif action["timeline"] == "CLAY":
            reveal_group(right["output_groups"]["clay"], frame)
        elif action["timeline"] == "LOCK":
            reveal_group(right["output_groups"]["lock"], frame)
        elif action["timeline"] == "PRINT":
            reveal_group(right["output_groups"]["print"], frame)
        set_group_visible(right["output_groups"]["ready"], frame, i == 0)


def setup_camera():
    bpy.ops.object.camera_add(location=(0, -12.0, 0), rotation=(math.radians(90), 0, 0))
    camera = bpy.context.object
    camera.name = "RubikFlow Clean Orthographic Camera"
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = CANVAS_HEIGHT
    camera.data.display_size = 0.12
    camera.hide_select = True
    camera.hide_viewport = True
    camera.hide_render = False
    bpy.context.scene.camera = camera
    return camera


def setup_world(materials):
    world = bpy.context.scene.world or bpy.data.worlds.new("RubikFlow Clean World")
    bpy.context.scene.world = world
    world.color = (0.94, 0.92, 0.86)
    panel("clean_background", 0, 0, CANVAS_WIDTH + 0.55, CANVAS_HEIGHT + 0.32, materials["bg"], y=Z_BACKGROUND, radius=0.02, depth=0.020)
    panel("fit_app_shell", APP_SHELL["x"], APP_SHELL["z"], APP_SHELL["w"], APP_SHELL["h"], materials["app"], y=Z_CARD + 0.065, radius=0.18, depth=0.040, shadow=True)
    bpy.ops.object.light_add(type="AREA", location=(0, -4.5, 5.0))
    light = bpy.context.object
    light.name = "clean softbox"
    light.data.energy = 720
    light.data.size = 7.4
    bpy.context.scene.render.resolution_x = 1920
    bpy.context.scene.render.resolution_y = 1080
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = TOTAL_FRAMES
    if hasattr(bpy.context.scene, "eevee"):
        bpy.context.scene.eevee.taa_render_samples = 96


def cleanup_abnormal_objects():
    markers = ("debug", "stray", "oversized", "huge_triangle", "black_triangle", "orphan", "floating")
    for obj in list(bpy.context.scene.objects):
        lower = obj.name.lower()
        if any(marker in lower for marker in markers):
            bpy.data.objects.remove(obj, do_unlink=True)
            continue
        if obj.type == "MESH" and obj.data and "background" not in lower and "app_shell" not in lower:
            if max(obj.dimensions) > 12.5:
                bpy.data.objects.remove(obj, do_unlink=True)


def build_scene():
    clear_scene()
    RENDER_DIR.mkdir(parents=True, exist_ok=True)
    materials = create_materials()
    setup_world(materials)
    setup_camera()
    left = create_left_panel(materials)
    center = create_center_panel(materials)
    right = create_right_panel(materials)
    timeline = create_timeline(materials)
    animate_scene(left, center, right, timeline)
    cleanup_abnormal_objects()
    bpy.context.scene.frame_set(STILL_PREVIEW_FRAME)


def maybe_render():
    if AUTO_RENDER_STILL:
        bpy.context.scene.frame_set(STILL_PREVIEW_FRAME)
        bpy.context.scene.render.filepath = str(STILL_PATH)
        bpy.ops.render.render(write_still=True)
    if AUTO_RENDER_ANIMATION:
        bpy.context.scene.render.filepath = str(ANIMATION_PATH)
        bpy.context.scene.render.image_settings.file_format = "FFMPEG"
        bpy.context.scene.render.ffmpeg.format = "MPEG4"
        bpy.context.scene.render.ffmpeg.codec = "H264"
        bpy.ops.render.render(animation=True)


def main():
    build_scene()
    maybe_render()


if __name__ == "__main__":
    main()
