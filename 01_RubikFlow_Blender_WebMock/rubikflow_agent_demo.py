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

UI_ROTATION = (math.radians(90), 0, 0)

# Depth layers. The camera looks along world +Y, so smaller Y values are closer.
# The order is intentionally strict:
# background -> panel -> tile -> highlight -> output -> arrow -> icon -> text.
Z_BACKGROUND = 0.34
Z_PANEL = 0.08
Z_TILE = -0.02
Z_HIGHLIGHT = -0.09
Z_OUTPUT = -0.17
Z_ARROW = -0.23
Z_ICON = -0.30
Z_TEXT = -0.38

PANEL_Y = Z_PANEL
SURFACE_Y = Z_TILE
HIGHLIGHT_Y = Z_HIGHLIGHT
TEXT_Y = Z_TEXT
CUBE_Y = -0.52

# Stable orthographic UI layout anchors. The scene is arranged as a flat
# product interface: left input controller, middle Roll board, right Agent/output,
# and a bottom timeline.
LEFT_X = -5.22
CENTER_X = -1.15
RIGHT_X = 4.40
TOP_Z = 2.92
MID_Z = 0.72
BOTTOM_Z = -2.96
Z_SURFACE = SURFACE_Y

VIEW_WIDTH = 13.66
VIEW_HEIGHT = 7.68
SAFE_MARGIN = 0.22
LEFT_ZONE = {
    "x": LEFT_X,
    "width": 3.08,
    "height": 6.78,
    "top": 3.10,
    "bottom": -2.90,
}
CENTER_ZONE = {
    "x": CENTER_X,
    "width": 5.34,
    "height": 6.78,
    "top": 3.10,
    "bottom": -2.34,
}
RIGHT_ZONE = {
    "x": RIGHT_X,
    "width": 3.46,
    "height": 6.78,
    "top": 2.88,
    "bottom": -2.76,
}
TIMELINE_ZONE = {
    "x": 1.28,
    "width": 9.28,
    "height": 0.68,
    "z": -3.28,
}
OUTPUT_BOUNDS = {
    "left": RIGHT_X - 1.43,
    "right": RIGHT_X + 1.36,
    "top": -0.34,
    "bottom": -2.60,
}
CUBE_ARROW_BOUNDS = {
    "left": LEFT_X - 1.22,
    "right": LEFT_X + 1.22,
    "top": 1.35,
    "bottom": -0.34,
}

STRAY_OBJECT_NAME_MARKERS = (
    "huge_triangle",
    "black_triangle",
    "arrow_debug",
    "debug_plane",
    "triangle_arrow",
    "stray_mesh",
    "oversized_arrow",
    "oversized_plane",
    "motion_arrow_wrong_size",
    "floating_block",
    "floating_face",
    "face_marker",
    "stray_panel",
    "debug_face",
    "orphan_object",
    "debug_marker",
    "camera_helper_mesh",
)

MODULES = [
    "+BLOCK", "CLAY", "VOXEL", "JOINT", "MIRROR",
    "SCALE", "COLOR", "SCAN", "AGENT", "PRINT",
    "EXPORT", "SHELL", "HOLLOW", "STACK", "LOCK",
    "LOOP", "CHECK", "FIX", "BUILD", "SAVE",
]

TIMELINE_NODES = [
    "SELECT",
    "BLOCK",
    "LOGIC",
    "CLAY",
    "LOCK",
    "PRINT",
]

MODULE_ACCENTS = {
    "+BLOCK": ("accent_blue", "B"),
    "CLAY": ("accent_orange", "C"),
    "VOXEL": ("accent_teal", "V"),
    "JOINT": ("accent_purple", "J"),
    "MIRROR": ("accent_red", "M"),
    "SCALE": ("accent_green", "S"),
    "COLOR": ("accent_orange", "C"),
    "SCAN": ("accent_teal", "S"),
    "AGENT": ("accent_purple", "A"),
    "PRINT": ("accent_purple", "P"),
    "EXPORT": ("accent_blue", "E"),
    "SHELL": ("accent_teal", "S"),
    "HOLLOW": ("accent_orange", "H"),
    "STACK": ("accent_blue", "S"),
    "LOCK": ("accent_yellow", "L"),
    "LOOP": ("accent_teal", "L"),
    "CHECK": ("accent_green", "C"),
    "FIX": ("accent_red", "F"),
    "BUILD": ("accent_blue", "B"),
    "SAVE": ("accent_blue", "S"),
}

TIMELINE_ACCENTS = {
    "SELECT": ("accent_blue", "S"),
    "BLOCK": ("accent_blue", "B"),
    "LOGIC": ("accent_red", "L"),
    "CLAY": ("accent_orange", "C"),
    "LOCK": ("accent_yellow", "L"),
    "PRINT": ("accent_purple", "P"),
}

STAGE_MATERIALS = {
    "SELECT": "stage_select",
    "BLOCK": "stage_block",
    "LOGIC": "stage_logic",
    "CLAY": "stage_clay",
    "LOCK": "stage_lock",
    "PRINT": "stage_print",
}

ACTION_DATA = [
    {
        "move": "U",
        "action": "Select Module",
        "module": "AGENT",
        "triggered": "AGENT / SCAN",
        "timeline": "SELECT",
        "state": "Module palette active",
        "material": "Smart input",
        "printability": "WAIT",
        "score": "1600",
        "combo": "x1",
        "stage": "READY",
        "chain": "INPUT SELECT",
        "agent_function": "Select workflow module",
        "result": "Ready",
        "status": "READY",
        "mode": "IDLE",
        "object": "NONE",
        "progress": "0%",
        "progress_value": 0.00,
    },
    {
        "move": "F",
        "action": "Generate Block",
        "module": "+BLOCK",
        "triggered": "+BLOCK",
        "timeline": "BLOCK",
        "state": "Base block generated",
        "material": "Block",
        "printability": "PROTO",
        "score": "2500",
        "combo": "x2",
        "stage": "BLOCK",
        "chain": "BLOCK CHAIN",
        "agent_function": "Generate base block",
        "result": "Basic Block",
        "status": "ACTIVE",
        "mode": "BLOCK",
        "object": "BASE",
        "progress": "24%",
        "progress_value": 0.24,
    },
    {
        "move": "R",
        "action": "Upgrade Structure",
        "module": "JOINT",
        "triggered": "JOINT / STACK / LOOP",
        "timeline": "LOGIC",
        "state": "Supports and joints added",
        "material": "Joint / stack",
        "printability": "PROTO",
        "score": "3600",
        "combo": "x3",
        "stage": "UPGRADE",
        "chain": "REDSTONE-LIKE LOGIC",
        "agent_function": "Add connectors and logic nodes",
        "result": "ACTIVE",
        "status": "ACTIVE",
        "mode": "LOGIC",
        "object": "NETWORK",
        "progress": "45%",
        "progress_value": 0.45,
    },
    {
        "move": "F",
        "action": "Add Clay / Voxel Shell",
        "module": "CLAY",
        "triggered": "CLAY / VOXEL",
        "timeline": "CLAY",
        "state": "Clay voxel shell added",
        "material": "Block + clay",
        "printability": "PROTO",
        "score": "5200",
        "combo": "x4",
        "stage": "SHELL",
        "chain": "CLAY / VOXEL CHAIN",
        "agent_function": "Add soft shell or voxel layer",
        "result": "BUILDING",
        "status": "ACTIVE",
        "mode": "CLAY",
        "object": "SHELL",
        "progress": "68%",
        "progress_value": 0.68,
    },
    {
        "move": "D",
        "action": "Confirm Node",
        "module": "LOCK",
        "triggered": "LOCK",
        "timeline": "LOCK",
        "state": "Node confirmed and locked",
        "material": "Locked",
        "printability": "STABLE",
        "score": "6800",
        "combo": "x5",
        "stage": "LOCKED",
        "chain": "CONFIRM",
        "agent_function": "Lock current node",
        "result": "LOCKED",
        "status": "ACTIVE",
        "mode": "LOCK",
        "object": "SHELL",
        "progress": "84%",
        "progress_value": 0.84,
    },
    {
        "move": "B",
        "action": "Prepare Print",
        "module": "PRINT",
        "triggered": "PRINT / EXPORT",
        "timeline": "PRINT",
        "state": "Slicer preview ready",
        "material": "Print prep",
        "printability": "READY",
        "score": "7600",
        "combo": "x6",
        "stage": "PRINT READY",
        "chain": "PRINT CHAIN",
        "agent_function": "Prepare STL and print",
        "result": "Print Ready",
        "status": "ACTIVE",
        "mode": "PRINT",
        "object": "STL",
        "progress": "100%",
        "progress_value": 1.00,
    },
]

FACE_COLORS = {
    "U": "cube_green",
    "D": "cube_yellow",
    "F": "cube_blue",
    "B": "cube_white",
    "R": "cube_red",
    "L": "cube_orange",
}

