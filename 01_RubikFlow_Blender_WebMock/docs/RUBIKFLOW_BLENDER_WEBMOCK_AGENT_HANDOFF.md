# RubikFlow Agent / Blender / Web Mock Handoff

This document is a handoff summary for the current RubikFlow Agent project. It is intended for a team lead or a follow-up Agent to understand the project direction, current artifacts, known limitations, and recommended next steps without re-reading the whole thread history.

## 1. Project Identity

RubikFlow Agent is a prototype system for:

```text
smart cube move
-> workflow tile
-> agent command
-> output preview
-> buildable / printable result
```

Core product idea:

```text
physical smart cube U/F/R/F/D/B moves
-> SELECT / BLOCK / LOGIC / CLAY / LOCK / PRINT workflow
-> Roll-inspired UI feedback
-> Blender / Web / WebGL visualization
-> block, clay, voxel, or 3D-print output
```

The project is not a Roll clone and not only a Rubik's cube animation. The cube is the physical input device, the Roll-inspired interface is workflow feedback, Blender is the visualization stage, and the Agent is the move interpretation / generation brain.

## 2. Current Repository

Current project path:

```text
D:\codex-blender\rubikflow-agent
```

This repository is the RubikFlow / Blender / Web Mock project.

Important separation:

- Do not mix this project with the csTimer plugin project.
- Do not involve AuthentiX.
- Do not modify other project directories while working on this repository.

## 3. Key Files

| File / Folder | Purpose |
| --- | --- |
| `memorize.md` | The most important long-term product memory. It defines the RubikFlow Agent concept, cube-to-workflow mapping, visual rules, and constraints. |
| `README.md` | The original Blender Python demo overview and usage notes. |
| `task.md` | Current task and iteration notes for the Blender demo direction. |
| `docs/REFERENCE_PROJECTS.md` | Analysis of reference projects and derivative design direction, including smart cube controller, dice / Roll-like interaction, Blender node workflows, and voxel / print output. |
| `docs/LAYOUT_REFACTOR_REPORT.md` | Record of Blender layout refactor passes, z-order fixes, object cleanup, keyframe alignment, and clean demo attempts. |
| `web/rubikflow_web_mock.html` | The current most usable visual prototype. It is a single-file HTML/CSS/JS mock for the RubikFlow UI. |
| `web/README.md` | Usage and layout notes for the Web Mock. |
| `rubikflow_agent_demo.py` | Earlier Blender Python demo. It contains the fuller Blender scene generation direction but has had layout and visibility issues across iterations. |
| `rubikflow_agent_clean_demo.py` | Later clean Blender demo attempt. It tried to simplify layout, but the Web Mock is currently the more stable visual reference. |
| `renders/` | Render output folder for Blender or visual references. |
| `refs/` | Reference images and visual materials. |

## 4. Current Main Usable Demo

The recommended demo to open now is:

```text
D:\codex-blender\rubikflow-agent\web\rubikflow_web_mock.html
```

How to open:

```text
Double-click web/rubikflow_web_mock.html
```

This Web Mock is currently the best presentation artifact for team lead review because it is more stable than the Blender Python UI layout. It is a single-file HTML prototype with embedded CSS and JS. It does not need a build step, server, CDN, database, or external assets.

The mock is designed for a 1920 x 1080 browser window with no page scrollbars.

## 5. Current Web Mock Status

`web/rubikflow_web_mock.html` currently implements:

- `Smart Cube Input`
- U/F/R/F/D/B step bar
- Active Face On Top
- Cube Command Lens
- a CSS-only 2.5D cube visual with a strict 3 x 3 `cubelet` top face
- a contained `cube-arrow`
- `RubikFlow Agent` title area
- `Workflow-o-pedia`
- 20 workflow tiles
- Triggered Tile / Agent Command / Result info strip
- SCORE / COMBO / PRINTABILITY cards
- Agent State
- Agent Function Pipeline
- Output Preview
- Workflow Timeline
- LOGIC / CLAY / LOCK keyframe state switching
- warm cream background, white rounded cards, soft icon colors, and a Roll-inspired product UI feel

