# RubikFlow Agent Reference Projects

This document studies several open-source projects as design references for RubikFlow Agent. It is not a code reuse plan. We should not copy their code, assets, UI, naming, license text, or implementation details. The goal is to extract interaction patterns and reinterpret them into a smart-cube-driven Blender Agent workflow.

Core RubikFlow direction:

Physical smart cube rotation -> Detected Move -> Agent workflow command -> Roll-inspired tile trigger -> Blender output change -> block / clay / voxel / 3D-print preparation.

## 1. Reference Project List

| Project | GitHub URL | Problem It Solves | Value for RubikFlow |
| --- | --- | --- | --- |
| Smart Cube Gaming Controller | https://github.com/ignisco/Smart-Cube-Gaming-Controller | Uses a Bluetooth smart cube as a game controller and maps cube actions to keyboard inputs. | Shows how a physical smart cube can become an input layer. RubikFlow can reinterpret this as cube move -> Agent command instead of cube move -> keyboard key. |
| dice-box | https://github.com/3d-dice/dice-box | Provides a 3D dice rolling system with visual roll feedback and dice results. | Helps define the pattern: physical-looking action -> detected result -> feedback. RubikFlow can transform this into rotate cube face -> detected move -> workflow tile trigger. |
| awesome-blender | https://github.com/agmmnn/awesome-blender | Curates Blender tools, add-ons, workflows, and learning resources. | Useful as a map of Blender ecosystem directions: scripting, procedural modeling, Geometry Nodes, rendering, add-ons, and automation. |
| Procedural 3D Modeling Using Geometry Nodes in Blender, Second Edition | https://github.com/PacktPublishing/Procedural-3D-Modeling-Using-Geometry-Nodes-in-Blender-Second-Edn | Companion repository for learning procedural modeling with Geometry Nodes. | Gives a conceptual path for future Agent-controlled procedural generation: blocks, shells, connectors, modular structures. |
| geometry-script | https://github.com/carson-katri/geometry-script | Offers a Python-oriented way to create Blender geometry node setups. | Suggests a future bridge where Agent commands can generate or alter node graphs programmatically. |
| BVtkNodes | https://github.com/tkeskita/BVtkNodes | Visualizes and executes VTK pipelines inside Blender through node workflows. | Useful reference for pipeline visualization: data enters nodes, nodes transform it, final geometry or output appears. |
| BVtkNodes fork | https://github.com/simboden/BVtkNodes | Fork of BVtkNodes. | Confirms that Blender node-pipeline workflows can be adapted and extended. RubikFlow can design its own simpler Agent Function Pipeline. |
| voxel-builder | https://github.com/nimadez/voxel-builder | Browser-based voxel building / voxel editing direction. | Useful for block-like output preview: voxel blocks, grid logic, buildable structures, and modular visual language. |
| voxel-builder live page | https://nimadez.github.io/voxel-builder/ | Live web demo for voxel-building interaction. | Helps imagine a clearer Output Preview where block / voxel output is shown as editable, buildable modules rather than abstract shapes. |
| voxel2gcode | https://github.com/nonoesp/voxel2gcode | Converts voxel-style forms toward G-code / fabrication-oriented output. | Provides a fabrication direction: voxel model -> slicing / toolpath implication -> print-ready state. RubikFlow can use this as conceptual inspiration for 3D Print Preview. |

## 2. What We Can Learn

### Design Patterns

| Pattern | Source Direction | RubikFlow Interpretation |
| --- | --- | --- |
| Physical object as controller | Smart Cube Gaming Controller | Treat the cube as a real-world input device, not decoration. The Blender cube is a digital twin of user motion. |
| Action -> result -> feedback | dice-box | Each cube face turn should immediately show detected move, mapped command, tile trigger, and output response. |
| Encyclopedia / board of actions | Roll-like interaction direction | Workflow-o-pedia should feel like a grid of unlockable workflow tiles: +BLOCK, CLAY, VOXEL, JOINT, PRINT, etc. |
| Node pipeline | BVtkNodes / Geometry Nodes direction | Agent Function Pipeline should show a clear chain: INPUT -> BLOCK -> LOGIC -> CLAY -> LOCK -> PRINT. |
| Procedural generation | Geometry Nodes resources | Agent commands should eventually drive parametric generation, not only static animation. |
| Voxel / fabrication output | voxel-builder / voxel2gcode | Output Preview should make block, clay shell, voxel structure, slicing lines, and print readiness visually distinct. |

### Interaction Logic

- Smart cube interaction should be treated as hardware input:
  - physical rotation
  - detected move
  - face identity
  - mapped workflow command
  - command history

- Dice / Roll-like interaction should be reinterpreted as workflow triggering:
  - roll result becomes detected cube move
  - dice result feedback becomes Workflow-o-pedia highlight
  - bonus / combo becomes Creation Score and Combo
  - upgrade becomes Agent-generated block / clay / print state

- Blender procedural workflow should be staged as a clear pipeline:
  - cube move selects operation
  - Agent maps operation
  - Blender visualization changes
  - generated output enters block / clay / voxel / print preview