MOVE_CONFIG = {
    "U": {
        "face_name": "Up Face",
        "layer_axis": "z",
        "layer_value": 1,
        "rotation_axis": "z",
        "rotation_degrees": 90,
        "arrow_center": (LEFT_X, Z_ARROW, 1.10),
        "arrow_radius": (0.62, 0.22),
        "arrow_start": 205,
        "arrow_span": 250,
        "face_color": FACE_COLORS["U"],
    },
    "D": {
        "face_name": "Down Face",
        "layer_axis": "z",
        "layer_value": -1,
        "rotation_axis": "z",
        "rotation_degrees": -90,
        "arrow_center": (LEFT_X, Z_ARROW, -0.10),
        "arrow_radius": (0.62, 0.22),
        "arrow_start": 25,
        "arrow_span": -250,
        "face_color": FACE_COLORS["D"],
    },
    "F": {
        "face_name": "Front Face",
        "layer_axis": "y",
        "layer_value": -1,
        "rotation_axis": "y",
        "rotation_degrees": -90,
        "arrow_center": (LEFT_X, Z_ARROW, 0.55),
        "arrow_radius": (0.72, 0.50),
        "arrow_start": 215,
        "arrow_span": -260,
        "face_color": FACE_COLORS["F"],
    },
    "B": {
        "face_name": "Back Face",
        "layer_axis": "y",
        "layer_value": 1,
        "rotation_axis": "y",
        "rotation_degrees": 90,
        "arrow_center": (LEFT_X, Z_ARROW, 0.55),
        "arrow_radius": (0.66, 0.46),
        "arrow_start": 35,
        "arrow_span": 260,
        "face_color": FACE_COLORS["B"],
    },
    "R": {
        "face_name": "Right Face",
        "layer_axis": "x",
        "layer_value": 1,
        "rotation_axis": "x",
        "rotation_degrees": -90,
        "arrow_center": (LEFT_X + 0.74, Z_ARROW, 0.55),
        "arrow_radius": (0.26, 0.58),
        "arrow_start": 105,
        "arrow_span": -250,
        "face_color": FACE_COLORS["R"],
    },
    "L": {
        "face_name": "Left Face",
        "layer_axis": "x",
        "layer_value": -1,
        "rotation_axis": "x",
        "rotation_degrees": 90,
        "arrow_center": (LEFT_X - 0.74, Z_ARROW, 0.55),
        "arrow_radius": (0.26, 0.58),
        "arrow_start": 285,
        "arrow_span": 250,
        "face_color": FACE_COLORS["L"],
    },
}


def clear_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()
    for datablocks in (
        bpy.data.meshes,
        bpy.data.curves,
        bpy.data.materials,
        bpy.data.lights,
        bpy.data.cameras,
    ):
        for item in list(datablocks):
            if item.users == 0:
                datablocks.remove(item)


def create_materials():
    def mat(name, color, alpha=1.0, emission=None, strength=0.0):
        material = bpy.data.materials.new(name)
        material.diffuse_color = color
        material.use_nodes = True
        bsdf = material.node_tree.nodes.get("Principled BSDF")
        if bsdf:
            if "Base Color" in bsdf.inputs:
                bsdf.inputs["Base Color"].default_value = color
            if "Alpha" in bsdf.inputs:
                bsdf.inputs["Alpha"].default_value = alpha
            if "Roughness" in bsdf.inputs:
                bsdf.inputs["Roughness"].default_value = 0.88
            if emission and "Emission Color" in bsdf.inputs:
                bsdf.inputs["Emission Color"].default_value = emission
            if "Emission Strength" in bsdf.inputs:
                bsdf.inputs["Emission Strength"].default_value = strength
        material.blend_method = "BLEND" if alpha < 1.0 else "OPAQUE"
        material.show_transparent_back = True
        return material

    return {
        "bg": mat("warm milk background", (0.982, 0.972, 0.944, 1)),
        "app": mat("clean milk app shell", (1.000, 0.996, 0.974, 1)),
        "card": mat("crisp cream card", (0.992, 0.982, 0.952, 1)),
        "card_light": mat("bright content card", (1.000, 0.998, 0.984, 1)),
        "blue_card": mat("clear pale blue card", (0.930, 0.970, 1.000, 1)),
        "tile": mat("roll tile warm white", (0.996, 0.988, 0.960, 1)),
        "tile_alt": mat("roll tile cool white", (0.988, 0.994, 0.986, 1)),
        "tile_border": mat("tile soft border", (0.075, 0.064, 0.050, 0.18), alpha=0.18),
        "ink": mat("ink black", (0.010, 0.010, 0.012, 1)),
        "muted": mat("muted ink", (0.300, 0.300, 0.280, 1)),
        "shadow": mat("soft app shadow", (0.10, 0.08, 0.06, 0.11), alpha=0.11),
        "blue": mat(
            "active clear blue",
            (0.58, 0.78, 1.00, 0.76),
            alpha=0.76,
            emission=(0.38, 0.66, 1.00, 1),
            strength=0.28,
        ),
        "violet": mat(
            "active soft lavender",
            (0.78, 0.68, 1.00, 0.74),
            alpha=0.74,
            emission=(0.54, 0.42, 1.00, 1),
            strength=0.26,
        ),
        "stage_select": mat("stage select blue wash", (0.74, 0.88, 1.00, 0.56), alpha=0.56),
        "stage_block": mat("stage block green wash", (0.76, 0.92, 0.72, 0.54), alpha=0.54),
        "stage_logic": mat("stage logic red wash", (1.00, 0.72, 0.64, 0.58), alpha=0.58),
        "stage_clay": mat("stage clay orange wash", (1.00, 0.78, 0.52, 0.58), alpha=0.58),
        "stage_lock": mat("stage lock yellow wash", (1.00, 0.88, 0.48, 0.58), alpha=0.58),
        "stage_print": mat("stage print purple wash", (0.86, 0.76, 1.00, 0.56), alpha=0.56),
        "complete_fill": mat("completed step green wash", (0.80, 0.94, 0.76, 0.50), alpha=0.50),
        "complete_badge": mat("completed check green", (0.18, 0.64, 0.22, 1)),
        "signal": mat(
            "signal blue",
            (0.22, 0.58, 1.00, 1),
            emission=(0.26, 0.64, 1.00, 1),
            strength=0.35,
        ),
        "cube_dark": mat("cube black plastic", (0.018, 0.018, 0.022, 1)),
        "cube_white": mat("cube white", (0.95, 0.95, 0.91, 1)),
        "cube_yellow": mat("cube yellow", (1.00, 0.76, 0.18, 1)),
        "cube_red": mat("cube red", (0.88, 0.22, 0.16, 1)),
        "cube_blue": mat("cube blue", (0.12, 0.36, 0.86, 1)),
        "cube_green": mat("cube green", (0.43, 0.78, 0.42, 1)),
        "cube_orange": mat("cube orange", (0.96, 0.46, 0.10, 1)),
        "block": mat("generated block clear blue", (0.34, 0.66, 1.00, 1)),
        "gray_block": mat("preview gray voxel block", (0.58, 0.60, 0.58, 1)),
        "gray_block_dark": mat("preview gray voxel side", (0.36, 0.38, 0.38, 1)),
        "joint": mat("generated joint lavender", (0.58, 0.42, 0.96, 1)),
        "clay": mat("clay shell visible", (0.96, 0.55, 0.28, 0.58), alpha=0.58),
        "slice": mat("slice lines clean", (0.02, 0.02, 0.02, 0.62), alpha=0.62),
        "logic": mat(
            "redstone like logic signal",
            (0.92, 0.25, 0.18, 1),
            emission=(0.92, 0.20, 0.12, 1),
            strength=0.24,
        ),
        "logic_node": mat("logic trigger node", (1.00, 0.76, 0.18, 1)),
        "ready_green": mat(
            "print ready green",
            (0.56, 0.88, 0.52, 1),
            emission=(0.36, 0.72, 0.34, 1),
            strength=0.18,
        ),
        "accent_blue": mat("ui accent blue", (0.16, 0.44, 0.86, 1)),
        "accent_green": mat("ui accent green", (0.20, 0.62, 0.28, 1)),
        "accent_purple": mat("ui accent purple", (0.36, 0.20, 0.72, 1)),
        "accent_orange": mat("ui accent orange", (0.94, 0.50, 0.16, 1)),
        "accent_yellow": mat("ui accent yellow", (0.96, 0.68, 0.12, 1)),
        "accent_red": mat("ui accent red orange", (0.88, 0.26, 0.20, 1)),
        "accent_teal": mat("ui accent teal", (0.08, 0.58, 0.62, 1)),
        "work_area": mat("output work area lavender wash", (0.74, 0.62, 1.00, 0.12), alpha=0.12),
        "soft_line": mat("soft product line", (0.40, 0.30, 0.82, 0.38), alpha=0.38),
    }