Current cube visual classes:

```text
cube-shadow
cube-base
cube-top
cubelet
cube-arrow
```

The latest cube visual intentionally avoids:

- black vertical side plates
- rear flaps
- folding panels
- floating support pieces
- canvas or external 3D libraries

## 6. Current Workflow Mapping

Fixed conceptual move sequence:

```text
MOVES = ["U", "F", "R", "F", "D", "B"]
```

Current workflow mapping:

| Move | Stage | Command | Meaning |
| --- | --- | --- | --- |
| `U` | `SELECT` | `SELECT_MODULE` | Select a workflow module. |
| First `F` | `BLOCK` | `GENERATE_BLOCK` | Generate a basic block. |
| `R` | `LOGIC` | `UPGRADE_LOGIC` / `UPGRADE_STRUCTURE` | Add logic nodes, redstone-like signal lines, or structural connectors. |
| Second `F` | `CLAY` | `ADD_CLAY_SHELL` | Add a clay / voxel shell around the structure. |
| `D` | `LOCK` | `CONFIRM_LOCK` | Confirm and lock the generated structure. |
| `B` | `PRINT` | `PREPARE_PRINT` | Prepare print bed, slicing lines, and print-ready state. |

Timeline:

```text
SELECT -> BLOCK -> LOGIC -> CLAY -> LOCK -> PRINT
```

## 7. Key Visual States

The Web Mock currently focuses on three keyframe states.

### LOGIC / R

- Active Face: `R FACE`
- Workflow tile: `JOINT`
- Agent Pipeline: `LOGIC`
- Output Preview: grey base blocks, red signal lines, red logic nodes
- Result: `ACTIVE`

### CLAY / F

- Active Face: `F FACE`
- Workflow tile: `CLAY`
- Agent Pipeline: `CLAY`
- Output Preview: orange clay / voxel shell
- Result: `BUILDING`

### LOCK / D

- Active Face: `D FACE`
- Workflow tile: `LOCK`
- Agent Pipeline: `LOCK`
- Output Preview: lock icons / confirmed shell
- Result: `LOCKED`

The `LOGIC`, `CLAY`, and `LOCK` buttons in the Web Mock header switch between these states.

## 8. Current Blender Python Status

The Blender Python demos attempted to generate a full RubikFlow Agent scene including:

- 27 cubelets for the smart cube digital twin
- U/F/R/F/D/B layer-turn logic
- `MOVE_CONFIG`
- `FACE_COLORS`
- Workflow-o-pedia
- Agent State
- Agent Function Pipeline
- Output Preview
- Workflow Timeline
- orthographic 1920 x 1080 product composition

However, the Blender versions have repeatedly run into presentation problems:

- text overlap
- panel overlap
- floating or stray objects
- black triangle / helper object visibility
- camera / front orthographic confusion
- z-depth issues
- Output Preview containment issues
- difficulty making dense app UI stable directly in Blender

Current recommendation:

Use `web/rubikflow_web_mock.html` as the visual standard first, then rebuild Blender or WebGL / Three.js from that stable layout.

## 9. Current Issues / Limitations

Current limitations:

- The Web Mock is still a visual prototype, not the final application.
- The cube visual is CSS-only; it is not a real WebGL cube.
- The Web Mock has only three main keyframe states: LOGIC, CLAY, and LOCK.
- U / SELECT, first F / BLOCK, and B / PRINT are part of the conceptual mapping but are less developed in the current Web Mock UI state switching.
- The Blender Python demos are not yet recommended as the final presentation version.
- Real smart cube hardware input is not connected yet.
- Real csTimer move events are not connected yet.
- Geometry Nodes / voxel generation / slicing / STL export are not implemented yet.
- Output Preview is a styled prototype, not a real modeling or print pipeline.