### Visual Expression

- Keep the interface flat, orthographic, and product-like.
- Use large readable zones instead of many small labels.
- Use clear color language:
  - cube face color for Active Face
  - pale blue / lavender for active UI tile
  - green for current step / print ready
  - black text on cream cards for readability
- Use output lanes:
  - Block
  - Logic
  - Clay / Voxel
  - Print

## 3. What We Should Not Copy

- Do not copy external project code.
- Do not copy external assets, icons, screenshots, or UI layouts.
- Do not copy their exact interaction design.
- Do not copy license text into this project as if it applies to RubikFlow.
- Do not use unclear-license implementations as dependencies without review.
- Do not directly clone Roll, dice-box, Geometry Nodes examples, BVtkNodes UI, voxel-builder UI, or voxel2gcode internals.
- Do not make RubikFlow into a keyboard-input demo only. The project direction is cube move -> Agent workflow command.

RubikFlow should be an original reinterpretation:

Smart cube as physical workflow controller, Roll-inspired workflow feedback, Blender as visualization stage, Agent as generation brain, and block / clay / voxel / 3D-print as output directions.

## 4. RubikFlow Derivative Integration Plan

### Smart Cube Input Layer

Goal:

Turn the smart cube into a hardware workflow controller.

Original reference direction:

Smart Cube Gaming Controller maps cube activity to keyboard-style control.

RubikFlow reinterpretation:

Cube move maps to Agent workflow command:

| Move | Agent Command | UI Response |
| --- | --- | --- |
| U | Select Module | Highlight selection tile / AGENT / SCAN |
| F | Generate Block | Highlight +BLOCK and show a base block |
| R | Upgrade Structure | Highlight JOINT / STACK / LOGIC and show connectors |
| Second F | Add Clay / Voxel Shell | Highlight CLAY / VOXEL and show shell |
| D | Confirm Node | Highlight LOCK and show locked state |
| B | Prepare Print | Highlight PRINT / EXPORT and show print bed |

Implementation idea:

- Keep a clean Smart Cube Input Zone.
- Display only the essential command state:
  - Move
  - Face
  - Roll Tile
  - Agent
  - Output
- Show Active Face On Top with a large face-colored card.
- Keep the 3D cube visible and independent from the main UI.

### Roll-inspired Workflow Layer

Goal:

Transform Roll-like feedback into a workflow board.

Original reference direction:

Dice roll produces a result and visual feedback.

RubikFlow reinterpretation:

Cube move triggers a Workflow-o-pedia tile:

Rotate face -> detected move -> active tile -> score / combo / workflow progression.

Design ideas:

- Workflow-o-pedia is a 5 x 4 tile board.
- Tiles should look like clear rounded buttons.
- Active tile should be obvious, but highlight must never cover text.
- Avoid extra text inside the tile board.
- Put Triggered Tile / Agent Command / Result in one separate card below the board.

### Agent Command Layer

Goal:

Make the Agent feel like the brain between physical input and Blender output.

RubikFlow command flow:

Input Move -> Agent Command -> Pipeline Step -> Output Result.

Pipeline:

INPUT -> BLOCK -> LOGIC -> CLAY -> LOCK -> PRINT.

Design ideas:

- Use six compact pipeline chips.
- Highlight one current pipeline chip.
- Avoid long pipeline descriptions in the main render.
- Store detailed command explanations in documentation or future debug mode, not in the presentation view.

### Blender Visualization Layer

Goal:

Make Blender the visual stage, not just a collection of panels.

Procedural inspiration:

Geometry Nodes and geometry-script suggest future directions for Agent-generated geometry graphs.

RubikFlow reinterpretation:

- Current demo: animate simple blocks, shells, joints, slicing lines.
- Future version: Agent selects or modifies procedural node templates.
- Long-term: cube move sequences generate parameter changes:
  - block count
  - shell thickness
  - connector pattern
  - voxel resolution
  - print bed orientation

### Block / Clay / Voxel Output Layer

Goal:

Make the result visually readable as physical creation, not abstract decoration.

Reference direction:

Voxel-builder suggests a block/grid building language.

RubikFlow reinterpretation:

- F creates a basic block.
- R adds joints, supports, or logic signal nodes.
- Second F adds clay / voxel shell.
- D locks the current node.
- B prepares for printing.

Output Preview should have visual categories:

| Category | Visual Cue |
| --- | --- |
| Block | strong cube / modular block |
| Logic | signal line, joint nodes, connector points |
| Clay / Voxel | shell, soft cover, voxel skin |
| Print | platform, slicing lines, PRINT READY |

### 3D Print Preview Layer

Goal:

Show the final workflow state as fabrication-ready.

Reference direction:

Voxel2gcode suggests the larger path from voxel form to fabrication / toolpath output.

RubikFlow reinterpretation:

- Do not implement real G-code in the demo yet.
- Represent print readiness visually:
  - print bed
  - slicing lines
  - STL / export label
  - PRINT READY state