def rounded_rect_points(width, height, radius, segments=8):
    radius = min(radius, width / 2, height / 2)
    x0, x1 = -width / 2, width / 2
    z0, z1 = -height / 2, height / 2
    centers = [
        (x1 - radius, z1 - radius, 0, math.pi / 2),
        (x0 + radius, z1 - radius, math.pi / 2, math.pi),
        (x0 + radius, z0 + radius, math.pi, 3 * math.pi / 2),
        (x1 - radius, z0 + radius, 3 * math.pi / 2, 2 * math.pi),
    ]
    points = []
    for cx, cz, start, end in centers:
        for index in range(segments + 1):
            angle = start + (end - start) * index / segments
            points.append((cx + math.cos(angle) * radius, cz + math.sin(angle) * radius))
    return points


def create_flat_round_rect(name, loc, size, material, radius=0.08):
    width, height = size
    points = rounded_rect_points(width, height, radius)
    verts = [(loc[0] + x, loc[1], loc[2] + z) for x, z in points]
    mesh = bpy.data.meshes.new(f"{name}_mesh")
    mesh.from_pydata(verts, [], [list(range(len(verts)))])
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(material)
    return obj


def create_round_panel(name, loc, size, material, radius=0.08, depth=0.035, shadow=False):
    # UI surfaces are intentionally flat mesh layers, not beveled cubes.
    # The only strongly 3D element in the scene should be the smart cube itself.
    if shadow:
        create_flat_round_rect(
            f"{name}_shadow",
            (loc[0] + 0.055, loc[1] + 0.035, loc[2] - 0.055),
            size,
            bpy.data.materials["soft app shadow"],
            radius=radius,
        )
    return create_flat_round_rect(name, loc, size, material, radius=radius)


def create_text(name, body, loc, size, material, align="CENTER", valign="CENTER"):
    bpy.ops.object.text_add(location=loc, rotation=UI_ROTATION)
    obj = bpy.context.object
    obj.name = name
    obj.data.body = body
    obj.data.align_x = align
    obj.data.align_y = valign
    obj.data.size = size
    obj.data.extrude = 0.001
    obj.data.materials.append(material)
    return obj


def short_action(action):
    return {
        "Select Module": "Select",
        "Generate Block": "Generate Block",
        "Upgrade Structure": "Logic Upgrade",
        "Add Clay / Voxel Shell": "Add Clay",
        "Confirm Node": "Lock Node",
        "Prepare Print": "Prepare Print",
    }.get(action, action)


def short_trigger(triggered):
    return triggered.replace("AGENT / SCAN", "AGENT").replace("JOINT / STACK / LOOP", "JOINT").replace("PRINT / EXPORT", "PRINT")


def stage_material_key(data):
    return STAGE_MATERIALS.get(data["timeline"], "stage_select")


def move_layer_label(move):
    return {
        "U": "TOP",
        "F": "FRONT",
        "R": "RIGHT",
        "D": "DOWN",
        "B": "BACK",
        "L": "LEFT",
    }.get(move, move)


def command_label(data):
    return {
        "Select Module": "SELECT MODULE",
        "Generate Block": "GENERATE BLOCK",
        "Upgrade Structure": "UPGRADE LOGIC",
        "Add Clay / Voxel Shell": "ADD CLAY",
        "Confirm Node": "CONFIRM LOCK",
        "Prepare Print": "PREPARE PRINT",
    }.get(data["action"], data["action"].upper())


def bottom_mapping_label(data):
    return f"FACE TURN ({move_layer_label(data['move'])}) -> {command_label(data)}"


def lens_output_label(data):
    return {
        "Select Module": "READY",
        "Generate Block": "BASIC BLOCK",
        "Upgrade Structure": "LOGIC NETWORK",
        "Add Clay / Voxel Shell": "CLAY SHELL",
        "Confirm Node": "LOCKED MODEL",
        "Prepare Print": "PRINT READY",
    }.get(data["action"], data["result"].upper())


def flow_result_label(data):
    return {
        "Select Module": "READY",
        "Generate Block": "BLOCK",
        "Upgrade Structure": "ACTIVE",
        "Add Clay / Voxel Shell": "BUILDING",
        "Confirm Node": "LOCKED",
        "Prepare Print": "PRINT READY",
    }.get(data["action"], data["result"].upper())


def output_command_label(data):
    return {
        "Select Module": "SELECT",
        "Generate Block": "BLOCK",
        "Upgrade Structure": "UPGRADE\nLOGIC",
        "Add Clay / Voxel Shell": "ADD CLAY",
        "Confirm Node": "CONFIRM\nLOCK",
        "Prepare Print": "PREPARE\nPRINT",
    }.get(data["action"], command_label(data))


def clamp(value, lower, upper):
    return max(lower, min(upper, value))


def clamp_point_to_bounds(point, bounds):
    return (
        clamp(point[0], bounds["left"], bounds["right"]),
        point[1],
        clamp(point[2], bounds["bottom"], bounds["top"]),
    )


def create_curve_line(name, points, material, width=0.012):
    curve = bpy.data.curves.new(name, type="CURVE")
    curve.dimensions = "3D"
    curve.resolution_u = 3
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


def create_curve_arrow_head(name, tip, angle, material, size=0.11, spread=0.70):
    left_angle = angle + math.pi - spread
    right_angle = angle + math.pi + spread
    left_tail = (tip[0] + math.cos(left_angle) * size, tip[1], tip[2] + math.sin(left_angle) * size)
    right_tail = (tip[0] + math.cos(right_angle) * size, tip[1], tip[2] + math.sin(right_angle) * size)
    return [
        create_curve_line(f"{name}_a", [tip, left_tail], material, width=0.014),
        create_curve_line(f"{name}_b", [tip, right_tail], material, width=0.014),
    ]


def store_final_scale(obj):
    obj["final_scale_x"] = obj.scale.x
    obj["final_scale_y"] = obj.scale.y
    obj["final_scale_z"] = obj.scale.z
    return obj


def set_visibility(obj, frame, visible):
    obj.hide_viewport = not visible
    obj.hide_render = not visible
    obj.keyframe_insert(data_path="hide_viewport", frame=frame)
    obj.keyframe_insert(data_path="hide_render", frame=frame)


def set_group_visibility(objects, frame, visible):
    for obj in objects:
        set_visibility(obj, frame, visible)


def remove_stray_helper_objects():
    for obj in list(bpy.context.scene.objects):
        lower_name = obj.name.lower()
        should_remove = any(marker in lower_name for marker in STRAY_OBJECT_NAME_MARKERS)
        if not should_remove and obj.type == "MESH" and obj.data:
            vertex_count = len(obj.data.vertices)
            polygon_count = len(obj.data.polygons)
            max_dimension = max(obj.dimensions) if obj.dimensions else 0
            is_large_triangle = vertex_count <= 3 and polygon_count <= 1 and max_dimension > 1.2
            is_unexpected_huge_mesh = max_dimension > 12.0 and "background" not in lower_name
            should_remove = is_large_triangle or is_unexpected_huge_mesh
        if should_remove:
            bpy.data.objects.remove(obj, do_unlink=True)


def parent_local(child, parent, local_location):
    child.parent = parent
    child.location = local_location
    return child


def create_cube_sticker(name, local_location, scale, material, parent):
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0))
    sticker = bpy.context.object
    sticker.name = name
    sticker.scale = scale
    sticker.data.materials.append(material)
    bevel = sticker.modifiers.new(name="sticker bevel", type="BEVEL")
    bevel.width = 0.007
    bevel.segments = 2
    sticker.modifiers.new(name="sticker normals", type="WEIGHTED_NORMAL")
    parent_local(sticker, parent, local_location)
    return sticker


