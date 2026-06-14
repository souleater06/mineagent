# RubikFlow csTimer Plugin Memory Brief

## Core Memory

This repository is now being used to design a csTimer plugin for RubikFlow Agent.

csTimer is the host. csTimer is not just a normal timer in this direction. It is the smart cube action input endpoint and the RubikFlow workflow trigger. The physical smart cube is the user's real control device. Every detected cube move can become a workflow command.

Core sentence:

Program by rotating a smart cube, let csTimer detect and route the action, visualize the Roll-inspired workflow, and let the Agent generate buildable and printable creations.

## Product Model

- Cube = physical input device.
- csTimer = smart cube move detector, input endpoint, and workflow trigger.
- RubikFlow plugin = move normalizer, workflow mapper, UI, and event bridge.
- Roll-inspired UI = workflow feedback interface.
- Web Mock = fastest browser-side visualization and debugging target.
- Blender = high-quality visualization stage and digital twin scene.
- WebGL = live browser-native 3D preview.
- Agent = move interpretation and generation brain.
- Blocks / clay / voxels / connectors / 3D printing = final physical output directions.

## What This Is Not

- Not a separate Blender-only demo.
- Not a pure Roll clone.
- Not a normal dice game.
- Not just a pretty UI.
- Not using the cube as decoration.
- Not visual-only without move-to-workflow logic.
- Not direct long-term edits to generated `dist/js/cstimer.js`.
- Not an `npm_export` scramble-only feature.

## csTimer Structure Memory

- `src/index.php` loads the uncompiled source scripts in order.
- `Makefile` compiles ordered `src/js` files into `dist/js/cstimer.js`.
- `src/js/kernel.js` exposes the event bus, settings, dialogs, buttons, and windows.
- `src/js/tools/tools.js` exposes the tool registry through `tools.regTool`.
- `src/js/tools/bluetoothutil.js` is the key smart cube utility panel.
- `src/js/timer/giiker.js` uses smart cube input as timer input.
- `src/js/hardware/*cube.js` and `src/js/hardware/bluetooth.js` handle Bluetooth cube drivers.
- `experiment` is useful for move simulation and proof-of-concept work.
- `dist` is generated output.
- `npm_export` is mostly for scramble/image module usage.

Best future source entry:

```text
src/js/tools/rubikflow.js
```

But the first prototype should be a userscript / overlay mock before source integration.

## Initial Move Mapping

Fixed first demo sequence:

```text
U F R F D B
```

Mapping:

| Move | Action | Tile | Output State |
| --- | --- | --- | --- |
| U | Select Module | SCAN / AGENT | Ready |
| F | Generate Block | +BLOCK | Basic Block |
| R | Upgrade Structure | JOINT / STACK | Upgraded Structure |
| F | Add Clay / Voxel Shell | CLAY / VOXEL | Clay / Voxel Shell |
| D | Confirm Node | LOCK | Confirmed / Locked |
| B | Prepare Print | PRINT / EXPORT | Print Ready |

Important: the second `F` is context-sensitive. It does not repeat Generate Block; it means Add Clay / Voxel Shell after the workflow has already generated and upgraded a structure.

## Plugin UI Must Show

- Smart cube / bridge connection status.
- Detected Move.
- Normalized Move.
- Mapped Action.
- Active Workflow-o-pedia tile.
- 20-tile Workflow-o-pedia grid:
  `+BLOCK`, `CLAY`, `VOXEL`, `JOINT`, `MIRROR`, `SCALE`, `COLOR`, `SCAN`, `AGENT`, `PRINT`, `EXPORT`, `SHELL`, `HOLLOW`, `STACK`, `LOCK`, `LOOP`, `CHECK`, `FIX`, `BUILD`, `SAVE`.
- Timeline:
  SELECT MODULE -> GENERATE BLOCK -> UPGRADE STRUCTURE -> ADD CLAY -> CONFIRM -> PREPARE PRINT.
- Output state.
- Creation Score.
- Combo.
- Printability.
- Event/debug log.
- Mock sequence and reset controls.

## Event Shape

Future events should be structured and replayable:

```json
{
  "source": "cstimer-rubikflow",
  "event": "workflow.move",
  "rawMove": "F",
  "normalizedMove": "F",
  "sequence": ["U", "F", "R", "F"],
  "mappedAction": "Add Clay / Voxel Shell",
  "tile": "CLAY",
  "combo": 3,
  "scoreDelta": 180,
  "printabilityDelta": 12,
  "timestamp": 1780000000000
}
```

## Integration Order

1. Documentation and alignment.
2. Userscript / overlay mock in csTimer.
3. Experiment-style deterministic move injector.
4. RubikFlow Web Mock bridge.
5. `src/js/tools/rubikflow.js` source plugin.
6. Real smart cube integration through csTimer smart cube events.
7. Blender and WebGL live bridge.
8. Agent command layer.
9. Physical output pipeline: blocks, clay, voxels, connectors, STL/OBJ/print preparation.

## Development Rules

- Modify only this csTimer project when working in this repository.
- Do not modify RubikFlow project files from here.
- Do not change csTimer source yet during planning-only tasks.
- Prefer overlay/mock before core integration.
- Keep normal csTimer timing and smart cube behavior intact.
- Treat `dist` as generated output.
- Keep the cube-to-workflow mapping explicit.
- Preserve Roll-inspired workflow feedback.
- Prefer stable, readable, replayable events over complex visual tricks.