Recent Web Mock repair focus:

- Make Smart Cube Input read as a clear 3 x 3 smart cube input device.
- Avoid black side plates, rear panels, side flaps, and floating visual layers.
- Keep Output Preview from covering Agent Function Pipeline.
- Keep 1920 x 1080 single-screen layout stable.

## 10. Relation To csTimer Plugin Project

Separate project path:

```text
D:\codex-work\cstimer-plugin-dev\cstimer
```

Known related artifact:

```text
experiment/rubikflow-overlay-demo.html
```

The csTimer plugin project is responsible for the input/MVP integration side:

- keyboard or smart cube move simulation
- future real smart cube events
- event log
- export JSON
- `window.RubikFlowAgent` API

The RubikFlow Blender / Web Mock project is responsible for the visual/product prototype side:

- product UI direction
- Workflow-o-pedia
- Smart Cube Input presentation
- Agent State
- Output Preview
- Blender / WebGL / front-end visual reference

These projects are related but should not be mixed into the same files or directories.

## 11. Relation To AuthentiX

RubikFlow Agent has no functional relationship with AuthentiX or miniAuthentiX.

Do not modify:

```text
D:\codex-work\AuthentiX
D:\codex-work\miniAuthentiX
```

Do not import concepts, files, UI, data models, or implementation details from AuthentiX into this project.

## 12. Recommended Next Step

Recommended next step:

Continue polishing `web/rubikflow_web_mock.html` as the source of visual truth.

Priority order:

1. Confirm the Smart Cube Input cube reads clearly as a 3 x 3 smart cube in an actual 1920 x 1080 browser screenshot.
2. Audit all z-index / stacking relationships in the Web Mock after each visual change.
3. Keep LOGIC / CLAY / LOCK states stable and readable.
4. Add or strengthen U / SELECT, F / BLOCK, and B / PRINT states only after the three core keyframes are stable.
5. Later migrate the Web Mock design to WebGL / Three.js or rebuild Blender using fixed panel coordinates from the Web Mock.

If continuing Blender:

- Do not keep piling UI text and panels into Blender.
- Use the Web Mock as the layout blueprint.
- Rebuild the Blender UI as fewer, larger, fixed-position cards.
- Keep the cube digital twin visible but separate from the main workflow UI.

## 13. What Not To Do

Do not:

- modify AuthentiX
- modify miniAuthentiX
- modify the csTimer plugin project from this repository task
- mix RubikFlow Web Mock and csTimer overlay into one file
- treat the current Blender Python demo as the final presentation
- continue adding dense text to Blender panels
- add a backend or database
- introduce external UI assets without review
- copy external project code, UI, assets, or license text
- remove the Smart Cube Input concept
- remove Output Preview

## 14. Handoff Summary For Team Leader

RubikFlow Agent currently has two main directions:

1. `web/rubikflow_web_mock.html`

   This is the current most stable RubikFlow visual prototype. It shows the smart cube input layer, Workflow-o-pedia, Agent State, Agent Function Pipeline, Output Preview, and Workflow Timeline in a warm Roll-inspired product UI.

2. Blender Python demos

   `rubikflow_agent_demo.py` and `rubikflow_agent_clean_demo.py` explored generating the same idea directly in Blender. They contain useful logic and scene-generation experiments, but the Blender UI has had repeated layout, visibility, and overlap issues. The current recommendation is to use the Web Mock as the visual source of truth before attempting another Blender or WebGL implementation.

Core idea:

```text
U/F/R/F/D/B cube moves
-> SELECT / BLOCK / LOGIC / CLAY / LOCK / PRINT workflow
-> Agent command
-> visual output
-> buildable / printable result
```

In short:

RubikFlow Agent turns a physical smart cube into a spatial workflow controller for a Roll-inspired Agent creation pipeline.