def create_smart_cube(materials):
    create_round_panel(
        "input_zone_shell",
        (LEFT_X, Z_PANEL, 0.0),
        (3.08, 6.78),
        materials["app"],
        radius=0.17,
        depth=0.050,
        shadow=True,
    )
    create_text("input_title", "Smart Cube Input", (LEFT_X, Z_TEXT, 3.10), 0.170, materials["ink"])

    create_round_panel("input_cube_card", (LEFT_X, Z_SURFACE, 0.52), (2.56, 1.78), materials["card_light"], radius=0.14)
    create_round_panel("device_pedestal", (LEFT_X, Z_HIGHLIGHT, -0.27), (1.88, 0.22), materials["cube_dark"], radius=0.06, depth=0.065)

    cube_root = bpy.data.objects.new("Smart Cube Digital Twin", None)
    bpy.context.collection.objects.link(cube_root)
    cube_root.location = (LEFT_X, CUBE_Y, 0.58)
    cube_root.rotation_euler = (math.radians(-18), math.radians(28), math.radians(-10))

    face_materials = {
        "U": materials["cube_green"],
        "D": materials["cube_yellow"],
        "R": materials["cube_red"],
        "L": materials["cube_orange"],
        "F": materials["cube_blue"],
        "B": materials["cube_white"],
    }
    spacing = 0.425
    cubelet_size = 0.365
    sticker_span = 0.275
    sticker_thickness = 0.012
    cubelets = []

    # Smart cube local axes for the digital twin:
    # x = Right / Left layer, y = Back / Front layer, z = Up / Down layer.
    # U selects z == 1, D selects z == -1, F selects y == -1, B selects y == 1,
    # R selects x == 1, and L selects x == -1.
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            for z in [-1, 0, 1]:
                loc = (x * spacing, y * spacing, z * spacing)
                bpy.ops.mesh.primitive_cube_add(size=cubelet_size, location=(0, 0, 0))
                cubelet = bpy.context.object
                cubelet.name = f"cubelet_{x}_{y}_{z}"
                cubelet.data.materials.append(materials["cube_dark"])
                bevel = cubelet.modifiers.new(name="cubelet bevel", type="BEVEL")
                bevel.width = 0.017
                bevel.segments = 3
                cubelet.modifiers.new(name="cubelet normals", type="WEIGHTED_NORMAL")
                parent_local(cubelet, cube_root, loc)
                cubelet["cube_coord_x"] = x
                cubelet["cube_coord_y"] = y
                cubelet["cube_coord_z"] = z
                cubelet["home_x"] = loc[0]
                cubelet["home_y"] = loc[1]
                cubelet["home_z"] = loc[2]
                cubelets.append(cubelet)
                if z == 1:
                    create_cube_sticker(f"U_sticker_{x}_{y}_{z}", (0, 0, cubelet_size / 2 + sticker_thickness), (sticker_span / 2, sticker_span / 2, sticker_thickness), face_materials["U"], cubelet)
                if z == -1:
                    create_cube_sticker(f"D_sticker_{x}_{y}_{z}", (0, 0, -cubelet_size / 2 - sticker_thickness), (sticker_span / 2, sticker_span / 2, sticker_thickness), face_materials["D"], cubelet)
                if x == 1:
                    create_cube_sticker(f"R_sticker_{x}_{y}_{z}", (cubelet_size / 2 + sticker_thickness, 0, 0), (sticker_thickness, sticker_span / 2, sticker_span / 2), face_materials["R"], cubelet)
                if x == -1:
                    create_cube_sticker(f"L_sticker_{x}_{y}_{z}", (-cubelet_size / 2 - sticker_thickness, 0, 0), (sticker_thickness, sticker_span / 2, sticker_span / 2), face_materials["L"], cubelet)
                if y == -1:
                    create_cube_sticker(f"F_sticker_{x}_{y}_{z}", (0, -cubelet_size / 2 - sticker_thickness, 0), (sticker_span / 2, sticker_thickness, sticker_span / 2), face_materials["F"], cubelet)
                if y == 1:
                    create_cube_sticker(f"B_sticker_{x}_{y}_{z}", (0, cubelet_size / 2 + sticker_thickness, 0), (sticker_span / 2, sticker_thickness, sticker_span / 2), face_materials["B"], cubelet)

    face_glow = bpy.data.objects.new("cube_face_glow_disabled", None)
    bpy.context.collection.objects.link(face_glow)
    face_glow.empty_display_size = 0.0
    face_glow.hide_viewport = True
    face_glow.hide_render = True
    turn_arrows = create_motion_arrow_traces(materials)
    move_sequence_bar = create_move_sequence_bar(materials)

    current_move_groups = []
    face_preview_groups = []
    for index, data in enumerate(ACTION_DATA):
        config = MOVE_CONFIG[data["move"]]
        face_material = materials[config["face_color"]]

        preview_group = [
            create_round_panel(f"active_face_preview_shell_{index}", (LEFT_X, Z_TILE, 1.88), (2.46, 0.72), materials["card"], radius=0.12, depth=0.018),
            create_round_panel(f"active_face_preview_color_{index}", (LEFT_X - 0.78, Z_ICON, 1.86), (0.62, 0.48), face_material, radius=0.08, depth=0.018),
            create_text(f"active_face_preview_move_{index}", data["move"], (LEFT_X - 0.78, Z_TEXT, 1.86), 0.150, materials["ink"]),
            create_text(f"active_face_preview_title_{index}", "Active Face On Top", (LEFT_X - 1.12, Z_TEXT, 2.12), 0.060, materials["muted"], align="LEFT"),
            create_text(f"active_face_preview_face_{index}", f"{data['move']} FACE", (LEFT_X - 0.28, Z_TEXT, 1.94), 0.128, materials["ink"], align="LEFT"),
            create_text(f"active_face_preview_command_{index}", f"{move_layer_label(data['move'])}", (LEFT_X - 0.28, Z_TEXT, 1.69), 0.074, materials["muted"], align="LEFT"),
        ]
        face_preview_groups.append(preview_group)

    input_status_groups = []
    create_round_panel("command_lens_card", (LEFT_X, Z_SURFACE, -1.48), (2.58, 1.18), materials["blue_card"], radius=0.13)
    create_text("command_lens_title", "Cube Command Lens", (LEFT_X - 1.18, Z_TEXT, -1.02), 0.064, materials["ink"], align="LEFT")
    command_lens_groups = []
    for index, data in enumerate(ACTION_DATA):
        group = [
            create_text(f"lens_move_{index}", f"Move:     {data['move']}", (LEFT_X - 1.16, Z_TEXT, -1.24), 0.060, materials["ink"], align="LEFT"),
            create_text(f"lens_face_{index}", f"Face:     {move_layer_label(data['move'])}", (LEFT_X - 1.16, Z_TEXT, -1.48), 0.060, materials["ink"], align="LEFT"),
            create_text(f"lens_command_{index}", f"Command:  {command_label(data)}", (LEFT_X - 1.16, Z_TEXT, -1.72), 0.052, materials["ink"], align="LEFT"),
            create_text(f"lens_output_{index}", f"Output:   {lens_output_label(data)}", (LEFT_X - 1.16, Z_TEXT, -1.96), 0.060, materials["ink"], align="LEFT"),
        ]
        command_lens_groups.append(group)

    create_round_panel("input_signal_chip", (LEFT_X, Z_HIGHLIGHT, -2.72), (2.56, 0.46), materials["blue"], radius=0.12, depth=0.020)
    input_mapping_groups = []
    for index, data in enumerate(ACTION_DATA):
        input_mapping_groups.append([
            create_text(f"input_signal_chip_text_{index}", bottom_mapping_label(data), (LEFT_X, Z_TEXT, -2.72), 0.058, materials["ink"])
        ])

    return {
        "root": cube_root,
        "cubelets": cubelets,
        "face_glow": face_glow,
        "turn_arrows": turn_arrows,
        "move_sequence_bar": move_sequence_bar,
        "current_move_groups": current_move_groups,
        "face_preview_groups": face_preview_groups,
        "command_lens_groups": command_lens_groups,
        "input_status_groups": input_status_groups,
        "input_mapping_groups": input_mapping_groups,
    }


def create_move_sequence_bar(materials):
    create_round_panel("move_sequence_bar_shell", (LEFT_X, Z_TILE, 2.60), (2.74, 0.54), materials["card"], radius=0.10)
    positions = []
    active_groups = []
    complete_groups = []
    start_x = LEFT_X - 1.10
    for index, move in enumerate(MOVES):
        x = start_x + index * 0.44
        loc = (x, Z_TILE - 0.014, 2.60)
        data = ACTION_DATA[index]
        create_round_panel(f"move_sequence_chip_{index}_{move}", loc, (0.40, 0.40), materials["card_light"], radius=0.095)
        active_groups.append([
            create_round_panel(
                f"move_sequence_active_{index}_{move}",
                (x, Z_HIGHLIGHT, 2.60),
                (0.48, 0.48),
                materials[stage_material_key(data)],
                radius=0.105,
                depth=0.018,
            )
        ])
        complete_groups.append([
            create_round_panel(f"move_sequence_done_fill_{index}_{move}", (x, Z_HIGHLIGHT - 0.006, 2.60), (0.43, 0.43), materials["complete_fill"], radius=0.100, depth=0.012),
            create_round_panel(f"move_sequence_done_badge_{index}_{move}", (x + 0.15, Z_ICON, 2.46), (0.16, 0.16), materials["complete_badge"], radius=0.050, depth=0.010),
            create_text(f"move_sequence_done_check_{index}_{move}", "v", (x + 0.15, Z_TEXT - 0.004, 2.46), 0.066, materials["card_light"]),
        ])
        create_text(f"move_sequence_text_{index}_{move}", move, (x, Z_TEXT, 2.60), 0.142, materials["ink"])
        positions.append((x, Z_HIGHLIGHT, 2.60))
    return {"positions": positions, "active_groups": active_groups, "complete_groups": complete_groups}


