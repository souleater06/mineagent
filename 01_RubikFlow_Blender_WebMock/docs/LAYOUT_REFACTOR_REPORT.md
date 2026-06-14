# RubikFlow Agent Layout Refactor Report

## 1. Problem Diagnosis

This pass focused on layout stability and visual bug fixing, not on adding new features.

Observed / high-risk issues:

- Text and highlights could share too-close depth values, creating a risk that active fills or icon blocks cover labels.
- Workflow-o-pedia icons and tile labels needed a stricter icon/text depth separation.
- Timeline completed badges and active highlights needed clearer z-order separation from text.
- Motion arrow heads were previously text glyphs. In Blender front orthographic view, text-based arrow glyphs can produce large filled shapes or confusing helper geometry when viewed from certain angles.
- A huge black triangle appeared in Blender Front Orthographic. Based on its shape and viewport behavior, it was most likely the orthographic camera helper/frustum display or a helper-style viewport object, not a RubikFlow UI component.
- Stray helper object cleanup was too narrow and did not include all requested names such as `debug_plane`, `oversized_arrow`, `floating_block`, and `orphan_object`.

## 2. Modified Files

- `rubikflow_agent_demo.py`
- `docs/LAYOUT_REFACTOR_REPORT.md`

No other project directory was modified.

## 3. Layout System

The scene keeps the four-zone product interface:

| Zone | Purpose | Current Structure |
| --- | --- | --- |
| Left | Smart Cube Input | Title, U/F/R/F/D/B move bar, Active Face On Top, 3D smart cube, Cube Command Lens, command mapping button |
| Center | Workflow-o-pedia / Roll Board | RubikFlow Agent title, subtitle, 20 workflow tiles, Triggered Tile / Agent Command / Result card |
| Right | Agent + Output | Score, Combo, Printability, Agent State, Agent Function Pipeline, Output Preview |
| Bottom | Workflow Timeline | SELECT -> BLOCK -> LOGIC -> CLAY -> LOCK -> PRINT |

Added layout constants:

- `VIEW_WIDTH`
- `VIEW_HEIGHT`
- `SAFE_MARGIN`
- `LEFT_ZONE`
- `CENTER_ZONE`
- `RIGHT_ZONE`
- `TIMELINE_ZONE`
- `OUTPUT_BOUNDS`
- `CUBE_ARROW_BOUNDS`

These constants make the layout intent explicit and provide fixed boundaries for future adjustments.

## 4. Z-Order Rules

The script now uses this strict depth order:

| Layer | Constant | Purpose |
| --- | --- | --- |
| Background | `Z_BACKGROUND` | Scene background |
| Panel | `Z_PANEL` | Large app shells and cards |
| Tile | `Z_TILE` | Tile/card surfaces |
| Highlight | `Z_HIGHLIGHT` | Active fills and completed-state backgrounds |
| Output | `Z_OUTPUT` | Output Preview geometry |
| Arrow | `Z_ARROW` | Motion arrows and signal lines |
| Icon | `Z_ICON` | Tile icon backgrounds, timeline icons, check badges |
| Text | `Z_TEXT` | All readable labels and values |

Rule:

Text is always closest to camera. Highlights and icon backgrounds never share the same depth as text.

## 5. Abnormal Object Cleanup

The cleanup list now includes:

- `huge_triangle`
- `black_triangle`
- `stray_mesh`
- `debug_plane`
- `arrow_debug`
- `oversized_arrow`
- `motion_arrow_wrong_size`
- `oversized_plane`
- `floating_block`
- `orphan_object`
- `triangle_arrow`
- `debug_marker`
- `camera_helper_mesh`

The script removes:

- Objects with those name markers.
- Large one-face triangle mesh objects.
- Unexpected huge mesh objects larger than the UI canvas, excluding the normal background object.

The active orthographic camera remains active for rendering, but its viewport object display is hidden:

