# Current Task Goal

Three-keyframe alignment pass for `rubikflow_agent_demo.py`.

Scope:

- Keep the existing stable four-zone layout.
- Align the Blender demo to the uploaded R / LOGIC, F / CLAY, and D / LOCK keyframe mockups.
- Preserve RubikFlow Agent logic and the smart cube digital twin.
- Fix floating output objects, overlap, cramped state indicators, and unclear step progression.
- Avoid copying external UI assets, code, or exact design.

# Files Read First

- `memorize.md`
- `docs/REFERENCE_PROJECTS.md`

# Implemented This Round

- Kept the display around four clear zones:
  - left: Smart Cube Input
  - middle: Workflow-o-pedia / Roll Board
  - right: Agent + Output
  - bottom: Workflow Timeline
- Preserved required controls:
  - `AUTO_RENDER_STILL = False`
  - `AUTO_RENDER_ANIMATION = False`
  - `STILL_PREVIEW_FRAME = 205`
  - `MOVES = ["U", "F", "R", "F", "D", "B"]`
- Preserved core logic:
  - 27 cubelets
  - U/F/R/F/D/B layer turns
  - `MOVE_CONFIG`
  - `FACE_COLORS`
  - two independent `F` steps
  - independent arrow traces
  - 20 Workflow-o-pedia tiles
  - Agent Function Pipeline
  - Output Preview
  - Workflow Timeline

# Visual Polish

- Kept the palette toward the reference images:
  - warm milk background
  - white/cream cards
  - soft borders
  - muted black text
  - restrained blue, green, purple, orange, yellow, red-orange, and teal accents
- Reintroduced the main subtitle:
  `cube move -> workflow tile -> agent output`
- Changed cube face color direction so U is green, F is blue, R is red, and D is yellow.
- Added completed-state green checks to the left move bar and bottom Timeline.
- Added per-stage active highlights:
  - LOGIC red
  - CLAY orange
  - LOCK yellow
- Added simple color-coded icon marks to all 20 Workflow-o-pedia tiles.
- Added icon marks to the bottom Timeline pills.
- Reworked Output Preview into a contained workflow visualization window.

# Keyframe Alignment

R / LOGIC:

- Current move R.
- Active Face shows `R FACE` and `Right Face Active`.
- Workflow-o-pedia highlights JOINT.
- Agent State shows ACTIVE / LOGIC / NETWORK / 45%.
- Output Preview shows gray base blocks, redstone-like signal lines, trigger nodes, and lamps.
- Timeline shows SELECT and BLOCK completed, LOGIC active.

F / CLAY:

- Current move F.
- Active Face shows `F FACE` and `Front Face Active`.
- Workflow-o-pedia highlights CLAY.
- Agent State shows ACTIVE / CLAY / SHELL / 68%.
- Output Preview keeps base + logic and adds orange clay / voxel shell.
- Timeline shows SELECT, BLOCK, and LOGIC completed, CLAY active.

D / LOCK:

- Current move D.
- Active Face shows `D FACE` and `Down Face Active`.
- Workflow-o-pedia highlights LOCK.
- Agent State shows ACTIVE / LOCK / SHELL / 84%.
- Output Preview keeps clay shell and adds lock / security nodes plus LOCKED status.
- Timeline shows SELECT, BLOCK, LOGIC, and CLAY completed, LOCK active.

# Layout Fixes

- Left zone now stacks:
  - Smart Cube Input title
  - U/F/R/F/D/B step bar
  - Active Face On Top
  - 3D smart cube
  - Cube Command Lens
  - PHYSICAL MOVE -> AGENT COMMAND
- Middle zone now contains:
  - RubikFlow Agent title
  - Workflow-o-pedia title
  - 20 larger tiles
  - Triggered Tile / Agent Command / Result summary card
- Right zone now contains:
  - Creation Score / Combo / Printability metric cards
  - Agent State with 4 rows
  - six large pipeline capsules:
    `INPUT / BLOCK / LOGIC / CLAY / LOCK / PRINT`
  - enlarged Output Preview
- Bottom Timeline now uses six larger capsules:
  `SELECT / BLOCK / LOGIC / CLAY / LOCK / PRINT`

# Z-Order Fix

The scene now uses explicit layer order:

- background lowest
- panels above background
- tiles above panels
- highlights behind text
- output and arrow geometry below text
- text closest to camera

This prevents active fills, color cards, arrows, and output preview geometry from covering labels.

# Output Preview Fix

Output Preview was enlarged and separated from the Timeline.

It clearly shows:

- Empty work area / Select Module
- Gray base blocks
- Redstone-like Logic Nodes / Signal Lines
- Orange Clay / Voxel Shell
- Yellow lock / security nodes
- LOCKED confirmation state
- Print Bed
- Slicing Lines
- STL READY
- PRINT READY

# Validation

Passed:

```text
python -m py_compile rubikflow_agent_demo.py
```
