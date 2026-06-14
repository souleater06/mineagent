# RubikFlow Agent Blender Demo

This project is a Blender Python demo for RubikFlow Agent: a physical smart Rubik's Cube controls a Roll-inspired Blender workflow interface.

The script is:

```text
D:\codex-blender\rubikflow-agent\rubikflow_agent_demo.py
```

It uses `bpy`, clears the current Blender scene, and builds a complete visible demo scene. Rendering is off by default.

## Stable Visible Layout

The current version is rebuilt as a stable 16:9 orthographic product view. When the script runs and the Blender camera view is opened, the full system should be visible at once:

- Left: `Smart Cube Input Zone`
- Right / center: `Roll-inspired Main Workflow Stage`
- Bottom: `Workflow Timeline`
- Right lower area: `Output / 3D Print Preview`

The main UI panels, titles, 20 workflow tiles, status panel, output card, and timeline are present from frame 1. Animation uses moving highlights and output scaling instead of hiding the whole interface.

## Smart Cube Input Zone

The cube is not part of the Roll-style UI. It is a digital twin of the physical smart cube input device.

It includes:

- A clearly visible 3x3 cube.
- Title: `Smart Cube Input`.
- `Detected Move`.
- `Mapped Action`.
- A turn arrow and active face glow.
- A signal arrow pointing toward the workflow stage.

## Main Workflow Stage

The main stage is a clean App-like interface inspired by Roll's visual language:

- Warm light background.
- Milk-white rounded cards.
- Black text and simple icon-like navigation.
- Pale blue / pale violet active highlights.
- A 5 x 4 `Workflow-o-pedia` grid.
- Status panel.
- Output preview panel.
- Bottom pill-style workflow timeline.

## Workflow Tiles

The 20 visible tiles are:

```text
+BLOCK, CLAY, VOXEL, JOINT, MIRROR,
SCALE, COLOR, SCAN, AGENT, PRINT,
EXPORT, SHELL, HOLLOW, STACK, LOCK,
LOOP, CHECK, FIX, BUILD, SAVE
```

## Move Mapping

The animation sequence remains:

```python
MOVES = ["U", "F", "R", "F", "D", "B"]
```

| Move | Detected / mapped action | Tile highlight | Timeline highlight | Output change |
| --- | --- | --- | --- | --- |
| U | Select Module | AGENT | SELECT MODULE | Input mapping begins |
| F | Generate Block | +BLOCK | GENERATE BLOCK | Base block appears |
| R | Upgrade Structure | JOINT | UPGRADE STRUCTURE | Supports and connectors appear |
| F | Add Clay / Voxel Shell | CLAY | ADD CLAY | Translucent shell appears |
| D | Confirm Node | LOCK | CONFIRM | LOCKED label appears |
| B | Prepare Print | PRINT | PREPARE PRINT | Print bed and slice lines appear |

## Render Settings

Required switches are kept at the top:

```python
AUTO_RENDER_STILL = False
AUTO_RENDER_ANIMATION = False
STILL_PREVIEW_FRAME = 205
```

Still render output:

```text
D:\codex-blender\rubikflow-agent\renders\rubikflow_agent_still.png
```

Animation output:

```text
D:\codex-blender\rubikflow-agent\renders\rubikflow_agent_demo.mp4
```

The still preview frame is set near the final print-prep state, so `AUTO_RENDER_STILL=True` produces a product-demo-style image with the complete workflow visible.

## Future Integration

The fixed `MOVES` list can be replaced by real smart cube events from Bluetooth, serial, WebSocket, or local event files. Those events can drive the same mapping layer:

```text
physical cube move -> detected move -> mapped action -> workflow highlight -> generated output update
```

The placeholder output geometry can later be replaced by real Blender generation modules, printability checks, slicer previews, exports, and Agent decisions.