- `camera.data.display_size = 0.12`
- `camera.hide_viewport = True`
- `camera.hide_select = True`
- `camera.hide_render = False`

This prevents the huge black camera/frustum helper shape from blocking the front orthographic working view.

## 6. Overlap and Intersection Fixes

Changes made:

- Added `Z_ICON` so tile icon backgrounds and completed check badges sit above highlights but below text.
- Moved Workflow-o-pedia icon backgrounds to `Z_ICON`.
- Moved timeline icons and completed badges to `Z_ICON`.
- Moved Active Face color card to `Z_ICON`, with the face letter still on `Z_TEXT`.
- Replaced text-based cube motion arrow heads with small curve-line arrow heads.
- Clamped motion arrow points to `CUBE_ARROW_BOUNDS`, so arrows remain inside the Smart Cube Input area.
- Kept Output Preview geometry inside the right-side Output Preview card and separated it from the bottom Timeline.

## 7. Keyframe Alignment

Recommended frames:

| Frame | Stage | Expected Visual |
| --- | --- | --- |
| 1 | U / SELECT | Smart Cube Input ready, AGENT tile active, Output Preview empty / ready |
| 71 | R / LOGIC starts | R move begins, LOGIC timeline stage activates |
| 90 | R / LOGIC stable | R FACE, JOINT tile, redstone-like signal lines and logic nodes |
| 106 | F / CLAY starts | second F move begins, CLAY stage activates |
| 125 | F / CLAY stable | F FACE, CLAY tile, orange clay / voxel shell wraps structure |
| 141 | D / LOCK starts | D move begins, LOCK stage activates |
| 160 | D / LOCK stable | D FACE, LOCK tile, security nodes and LOCKED state |
| 205 | Final preview | Good still render frame with final print-ready context |

## 8. Blender Preview Method

Use this workflow:

1. Open Blender.
2. Run `rubikflow_agent_demo.py`.
3. Press numpad `0` for the active orthographic camera view, or use Front Orthographic for a direct UI drafting view.
4. Check frames:
   - `1`
   - `90`
   - `125`
   - `160`
   - `205`
5. Confirm that:
   - No huge black triangle appears.
   - Smart Cube Input is readable.
   - Workflow-o-pedia has all 20 tiles.
   - Agent State, Pipeline, and Output Preview do not overlap.
   - Workflow Timeline does not collide with the main UI.

## 9. Limitations

- This pass does not implement real smart cube hardware input.
- Output Preview remains a first-stage Blender visualization, not a real Geometry Nodes / slicer pipeline.
- The layout is stable for the current 1920 x 1080 orthographic composition, but future HTML/WebGL conversion should use a real responsive layout system.
- The cube remains a 3D digital twin, while the UI is intentionally mostly flat.

## 10. Second Pass Fixes

This second pass kept the current four-zone layout and focused only on targeted readability and containment fixes.

### 10.1 Text Enlargements

- Enlarged the Smart Cube move chips and completed check badges.
- Simplified Cube Command Lens from five dense debug-style rows to four readable rows:
  - `Move`
  - `Face`
  - `Command`
  - `Output`
- Enlarged Cube Command Lens values and the bottom physical-move mapping button text.
- Enlarged Workflow-o-pedia tile icons and labels.
- Enlarged Triggered Tile / Agent Command / Result text in the middle info card.
- Enlarged Agent State labels and values.
- Enlarged Agent Function Pipeline chip text.
- Enlarged Output Preview flow command/result labels.
- Enlarged Workflow Timeline title, node labels, icons, and completed check marks.

### 10.2 Stray Object / Left Panel Cleanup

- Removed the separate left-side `Move -> Agent` signal label, long signal line, and text arrow head.
- Kept only a small animated signal pulse inside the bottom `PHYSICAL MOVE -> AGENT COMMAND` button.
- Motion arrows around the cube remain curve-based and are still clamped to `CUBE_ARROW_BOUNDS`.
- This reduces the risk of purple/red/yellow helper marks or arrow heads floating outside the Smart Cube Input card.