def create_motion_arrow_traces(materials):
    arrow_groups = []
    for step_index, data in enumerate(ACTION_DATA):
        move = data["move"]
        config = MOVE_CONFIG[move]
        center_x, center_y, center_z = config["arrow_center"]
        if move == "F":
            center_x += -0.08 if step_index == 1 else 0.08
            center_z += 0.04 if step_index == 1 else -0.04
        radius_x, radius_z = (config["arrow_radius"][0] * 0.74, config["arrow_radius"][1] * 0.74)
        material = materials[config["face_color"]]
        segments = []
        segment_count = 5
        for segment_index in range(segment_count):
            segment_points = []
            start_angle = config["arrow_start"] + config["arrow_span"] * segment_index / segment_count
            end_angle = config["arrow_start"] + config["arrow_span"] * (segment_index + 0.78) / segment_count
            for point_index in range(9):
                angle = math.radians(start_angle + (end_angle - start_angle) * point_index / 8)
                segment_points.append(
                    clamp_point_to_bounds(
                        (center_x + math.cos(angle) * radius_x, center_y, center_z + math.sin(angle) * radius_z),
                        CUBE_ARROW_BOUNDS,
                    )
                )
            segment = create_curve_line(f"turn_arrow_step_{step_index}_{move}_{segment_index}", segment_points, material, width=0.012)
            segments.append(segment)
        head_angle = math.radians(config["arrow_start"] + config["arrow_span"])
        head_tip = clamp_point_to_bounds(
            (center_x + math.cos(head_angle) * radius_x, Z_ARROW, center_z + math.sin(head_angle) * radius_z),
            CUBE_ARROW_BOUNDS,
        )
        head = create_curve_arrow_head(f"turn_arrow_head_step_{step_index}_{move}", head_tip, head_angle, material, size=0.08)
        arrow_groups.append(segments + head)
    return arrow_groups


def create_main_workflow_stage(materials):
    create_round_panel(
        "main_app_shell",
        (1.28, Z_PANEL + 0.04, 0.00),
        (9.70, 6.78),
        materials["app"],
        radius=0.18,
        depth=0.060,
        shadow=True,
    )
    create_text("main_title", "RubikFlow Agent", (CENTER_X - 2.34, Z_TEXT, 3.08), 0.245, materials["ink"], align="LEFT")
    create_text(
        "main_subtitle",
        "cube move -> workflow tile -> agent output",
        (CENTER_X - 2.34, Z_TEXT, 2.80),
        0.076,
        materials["muted"],
        align="LEFT",
    )


def create_metric_cards(materials):
    metric_specs = [
        ("Score", "score", RIGHT_X - 1.08, "0120"),
        ("Combo", "combo", RIGHT_X, "x1"),
        ("Printability", "printability", RIGHT_X + 1.08, "WAIT"),
    ]
    groups = {"score": [], "combo": [], "printability": []}
    for label, key, x, _initial in metric_specs:
        create_round_panel(f"metric_{key}_card", (x, Z_TILE, 2.58), (0.98, 0.56), materials["blue_card"], radius=0.10)
        create_text(f"metric_{key}_label", label.upper(), (x, Z_TEXT, 2.76), 0.046 if key == "printability" else 0.052, materials["muted"])
        for idx, data in enumerate(ACTION_DATA):
            value = data["score"] if key == "score" else data[key]
            obj = create_text(f"metric_{key}_{idx}", value, (x, Z_TEXT, 2.48), 0.124 if key != "printability" else 0.086, materials["ink"])
            groups[key].append(obj)
    return groups


def create_icon_tile(name, label, loc, size, materials):
    material = materials["tile_alt"] if MODULES.index(label) % 2 else materials["tile"]
    tile = create_round_panel(name, loc, size, material, radius=0.075, depth=0.030)
    create_round_panel(f"{name}_border", (loc[0], Z_PANEL - 0.004, loc[2]), (size[0] + 0.040, size[1] + 0.040), materials["tile_border"], radius=0.085)
    accent_name, glyph = MODULE_ACCENTS.get(label, ("accent_blue", label[:1]))
    create_round_panel(f"{name}_icon_bg", (loc[0], Z_ICON, loc[2] + 0.105), (0.300, 0.225), materials[accent_name], radius=0.058, depth=0.018)
    create_text(f"{name}_icon", glyph, (loc[0], Z_TEXT, loc[2] + 0.104), 0.110, materials["card_light"])
    create_text(f"{name}_label", label, (loc[0], Z_TEXT, loc[2] - 0.135), 0.074 if len(label) > 5 else 0.086, materials["ink"])
    return {"tile": tile, "position": loc}


def create_mapping_strip(materials):
    create_round_panel("roll_mapping_strip", (-1.22, SURFACE_Y - 0.006, 1.78), (3.76, 0.50), materials["blue_card"], radius=0.10)
    create_text("roll_mapping_title", "Roll -> RubikFlow Mapping", (-3.02, TEXT_Y, 1.96), 0.060, materials["muted"], align="LEFT")
    pairs = [
        ("DICE", "CUBE"),
        ("RESULT", "MOVE"),
        ("BONUS", "NODE"),
        ("SCORE", "SCORE"),
        ("SHOP", "UPGRADE"),
        ("BANK", "ASSETS"),
    ]
    start_x = -2.95
    for idx, (roll, flow) in enumerate(pairs):
        x = start_x + idx * 0.61
        create_round_panel(f"mapping_chip_{idx}", (x, SURFACE_Y - 0.020, 1.66), (0.52, 0.22), materials["tile"], radius=0.055)
        create_text(f"mapping_chip_text_{idx}", f"{roll}>{flow}", (x, TEXT_Y, 1.66), 0.035, materials["ink"])


def create_workflow_opedia(materials):
    create_round_panel("opedia_area", (CENTER_X, Z_TILE, 0.68), (5.02, 4.42), materials["card_light"], radius=0.14)
    create_text("opedia_title", "Workflow-o-pedia", (CENTER_X - 2.28, Z_TEXT, 2.46), 0.154, materials["ink"], align="LEFT")

    tiles = {}
    start_x = CENTER_X - 1.92
    start_z = 1.70
    gap_x = 0.98
    gap_z = 0.64
    for idx, label in enumerate(MODULES):
        col = idx % 5
        row = idx // 5
        loc = (start_x + col * gap_x, Z_TILE - 0.010, start_z - row * gap_z)
        tiles[label] = create_icon_tile(f"workflow_tile_{label.replace('+', 'plus').lower()}", label, loc, (0.82, 0.48), materials)

    active_groups = []
    for index, data in enumerate(ACTION_DATA):
        target = tiles[data["module"]]["position"]
        active_groups.append([
            create_round_panel(
                f"active_tile_highlight_{index}_{data['module'].replace('+', 'plus').lower()}",
                (target[0], Z_HIGHLIGHT, target[2]),
                (1.02, 0.66),
                materials[stage_material_key(data)],
                radius=0.095,
                depth=0.018,
            )
        ])
    return {"tiles": tiles, "active_groups": active_groups}


def create_trigger_info_panel(materials):
    create_round_panel("trigger_info_area", (CENTER_X, Z_TILE, -1.42), (4.70, 0.78), materials["blue_card"], radius=0.12)
    columns = [
        ("Triggered Tile", CENTER_X - 1.55),
        ("Agent Command", CENTER_X),
        ("Result", CENTER_X + 1.55),
    ]
    for col, (label, x) in enumerate(columns):
        create_text(f"trigger_info_label_{col}", label, (x, Z_TEXT, -1.24), 0.058, materials["muted"])

    groups = []
    for idx, data in enumerate(ACTION_DATA):
        values = [data["module"], command_label(data), flow_result_label(data)]
        group = []
        for col, value in enumerate(values):
            x = columns[col][1]
            group.append(create_text(f"trigger_info_value_{idx}_{col}", value, (x, Z_TEXT, -1.58), 0.082, materials["ink"]))
        groups.append(group)
    return groups


def create_status_panel(materials):
    create_round_panel("status_area", (RIGHT_X, Z_TILE, 1.66), (3.30, 0.92), materials["blue_card"], radius=0.13)
    create_text("status_title", "Agent State", (RIGHT_X - 1.46, Z_TEXT, 2.03), 0.098, materials["ink"], align="LEFT")

    labels = ["Status", "Mode", "Progress"]
    for idx, label in enumerate(labels):
        z = 1.80 - idx * 0.24
        create_text(f"status_label_{idx}", label, (RIGHT_X - 1.42, Z_TEXT, z), 0.066, materials["muted"], align="LEFT")

    groups = []
    for idx, data in enumerate(ACTION_DATA):
        values = [data["status"], data["mode"], data["progress"]]
        group = []
        for row, value in enumerate(values):
            z = 1.80 - row * 0.24
            group.append(create_text(f"status_value_{idx}_{row}", value, (RIGHT_X - 0.46, Z_TEXT, z), 0.076, materials["ink"], align="LEFT"))
        group.append(create_round_panel(f"status_progress_track_{idx}", (RIGHT_X + 0.62, Z_HIGHLIGHT, 1.32), (1.04, 0.070), materials["tile_border"], radius=0.032, depth=0.010))
        progress_width = max(0.04, 1.04 * data["progress_value"])
        progress_x = RIGHT_X + 0.10 + progress_width / 2
        group.append(create_round_panel(f"status_progress_fill_{idx}", (progress_x, Z_ARROW, 1.32), (progress_width, 0.070), materials["signal"], radius=0.032, depth=0.010))
        groups.append(group)
    return groups