- Future system can connect voxel / mesh output to actual slicing or export pipelines.

## 5. Concrete Improvement Suggestions for `rubikflow_agent_demo.py`

These suggestions are for future code passes. This document does not modify the Blender script.

### Current Issue: Font Overlap

Recommendation:

- Keep the current reduced text strategy.
- Use a strict presentation view and a separate future debug view.
- Remove secondary labels from camera render.
- Use short labels: Move, Tile, Agent, Output.
- Never put dynamic multi-line text in narrow cards.

### Current Issue: Panel Overlap

Recommendation:

- Keep four major zones:
  - left input
  - middle Roll Board
  - right Agent + Output
  - bottom Timeline
- Define and use a layout grid.
- Avoid nested cards except for repeated tiles or tool surfaces.
- Maintain safe margins between Output Preview and Timeline.

### Current Issue: Cube Move Not Intuitive Enough

Recommendation:

- Make Active Face On Top the primary teaching element.
- Use a big face-colored card with:
  - FACE: F
  - COMMAND: Generate Block
- Keep arrows inside the cube zone.
- Use one visible arrow per current action, with old arrows dimmed or removed.

### Current Issue: U/F/R/F/D/B Step Bar Not Clear Enough

Recommendation:

- Use large chips:
  - U
  - F
  - R
  - F
  - D
  - B
- Use green current-step highlight.
- Use separate object names for both F chips.
- Do not add tiny labels below chips in the presentation view.

### Current Issue: Active Face On Top Not Clear Enough

Recommendation:

- Make the face card larger than status labels.
- Use face color as the main visual cue.
- Show only:
  - FACE: F
  - COMMAND: Generate Block
- Avoid long explanations in the face card.

### Current Issue: Output Preview Not Like Real Block / Clay / Logic / Print

Recommendation:

- Separate the output composition into visible lanes:
  - Block object
  - Logic nodes / signal lines
  - Clay / voxel shell
  - Print bed / slicing lines
- Use fewer words and stronger geometry.
- Make final frame 205 clearly show PRINT READY.

### Current Issue: Agent Function Pipeline Not Intuitive

Recommendation:

- Use six chips only:
  - INPUT
  - BLOCK
  - LOGIC
  - CLAY
  - LOCK
  - PRINT
- Highlight current chip.
- Avoid long labels like REDSTONE-LIKE LOGIC inside tiny chips.
- Put longer explanation in README or a separate notes panel.

## 6. Next Development Priorities

### Phase 1: Fix Layout and Readability

- Keep the current four-zone layout.
- Audit all dynamic text positions.
- Keep text big enough for camera render.
- Remove minor captions that compete with core logic.
- Verify frames 1, 60, 120, 180, and 205.

### Phase 2: Strengthen Cube Move Teaching Demo

- Make Active Face On Top more central to the input zone.
- Use face-colored cue cards.
- Keep turn arrows inside the cube area.
- Make each move visually teachable:
  - U selects
  - F generates
  - R upgrades
  - F adds shell
  - D locks
  - B prints

### Phase 3: Strengthen Roll Tile Trigger

- Make Workflow-o-pedia feel like a real action board.
- Make active tile highlight clearer.
- Add a simple tile-trigger pulse between cube input and Roll Board.
- Keep triggered tile info in one clean card below the board.

### Phase 4: Strengthen Output Preview

- Replace abstract shapes with more readable block / joint / shell / print objects.
- Make the output area the largest region on the right.
- Use geometry more than text.
- Final frame should clearly read:
  - generated object
  - slicing lines
  - print platform
  - PRINT READY

### Phase 5: Connect Real Smart Cube Input

- Add a keyboard-input prototype first.
- Then integrate real smart cube data stream.
- Convert sensor state to U/F/R/L/D/B move events.
- Feed move events into the same Agent command mapping used by the demo.

### Phase 6: Connect Geometry Nodes / Voxel / Print Pipeline

- Create procedural templates:
  - block builder
  - connector generator
  - clay / voxel shell generator
  - print bed preview
- Let Agent commands modify template parameters.
- Add export pathway concepts:
  - mesh output
  - voxel output
  - STL / OBJ export
  - future slicer or G-code integration.

## 7. Source Links

- Smart Cube Gaming Controller: https://github.com/ignisco/Smart-Cube-Gaming-Controller
- dice-box: https://github.com/3d-dice/dice-box
- awesome-blender: https://github.com/agmmnn/awesome-blender
- Procedural 3D Modeling Using Geometry Nodes in Blender, Second Edition: https://github.com/PacktPublishing/Procedural-3D-Modeling-Using-Geometry-Nodes-in-Blender-Second-Edn
- geometry-script: https://github.com/carson-katri/geometry-script
- BVtkNodes: https://github.com/tkeskita/BVtkNodes
- BVtkNodes fork: https://github.com/simboden/BVtkNodes
- voxel-builder: https://github.com/nimadez/voxel-builder
- voxel-builder live demo: https://nimadez.github.io/voxel-builder/
- voxel2gcode: https://github.com/nonoesp/voxel2gcode