### 10.3 Output Preview Enhancements

- `R / LOGIC`: strengthened the red signal path, enlarged logic nodes, lamps, and the `Logic Nodes / Signal Lines` label. The flow chip reads `UPGRADE LOGIC -> ACTIVE`.
- `F / CLAY`: enlarged the orange voxel/clay shell pieces and shell wash so the wrap is more visible. The flow chip reads `ADD CLAY SHELL -> BUILDING`.
- `D / LOCK`: enlarged security nodes and the `LOCKED` badge. The flow chip reads `CONFIRM LOCK -> LOCKED`.
- The Output Preview visual elements remain inside the right-side output card and above the bottom timeline boundary.

### 10.4 Recommended Frames

| Frame | Stage | What To Check |
| --- | --- | --- |
| 90 | R / LOGIC | Red signal lines, logic nodes, JOINT tile, LOGIC timeline highlight |
| 125 | F / CLAY | Orange clay / voxel shell, CLAY tile, CLAY timeline highlight |
| 160 | D / LOCK | Lock nodes, LOCKED badge, LOCK tile, LOCK timeline highlight |
| 205 | Final still preview | Full product UI with final print-ready context |

### 10.5 Validation

`python -m py_compile rubikflow_agent_demo.py` passed after this second pass.

## 11. Third Pass: Simplified Readable UI

This pass follows the rule: fewer labels, larger readable states, and no overlap. It does not replace the current four-zone layout.

### 11.1 Removed / Shortened Text

- Cube Command Lens remains four rows only:
  - `Move`
  - `Face`
  - `Command`
  - `Output`
- Removed dense command details such as `Type`, `Direction`, `Layer`, and `Notation`.
- Shortened left command output values:
  - `LOGIC NETWORK`
  - `CLAY SHELL`
  - `LOCKED MODEL`
  - `PRINT READY`
- Rebuilt the middle info strip into three clean columns:
  - `Triggered Tile`
  - `Agent Command`
  - `Result`
- Removed long explanations from the middle info strip. Each column now has one label and one short value.
- Agent State now keeps only:
  - `Status`
  - `Mode`
  - `Progress`
- Removed `Object` from the camera-facing Agent State card.
- Removed extra labels inside Output Preview such as model notes, print-bed notes, and decorative workflow arrows.

### 11.2 Left-Side Stray Color Cleanup

- Disabled the visible cube face glow block and replaced it with a hidden empty object so animation hooks remain intact without adding stray color panels.
- Disabled the visible bottom signal pulse and replaced it with a hidden empty object.
- Reduced cube motion arrow radius and stroke width.
- Motion arrow heads are smaller curve heads and remain clamped to `CUBE_ARROW_BOUNDS`.
- Active Face On Top remains inside the small face card, with the color block reduced and contained.

### 11.3 Simplified Info Strip

The Triggered Tile / Agent Command / Result strip is now a horizontal three-column layout instead of a dense multi-row label/value list.

Example for LOGIC:

| Triggered Tile | Agent Command | Result |
| --- | --- | --- |
| `JOINT` | `UPGRADE LOGIC` | `ACTIVE` |

This removes the previous overlap risk caused by long values sharing one narrow text column.

### 11.4 Larger Output Preview

Output Preview is simplified into two visual lanes:

| Lane | Purpose |
| --- | --- |
| Left 70% | Visual model: grey base, red signal nodes, orange shell, yellow lock nodes, print bed |
| Right 30% | Current command and result only |

Stage-specific output:

| Stage | Visual Model | Right Status |
| --- | --- | --- |
| `R / LOGIC` | grey base, red signal lines, red nodes | `UPGRADE LOGIC` / `ACTIVE` |
| `F / CLAY` | grey base, orange shell | `ADD CLAY` / `BUILDING` |
| `D / LOCK` | orange shell, yellow lock icons | `CONFIRM LOCK` / `LOCKED` |
| `B / PRINT` | print bed, slicing lines, print-ready badge | `PREPARE PRINT` / `PRINT READY` |