def create_function_pipeline(materials):
    create_round_panel("function_pipeline_area", (RIGHT_X, Z_TILE, 0.60), (3.30, 0.88), materials["card"], radius=0.12)
    create_text("function_pipeline_title", "Agent Function Pipeline", (RIGHT_X - 1.46, Z_TEXT, 0.96), 0.072, materials["ink"], align="LEFT")
    chain_specs = [
        ("INPUT", "INPUT SELECT", RIGHT_X - 0.98, 0.68),
        ("BLOCK", "BLOCK CHAIN", RIGHT_X, 0.68),
        ("LOGIC", "REDSTONE-LIKE LOGIC", RIGHT_X + 0.98, 0.68),
        ("CLAY", "CLAY / VOXEL CHAIN", RIGHT_X - 0.98, 0.36),
        ("LOCK", "CONFIRM", RIGHT_X, 0.36),
        ("PRINT", "PRINT CHAIN", RIGHT_X + 0.98, 0.36),
    ]
    positions = {}
    chain_order = []
    complete_groups = []
    for idx, (label, chain, x, z) in enumerate(chain_specs):
        create_round_panel(f"pipeline_chip_{idx}", (x, Z_TILE - 0.010, z), (0.88, 0.26), materials["tile_alt"], radius=0.085)
        complete_groups.append([
            create_round_panel(f"pipeline_done_{idx}", (x, Z_HIGHLIGHT, z), (0.94, 0.32), materials["complete_fill"], radius=0.095, depth=0.014)
        ])
        create_text(f"pipeline_chip_text_{idx}", label, (x, Z_TEXT, z), 0.064, materials["ink"])
        positions[chain] = (x, Z_HIGHLIGHT, z)
        chain_order.append(chain)
    active_groups = []
    for index, data in enumerate(ACTION_DATA):
        x, _y, z = positions[data["chain"]]
        active_groups.append([
            create_round_panel(
                f"active_pipeline_highlight_{index}",
                (x, Z_HIGHLIGHT - 0.006, z),
                (0.98, 0.36),
                materials[stage_material_key(data)],
                radius=0.100,
                depth=0.018,
            )
        ])
    return {"positions": positions, "active_groups": active_groups, "complete_groups": complete_groups, "chain_order": chain_order, "groups": []}


def create_output_area(materials):
    create_round_panel("output_area", (RIGHT_X, Z_TILE, -1.36), (3.30, 2.78), materials["card_light"], radius=0.13)
    create_text("output_title", "Output Preview", (RIGHT_X - 1.46, Z_TEXT, -0.10), 0.116, materials["ink"], align="LEFT")
    create_round_panel("output_work_area_panel", (RIGHT_X - 0.58, Z_TILE - 0.020, -1.38), (2.02, 1.52), materials["work_area"], radius=0.11)
    create_round_panel("output_status_panel", (RIGHT_X + 1.04, Z_TILE - 0.018, -1.38), (0.96, 1.52), materials["blue_card"], radius=0.11)
    create_round_panel("output_flow_agent_chip", (RIGHT_X + 1.04, Z_HIGHLIGHT, -1.12), (0.88, 0.40), materials["violet"], radius=0.090, depth=0.014)
    create_round_panel("output_flow_ready_chip", (RIGHT_X + 1.04, Z_HIGHLIGHT, -1.70), (0.88, 0.38), materials["blue"], radius=0.090, depth=0.014)
    create_round_panel("output_floor", (RIGHT_X - 0.58, Z_TILE - 0.015, -2.28), (2.02, 0.18), materials["tile_alt"], radius=0.045)
    ready_card = create_round_panel("output_ready_card", (RIGHT_X - 0.58, Z_TILE - 0.006, -1.38), (1.88, 1.36), materials["work_area"], radius=0.10)
    ready_text = create_text("output_ready_text", "SELECT MODULE", (RIGHT_X - 0.52, Z_TEXT, -1.36), 0.074, materials["muted"])

    stages = {"ready": [ready_card, ready_text], "basic_block": [], "upgrade": [], "clay": [], "confirm": [], "print": [], "flow_groups": []}
    for index, data in enumerate(ACTION_DATA):
        stages["flow_groups"].append([
            create_text(f"output_flow_command_{index}", output_command_label(data), (RIGHT_X + 1.04, Z_TEXT, -1.12), 0.046, materials["ink"]),
            create_text(f"output_flow_result_{index}", flow_result_label(data), (RIGHT_X + 1.04, Z_TEXT, -1.70), 0.064, materials["ink"]),
        ])

    grid_origin_x = RIGHT_X - 1.10
    grid_origin_z = -1.82
    cell = 0.30
    for row in range(4):
        for col in range(5):
            x = grid_origin_x + col * cell
            z = grid_origin_z + row * cell * 0.76
            stages["basic_block"].append(create_round_panel(f"output_base_tile_{row}_{col}", (x, Z_OUTPUT, z), (0.28, 0.22), materials["gray_block"], radius=0.030, depth=0.045))
    for loc in [(RIGHT_X - 0.50, -1.16), (RIGHT_X - 0.20, -1.16), (RIGHT_X - 0.50, -1.42), (RIGHT_X - 0.20, -1.42)]:
        stages["basic_block"].append(create_round_panel(f"output_center_block_{len(stages['basic_block'])}", (loc[0], Z_OUTPUT - 0.018, loc[1]), (0.29, 0.23), materials["gray_block_dark"], radius=0.032, depth=0.070))

    logic_points = [
        (RIGHT_X - 1.02, Z_OUTPUT - 0.055, -1.70),
        (RIGHT_X - 0.74, Z_OUTPUT - 0.055, -1.52),
        (RIGHT_X - 0.46, Z_OUTPUT - 0.055, -1.70),
        (RIGHT_X - 0.16, Z_OUTPUT - 0.055, -1.38),
        (RIGHT_X + 0.18, Z_OUTPUT - 0.055, -1.54),
    ]
    stages["upgrade"].append(create_curve_line("logic_signal_path", logic_points, materials["logic"], width=0.020))
    stages["upgrade"].append(create_curve_line("logic_signal_branch", [(RIGHT_X - 0.74, Z_OUTPUT - 0.060, -1.52), (RIGHT_X - 0.80, Z_OUTPUT - 0.060, -1.04), (RIGHT_X - 0.26, Z_OUTPUT - 0.060, -0.94)], materials["logic"], width=0.018))
    for idx, loc in enumerate([(RIGHT_X - 1.02, -1.70), (RIGHT_X - 0.74, -1.52), (RIGHT_X - 0.16, -1.38), (RIGHT_X + 0.18, -1.54), (RIGHT_X - 0.26, -0.94)]):
        stages["upgrade"].append(create_round_panel(f"logic_trigger_node_{idx}", (loc[0], Z_OUTPUT - 0.070, loc[1]), (0.18, 0.18), materials["logic_node"], radius=0.050, depth=0.035))
    for idx, loc in enumerate([(RIGHT_X - 0.26, -0.80), (RIGHT_X + 0.10, -1.10)]):
        stages["upgrade"].append(create_round_panel(f"logic_lamp_{idx}", (loc[0], Z_OUTPUT - 0.075, loc[1]), (0.22, 0.25), materials["logic_node"], radius=0.050, depth=0.045))
        stages["upgrade"].append(create_text(f"logic_lamp_mark_{idx}", "!", (loc[0], Z_TEXT, loc[1]), 0.074, materials["logic"]))

    shell_positions = [
        (RIGHT_X - 0.98, -0.94), (RIGHT_X - 0.70, -0.82), (RIGHT_X - 0.42, -0.82), (RIGHT_X - 0.14, -0.94),
        (RIGHT_X - 1.02, -1.22), (RIGHT_X - 0.10, -1.22), (RIGHT_X - 1.02, -1.50), (RIGHT_X - 0.10, -1.50),
        (RIGHT_X - 0.98, -1.78), (RIGHT_X - 0.70, -1.90), (RIGHT_X - 0.42, -1.90), (RIGHT_X - 0.14, -1.78),
    ]
    for idx, loc in enumerate(shell_positions):
        stages["clay"].append(create_round_panel(f"voxel_shell_voxel_{idx}", (loc[0], Z_OUTPUT - 0.095, loc[1]), (0.25, 0.20), materials["accent_orange"], radius=0.040, depth=0.045))
    stages["clay"].append(create_round_panel("output_clay_shell_wash", (RIGHT_X - 0.56, Z_OUTPUT - 0.110, -1.38), (1.36, 1.12), materials["clay"], radius=0.14, depth=0.035))

    lock_positions = [(RIGHT_X - 0.98, -1.08), (RIGHT_X - 0.72, -0.88), (RIGHT_X - 0.20, -0.88), (RIGHT_X - 0.16, -1.70), (RIGHT_X - 0.74, -1.78)]
    for idx, loc in enumerate(lock_positions):
        stages["confirm"].append(create_round_panel(f"security_node_{idx}", (loc[0], Z_OUTPUT - 0.125, loc[1]), (0.22, 0.22), materials["accent_yellow"], radius=0.065, depth=0.040))
        stages["confirm"].append(create_text(f"security_node_lock_{idx}", "L", (loc[0], Z_TEXT, loc[1]), 0.074, materials["ink"]))
    stages["confirm"].append(create_round_panel("output_locked_badge", (RIGHT_X - 0.32, Z_OUTPUT - 0.130, -2.08), (0.98, 0.34), materials["stage_lock"], radius=0.09, depth=0.026))
    stages["confirm"].append(create_text("output_locked_text", "LOCKED", (RIGHT_X - 0.32, Z_TEXT, -2.08), 0.080, materials["ink"]))

    stages["print"].append(create_round_panel("print_bed", (RIGHT_X - 0.58, Z_OUTPUT, -2.38), (1.90, 0.24), materials["ink"], radius=0.05, depth=0.08))
    for idx in range(8):
        stages["print"].append(create_round_panel(f"slice_line_{idx}", (RIGHT_X - 0.58, Z_OUTPUT - 0.050, -2.04 + idx * 0.14), (1.72, 0.018), materials["slice"], radius=0.006, depth=0.010))
    stages["print"].append(create_round_panel("print_ready_badge", (RIGHT_X - 0.58, Z_OUTPUT - 0.030, -0.58), (1.20, 0.32), materials["ready_green"], radius=0.08, depth=0.018))
    stages["print"].append(create_text("print_ready_label", "PRINT READY", (RIGHT_X - 0.58, Z_TEXT, -0.58), 0.070, materials["ink"]))

    for stage_name, group in stages.items():
        if stage_name in ("ready", "flow_groups"):
            continue
        for obj in group:
            store_final_scale(obj)
            obj.scale = (0.001, 0.001, 0.001)
            obj.keyframe_insert(data_path="scale", frame=1)
    return stages