The print bed and slicing lines were narrowed so they stay in the model lane instead of crossing into the right status lane.

### 11.5 1920 x 1080 Readability

- Workflow-o-pedia tile icons and labels were enlarged.
- Tile spacing was increased slightly while keeping the full 5 x 4 board.
- Active tile highlight was strengthened but remains below icon/text layers.
- Timeline labels, icons, and completed check badges remain large and single-word only.
- The orthographic camera remains fixed at 1920 x 1080 with the full left / center / right / bottom layout in frame.

### 11.6 Recommended Frames

| Frame | Stage | What To Check |
| --- | --- | --- |
| 1 | U / SELECT | Left panel contained, no stray face glow, AGENT tile active |
| 90 | R / LOGIC | Three-column info strip, LOGIC output with red signal network |
| 125 | F / CLAY | Orange shell inside Output Preview, CLAY active |
| 160 | D / LOCK | Yellow lock nodes and `LOCKED` state |
| 205 | Final still preview | Full UI readability at product-demo framing |

### 11.7 Validation

`python -m py_compile rubikflow_agent_demo.py` passed after this third pass.

## 12. Fourth Pass: Clean Rebuild Demo

This pass creates a separate clean demo script instead of continuing to patch the older crowded UI.

New file:

- `rubikflow_agent_clean_demo.py`

The original `rubikflow_agent_demo.py` is preserved.

### 12.1 Why Create A Clean Demo

The previous script had accumulated many presentation layers, dynamic text groups, arrows, face highlights, and output details across several repair passes. Even after simplification, the Blender viewport could still show:

- small text at 1920 x 1080
- crowded Output Preview elements
- left-side color marks or arrows that were hard to visually police
- a UI that felt like a repaired prototype instead of a clean product draft

The clean demo is a fresh presentation script focused on readability, stable composition, and future HTML / WebGL conversion.

### 12.2 How The New Layout Avoids Overlap

The clean demo defines explicit layout constants:

- `CANVAS_WIDTH`
- `CANVAS_HEIGHT`
- `LEFT_PANEL`
- `CENTER_PANEL`
- `RIGHT_PANEL`
- `TIMELINE_PANEL`
- `GAP`
- `PADDING`

It also defines a strict z-order:

- `Z_BACKGROUND`
- `Z_CARD`
- `Z_TILE`
- `Z_HIGHLIGHT`
- `Z_OUTPUT`
- `Z_ARROW`
- `Z_ICON`
- `Z_TEXT`

Rules:

- Text is always closest to camera.
- Highlights sit below icon and text layers.
- Smart Cube Input, Workflow-o-pedia, Agent + Output, and Timeline are built in fixed zones.
- The left panel uses only one Active Face card, one cube card, one command lens, and one mapping button.
- The middle info strip is a three-column layout, not a dense label/value stack.
- Agent State is reduced to `Status`, `Mode`, and `Progress`.

### 12.3 Output Preview Simplification

The clean Output Preview uses two lanes:

| Lane | Purpose |
| --- | --- |
| Left model lane | visual blocks, logic, clay shell, locks, print bed |
| Right status lane | current command and result only |

Stage visuals:

| Stage | Output Preview |
| --- | --- |
| `R / LOGIC` | grey base blocks, red signal lines, red nodes |
| `F / CLAY` | grey base blocks, orange clay / voxel shell |
| `D / LOCK` | orange shell, yellow lock icons, locked badge |
| `B / PRINT` | print bed, slicing lines, print-ready badge |

No long explanatory text is placed inside the Output Preview.

### 12.4 Recommended Frames

| Frame | Stage | What To Check |
| --- | --- | --- |
| 1 | U / SELECT | Clean four-zone layout, AGENT tile active, ready Output Preview |
| 36 | F / BLOCK | basic grey block appears |
| 90 | R / LOGIC | red signal network and JOINT tile |
| 125 | F / CLAY | orange shell and CLAY tile |
| 160 | D / LOCK | yellow lock icons and LOCKED state |
| 205 | B / PRINT | final print-ready presentation |

### 12.5 Validation

Command:

```text
python -m py_compile rubikflow_agent_clean_demo.py
```

Result:

```text
Passed
```

## 13. Fifth Pass: Fit-to-Canvas Clean Demo

This pass modifies only the clean demo script and keeps the old `rubikflow_agent_demo.py` untouched.

Modified clean file:

- `rubikflow_agent_clean_demo.py`

### 13.1 Main 16:9 App Shell

The clean demo now uses a centered main app shell:

| Constant | Value |
| --- | --- |
| `CANVAS_WIDTH` | `13.35` |
| `CANVAS_HEIGHT` | `7.35` |
| `APP_SHELL` | `13.10 x 7.15` |

The app shell is placed behind all cards as a unified cream product canvas. This is intended to make the Blender view read as one front-end draft rather than detached cards on the grid.

### 13.2 Fit-To-Canvas Panel Ratios

The four zones were re-anchored inside the main shell:

| Zone | Approx Ratio | Script Constant |
| --- | --- | --- |
| Smart Cube Input | 26% | `LEFT_PANEL` |
| RubikFlow Agent / Workflow-o-pedia | 40% | `CENTER_PANEL` |
| Agent + Output | 34% | `RIGHT_PANEL` |
| Workflow Timeline | bottom full-width band | `TIMELINE_PANEL` |

The panel centers and widths were adjusted so the left, center, right, and bottom areas all sit inside the same 16:9 shell with consistent gaps.

### 13.3 Readability Changes

- Increased left title size.
- Enlarged Active Face card, active face color chip, and face text.
- Enlarged cubelets so the smart cube reads as a visible hardware input module.
- Enlarged Cube Command Lens title and rows.
- Enlarged Workflow-o-pedia title, tile icons, and tile labels.
- Enlarged right-side metric cards, Agent State values, and Pipeline chips.
- Kept dynamic text short rather than adding explanatory labels.

### 13.4 Output Preview Enhancement

The right panel was widened and the Output Preview was expanded:

- Output card now uses the wider right column.
- Model lane is wider and larger.
- Status lane remains separate so status buttons do not squeeze the model.
- LOGIC state has larger grey blocks, thicker red signal lines, and larger red nodes.
- CLAY state has a larger orange shell and larger voxel shell pieces.
- LOCK state has larger yellow lock nodes and a stronger `LOCKED` badge.
- PRINT state has a wider print bed, slicing lines, and a clearer `PRINT READY` badge.

### 13.5 Canvas Containment

- `fit_app_shell` is excluded from abnormal-object cleanup.
- The orthographic camera stays fixed to the full canvas height.
- Timeline was moved upward into the app shell instead of sitting near the bottom edge.
- The left cube arrows remain inside the cube display card and do not cross the command lens or title.

### 13.6 Recommended Frames

| Frame | Stage | What To Check |
| --- | --- | --- |
| 1 | U / SELECT | full 16:9 shell, left input module, AGENT tile |
| 36 | F / BLOCK | enlarged grey base block model |
| 90 | R / LOGIC | red signal network, JOINT tile, LOGIC timeline |
| 125 | F / CLAY | orange shell, CLAY tile, BUILDING status |
| 160 | D / LOCK | lock icons, LOCK tile, LOCKED badge |
| 205 | B / PRINT | final print-ready composition inside shell |

### 13.7 Validation

Command:

```text
python -m py_compile rubikflow_agent_clean_demo.py
```

Result:

```text
Passed
```

## 14. Validation

Command:

```text
python -m py_compile rubikflow_agent_demo.py
```

Result:

```text
Passed
```