def create_timeline(materials):
    create_round_panel("timeline_area", (1.28, Z_TILE, -3.28), (9.28, 0.68), materials["card"], radius=0.16)
    create_text("timeline_label", "Workflow Timeline", (-3.28, Z_TEXT, -3.28), 0.090, materials["ink"], align="LEFT")
    nodes = {}
    complete_groups = []
    active_groups = []
    start_x = -2.06
    gap = 1.40
    for idx, label in enumerate(TIMELINE_NODES):
        x = start_x + idx * gap
        loc = (x, Z_TILE - 0.010, -3.28)
        accent_name, glyph = TIMELINE_ACCENTS[label]
        create_round_panel(f"timeline_node_border_{idx}", (x, Z_PANEL - 0.004, -3.28), (1.10, 0.48), materials["tile_border"], radius=0.14)
        create_round_panel(f"timeline_node_{idx}", loc, (1.02, 0.42), materials["tile"], radius=0.13)
        complete_groups.append([
            create_round_panel(f"timeline_done_fill_{idx}", (x, Z_HIGHLIGHT, -3.28), (1.10, 0.50), materials["complete_fill"], radius=0.15, depth=0.014),
            create_round_panel(f"timeline_done_badge_{idx}", (x + 0.42, Z_ICON, -3.42), (0.17, 0.17), materials["complete_badge"], radius=0.055, depth=0.010),
            create_text(f"timeline_done_check_{idx}", "v", (x + 0.42, Z_TEXT - 0.004, -3.42), 0.068, materials["card_light"]),
        ])
        stage_key = STAGE_MATERIALS[label]
        active_groups.append([
            create_round_panel(f"timeline_active_{idx}_{label.lower()}", (x, Z_HIGHLIGHT - 0.006, -3.28), (1.20, 0.56), materials[stage_key], radius=0.16, depth=0.018)
        ])
        create_round_panel(f"timeline_icon_{idx}", (x - 0.32, Z_ICON, -3.28), (0.20, 0.20), materials[accent_name], radius=0.050, depth=0.014)
        create_text(f"timeline_icon_text_{idx}", glyph, (x - 0.32, Z_TEXT, -3.28), 0.068, materials["card_light"])
        create_text(f"timeline_text_{idx}", label, (x + 0.12, Z_TEXT, -3.28), 0.072, materials["ink"])
        nodes[label] = {"position": loc}
        if idx < len(TIMELINE_NODES) - 1:
            create_text(f"timeline_arrow_{idx}", ">", (x + gap / 2, Z_TEXT, -3.28), 0.086, materials["muted"])
    return {"nodes": nodes, "active_groups": active_groups, "complete_groups": complete_groups}


def create_input_to_workflow_signal(materials):
    pulse = bpy.data.objects.new("signal_pulse_disabled", None)
    bpy.context.collection.objects.link(pulse)
    pulse.empty_display_size = 0.0
    pulse.hide_viewport = True
    pulse.hide_render = True
    return {"pulse": pulse}


def rotate_vector_quarter_turn(vector, axis, direction):
    x, y, z = vector.x, vector.y, vector.z
    if axis == "x":
        return Vector((x, -direction * z, direction * y))
    if axis == "y":
        return Vector((direction * z, y, -direction * x))
    return Vector((-direction * y, direction * x, z))


def select_cube_layer(cubelets, move):
    config = MOVE_CONFIG[move]
    coord_axis = config["layer_axis"]
    coord_value = config["layer_value"]
    coord_key = f"cube_coord_{coord_axis}"
    selected = [cubelet for cubelet in cubelets if int(cubelet[coord_key]) == coord_value]
    return selected, config["rotation_axis"], config["rotation_degrees"]


def animate_cube_layer_turn(cube_data, move, start_frame, end_frame):
    selected, turn_axis, rotation_degrees = select_cube_layer(cube_data["cubelets"], move)
    mid_frame = start_frame + max(8, (end_frame - start_frame) // 2)
    turn_direction = 1 if rotation_degrees > 0 else -1
    angle = math.radians(rotation_degrees)
    rotation_delta = {"x": (angle, 0, 0), "y": (0, angle, 0), "z": (0, 0, angle)}[turn_axis]

    for cubelet in selected:
        home_location = Vector((cubelet["home_x"], cubelet["home_y"], cubelet["home_z"]))
        cubelet.location = home_location
        cubelet.rotation_euler = (0, 0, 0)
        cubelet.keyframe_insert(data_path="location", frame=start_frame)
        cubelet.keyframe_insert(data_path="rotation_euler", frame=start_frame)

        cubelet.location = rotate_vector_quarter_turn(home_location, turn_axis, turn_direction)
        cubelet.rotation_euler = rotation_delta
        cubelet.keyframe_insert(data_path="location", frame=mid_frame)
        cubelet.keyframe_insert(data_path="rotation_euler", frame=mid_frame)

        # Return to a tidy solved-grid state after the visual layer turn.
        # This keeps the first-stage demo stable while still showing true 9-cubelet face motion.
        cubelet.location = home_location
        cubelet.rotation_euler = (0, 0, 0)
        cubelet.keyframe_insert(data_path="location", frame=end_frame)
        cubelet.keyframe_insert(data_path="rotation_euler", frame=end_frame)


def animate_move_sequence_bar(cube_data, action_index, start_frame):
    bar = cube_data["move_sequence_bar"]
    for idx, group in enumerate(bar["active_groups"]):
        set_group_visibility(group, start_frame, idx == action_index)
    for idx, group in enumerate(bar["complete_groups"]):
        set_group_visibility(group, start_frame, idx < action_index)


def animate_arrow_trace_for_step(cube_data, action_index, start_frame, end_frame):
    if action_index == 0:
        all_arrow_objects = []
        for arrow_group in cube_data["turn_arrows"]:
            all_arrow_objects.extend(arrow_group)
        set_group_visibility(all_arrow_objects, 1, False)

    arrow_group = cube_data["turn_arrows"][action_index]
    step = max(2, (end_frame - start_frame) // max(1, len(arrow_group)))
    for index, obj in enumerate(arrow_group):
        set_visibility(obj, start_frame + index * step, True)


def animate_cube_move(cube_data, action_index, start_frame, end_frame):
    data = ACTION_DATA[action_index]
    move = data["move"]
    glow_positions = {
        "U": ((LEFT_X, Z_ARROW, 1.12), (1.38, 0.30, 0.22)),
        "D": ((LEFT_X, Z_ARROW, -0.10), (1.38, 0.30, 0.22)),
        "R": ((LEFT_X + 0.73, Z_ARROW, 0.55), (0.32, 0.30, 1.08)),
        "L": ((LEFT_X - 0.73, Z_ARROW, 0.55), (0.32, 0.30, 1.08)),
        "F": ((LEFT_X, Z_ARROW, 0.55), (1.38, 0.30, 1.02)),
        "B": ((LEFT_X, Z_ARROW, 0.55), (1.24, 0.30, 0.92)),
    }
    glow_loc, glow_scale = glow_positions[move]
    face_glow = cube_data["face_glow"]
    face_glow.location = glow_loc
    face_glow.scale = glow_scale
    face_glow.keyframe_insert(data_path="location", frame=start_frame)
    face_glow.keyframe_insert(data_path="scale", frame=start_frame)
    face_glow.scale = (glow_scale[0] * 1.08, glow_scale[1], glow_scale[2] * 1.08)
    face_glow.keyframe_insert(data_path="scale", frame=start_frame + 10)
    face_glow.scale = glow_scale
    face_glow.keyframe_insert(data_path="scale", frame=end_frame)

    animate_cube_layer_turn(cube_data, move, start_frame, end_frame)
    animate_move_sequence_bar(cube_data, action_index, start_frame)
    animate_arrow_trace_for_step(cube_data, action_index, start_frame, end_frame)

    for idx, group in enumerate(cube_data["input_status_groups"]):
        set_group_visibility(group, start_frame, idx == action_index)
    for idx, group in enumerate(cube_data["current_move_groups"]):
        set_group_visibility(group, start_frame, idx == action_index)
    for idx, group in enumerate(cube_data["face_preview_groups"]):
        set_group_visibility(group, start_frame, idx == action_index)
    for idx, group in enumerate(cube_data["command_lens_groups"]):
        set_group_visibility(group, start_frame, idx == action_index)
    for idx, group in enumerate(cube_data["input_mapping_groups"]):
        set_group_visibility(group, start_frame, idx == action_index)


def show_output_stage(objects, frame):
    for obj in objects:
        final_scale = (
            obj.get("final_scale_x", 1.0),
            obj.get("final_scale_y", 1.0),
            obj.get("final_scale_z", 1.0),
        )
        obj.scale = (0.001, 0.001, 0.001)
        obj.keyframe_insert(data_path="scale", frame=max(1, frame - 1))
        obj.scale = final_scale
        obj.keyframe_insert(data_path="scale", frame=frame + 8)


def animate_workflow_state(workflow_data, trigger_groups, status_groups, metric_groups, timeline_data, output_stages, signal_data, pipeline_data):
    pulse = signal_data["pulse"]
    for index, data in enumerate(ACTION_DATA):
        frame = 1 + index * FRAMES_PER_MOVE
        for group_index, group in enumerate(workflow_data["active_groups"]):
            set_group_visibility(group, frame, group_index == index)
        for group_index, group in enumerate(timeline_data["active_groups"]):
            set_group_visibility(group, frame, TIMELINE_NODES[group_index] == data["timeline"])
        for group_index, group in enumerate(timeline_data["complete_groups"]):
            set_group_visibility(group, frame, group_index < index)
        for group_index, group in enumerate(pipeline_data["active_groups"]):
            set_group_visibility(group, frame, group_index == index)
        for group_index, group in enumerate(pipeline_data["complete_groups"]):
            set_group_visibility(group, frame, group_index < index)
        for group_index, group in enumerate(trigger_groups):
            set_group_visibility(group, frame, group_index == index)
        for group_index, group in enumerate(status_groups):
            set_group_visibility(group, frame, group_index == index)
        for group_index, group in enumerate(pipeline_data["groups"]):
            set_group_visibility(group, frame, group_index == index)
        for metric_group in metric_groups.values():
            for metric_index, obj in enumerate(metric_group):
                set_visibility(obj, frame, metric_index == index)
        for flow_index, group in enumerate(output_stages["flow_groups"]):
            set_group_visibility(group, frame, flow_index == index)
        pulse.location = (LEFT_X - 0.96, Z_ICON, -2.72)
        pulse.keyframe_insert(data_path="location", frame=frame)
        pulse.location = (LEFT_X + 0.96, Z_ICON, -2.72)
        pulse.keyframe_insert(data_path="location", frame=frame + 15)
        set_group_visibility(output_stages["ready"], frame, index == 0)
        if data["action"] == "Generate Block":
            show_output_stage(output_stages["basic_block"], frame)
        elif data["action"] == "Upgrade Structure":
            show_output_stage(output_stages["upgrade"], frame)
        elif data["action"] == "Add Clay / Voxel Shell":
            show_output_stage(output_stages["clay"], frame)
        elif data["action"] == "Confirm Node":
            show_output_stage(output_stages["confirm"], frame)
        elif data["action"] == "Prepare Print":
            show_output_stage(output_stages["print"], frame)


def setup_camera():
    bpy.ops.object.camera_add(location=(0, -12.0, 0), rotation=(math.radians(90), 0, 0))
    camera = bpy.context.object
    camera.name = "RubikFlow Orthographic Product Camera"
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 7.70
    camera.data.display_size = 0.12
    camera.hide_select = True
    camera.hide_viewport = True
    camera.hide_render = False
    bpy.context.scene.camera = camera
    return camera


def setup_lighting_and_world(materials):
    world = bpy.context.scene.world or bpy.data.worlds.new("RubikFlow World")
    bpy.context.scene.world = world
    world.color = (0.935, 0.928, 0.890)
    create_round_panel("full_background", (0, Z_BACKGROUND, 0), (14.7, 8.2), materials["bg"], radius=0.02, depth=0.025)
    bpy.ops.object.light_add(type="AREA", location=(0, -4.5, 5.0))
    key = bpy.context.object
    key.name = "large app softbox"
    key.data.energy = 700
    key.data.size = 7.2
    bpy.ops.object.light_add(type="POINT", location=(-5.8, -3.2, 2.3))
    fill = bpy.context.object
    fill.name = "cube input fill"
    fill.data.energy = 95
    bpy.context.scene.render.resolution_x = 1920
    bpy.context.scene.render.resolution_y = 1080
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = TOTAL_FRAMES
    if hasattr(bpy.context.scene, "eevee"):
        bpy.context.scene.eevee.taa_render_samples = 96
        if hasattr(bpy.context.scene.eevee, "use_gtao"):
            bpy.context.scene.eevee.use_gtao = True


def build_scene():
    clear_scene()
    RENDER_DIR.mkdir(parents=True, exist_ok=True)
    materials = create_materials()
    setup_lighting_and_world(materials)
    setup_camera()
    cube_data = create_smart_cube(materials)
    create_main_workflow_stage(materials)
    signal_data = create_input_to_workflow_signal(materials)
    metric_groups = create_metric_cards(materials)
    workflow_data = create_workflow_opedia(materials)
    trigger_groups = create_trigger_info_panel(materials)
    status_groups = create_status_panel(materials)
    pipeline_data = create_function_pipeline(materials)
    output_stages = create_output_area(materials)
    timeline_data = create_timeline(materials)
    for index, _move in enumerate(MOVES):
        start = 1 + index * FRAMES_PER_MOVE
        end = min(TOTAL_FRAMES, start + FRAMES_PER_MOVE - 1)
        animate_cube_move(cube_data, index, start, end)
    animate_workflow_state(workflow_data, trigger_groups, status_groups, metric_groups, timeline_data, output_stages, signal_data, pipeline_data)
    remove_stray_helper_objects()
    bpy.context.scene.frame_set(1)
    return materials


def configure_render_outputs():
    bpy.context.scene.render.image_settings.file_format = "PNG"
    if AUTO_RENDER_STILL:
        bpy.context.scene.frame_set(STILL_PREVIEW_FRAME)
        bpy.context.scene.render.filepath = str(STILL_PATH)
        bpy.ops.render.render(write_still=True)
    if AUTO_RENDER_ANIMATION:
        bpy.context.scene.render.filepath = str(ANIMATION_PATH)
        bpy.context.scene.render.image_settings.file_format = "FFMPEG"
        bpy.context.scene.render.ffmpeg.format = "MPEG4"
        bpy.context.scene.render.ffmpeg.codec = "H264"
        bpy.context.scene.render.ffmpeg.constant_rate_factor = "MEDIUM"
        bpy.context.scene.render.ffmpeg.ffmpeg_preset = "GOOD"
        bpy.context.scene.frame_start = 1
        bpy.context.scene.frame_end = TOTAL_FRAMES
        bpy.ops.render.render(animation=True)


def main():
    build_scene()
    configure_render_outputs()


if __name__ == "__main__":
    main()
