# RubikFlow csTimer Plugin Development Plan

## 1. Direction

RubikFlow should now be implemented with csTimer as the host. The goal is not to continue a separate Blender-only demo. The new direction is:

Physical smart cube move -> csTimer detects move -> RubikFlow plugin maps it to a workflow command -> RubikFlow Web Mock / Blender / WebGL visualize and execute the workflow.

In this direction, csTimer is not just a timer. It becomes the smart cube action input endpoint and RubikFlow workflow trigger. The timer, scramble, Bluetooth cube, reconstruction, and event pipeline already inside csTimer become the bridge between real hand motion and an Agent-driven creative workflow.

RubikFlow remains:

- Cube = physical input device.
- Roll-inspired UI = workflow feedback interface.
- Blender = visualization stage.
- Agent = move interpretation and generation brain.
- Blocks / clay / voxels / 3D printing = final physical creation outputs.

The csTimer plugin should preserve that idea, but move the first integration point from Blender to csTimer.

## 2. Source Context Read

The csTimer project is organized as follows:

- `README.md`: Describes csTimer as a professional speedcubing/training timer, explains the online version policy, local browser storage, third-party deployment caveats, and the `cstimer_module` package.
- `src`: Main source tree. `src/index.php` loads scripts in source order. `src/js/kernel.js` provides the central event bus, settings registry, UI windows, buttons, and dialogs. `src/js/timer.js` controls timer state and pushes `timerStatus` and `time` signals. `src/js/tools` contains tool-window extensions. `src/js/hardware` contains Bluetooth smart cube and timer drivers. `src/js/timer/giiker.js` and `src/js/tools/bluetoothutil.js` connect smart cube state and moves to timer behavior.
- `dist`: Built output. It contains `dist/js/cstimer.js`, `dist/js/twisty.js`, language files, service worker, PHP entry files, and static assets. Current checkout does not include `dist/local`.
- `experiment`: Experimental scripts such as BLE move simulation and puzzle analysis. These are useful for prototyping move injection and workflow proof-of-concept behavior, but not as the final integration layer.
- `lib`: Build dependencies, especially Closure Compiler and legacy jQuery.
- `npm_export`: A standalone `cstimer_module` package focused on scramble and image generation. It does not contain the full csTimer UI, timer, or Bluetooth smart cube workflow surface.

The build path is source-first: `Makefile` compiles ordered `src/js` files into `dist/js/cstimer.js`. Direct edits to `dist/js/cstimer.js` should be avoided except for disposable local experiments.

## 3. Best Extension Entry

The best long-term extension point is a new csTimer tool module under `src/js/tools`, because csTimer already treats tools as pluggable panels through:

- `tools.regTool(name, label, execFunc)`
- `kernel.regListener(module, signal, callback, filter)`
- `kernel.regProp(module, key, type, label, values, sessionRelated)`
- `kernel.pushSignal(signal, value)`

The RubikFlow plugin should be modeled like existing tools such as `bluetoothutil`, `battle`, `onlinecomp`, `stats`, and `image`.

Recommended future source entry:

- `src/js/tools/rubikflow.js`
- Add it to `src/index.php` after `bluetoothutil.js` once real source integration begins.
- Add it to `Makefile` `timerSrc` after `tools/bluetoothutil.js` once it should be compiled into `dist/js/cstimer.js`.

Important existing modules to reuse:

- `src/js/tools/bluetoothutil.js`: Smart cube connection, state drawing, callbacks, battery, move timestamp fitting, reconstruction, and smart scramble state.
- `src/js/timer/giiker.js`: Smart cube as timer input; detects solved/scrambled states and emits solve records with move reconstruction.
- `src/js/hardware/bluetooth.js`: `GiikerCube` device group and smart cube model registration.
- `src/js/hardware/gancube.js`, `giikercube.js`, `gocube.js`, `moyucube.js`, `moyu32cube.js`, `qiyicube.js`: Supported smart cube drivers.
- `src/js/kernel.js`: Central event bus and UI registry.
- `src/js/tools/tools.js`: Tool panel registry.

## 4. Prototype Strategy

The first implementation should not immediately modify csTimer core source.

Recommended order:

1. Userscript / overlay mock on top of csTimer source or local build.
2. Experiment demo for deterministic U/F/R/F/D/B move injection.
3. Formal `src/js/tools/rubikflow.js` integration.
4. Optional build integration into `Makefile` and `src/index.php`.

Why start with userscript / overlay mock:

- It validates move-to-workflow mapping without risking timer regressions.
- It can listen to existing globals such as `kernel`, `tools`, `timer`, `GiikerCube`, and `giikerutil`.
- It can render a RubikFlow panel over csTimer without touching core UI.
- It lets us test Web Mock / Blender / WebGL messaging before committing to source integration.
- It keeps the csTimer codebase clean while the product logic is still changing.

Why not start by editing `dist`:

- `dist/js/cstimer.js` is generated and hard to maintain.
- Any manual edit can be overwritten by the next build.
- It hides the real source ownership boundary.

Why not start in `npm_export`:

- `npm_export` is useful for scramble generation, not full smart cube input or UI.
- RubikFlow needs real-time move events, plugin UI, status panels, and workflow triggers.

Why not start in `experiment` as the final location:

- `experiment` is good for BLE simulation and proof-of-concept logic.
- It is not wired into the production UI and build path.

## 5. Plugin Role

The RubikFlow csTimer plugin should have three roles.

### 5.1 Input Endpoint

The plugin receives or infers smart cube moves from csTimer:

- Real Bluetooth cube move events through `GiikerCube.callback`.
- Smart cube solve reconstruction from `timer.giiker` and `giikerutil`.
- Existing csTimer signals such as `scramble`, `scrambleX`, `time`, `timestd`, `timerStatus`, and `giirecons`.
- Prototype keyboard or scripted moves for U/F/R/F/D/B.

### 5.2 Workflow Mapper

The plugin converts cube moves into RubikFlow commands:

- Single moves map to simple workflow nodes.
- Move sequences map to higher-level Agent intents.
- Combos increase score, unlock material actions, or trigger chained nodes.
- Invalid or incomplete move sequences enter a safe pending state instead of executing destructive operations.

### 5.3 Output Bridge

The plugin forwards structured events to other RubikFlow surfaces:

- RubikFlow Web Mock: Browser-based Roll-inspired workflow board and output preview.
- Blender: Digital twin scene, 3D workflow visualization, block/clay/voxel/print demo.
- WebGL: Lightweight browser-native 3D preview, useful before or beside Blender.
- Agent layer: Move interpretation, command suggestion, model operation planning.

## 6. Initial Move Mapping

The first fixed demo sequence remains:

```text
MOVES = ["U", "F", "R", "F", "D", "B"]
```

The plugin should treat face moves as workflow commands, not speedcubing notation only.

| Move | Mapped Action | Workflow Tile | csTimer Plugin Response | External Visual Response |
| --- | --- | --- | --- | --- |
| U | Select Module | SCAN / AGENT | Update Detected Move to U; set state to selecting | Highlight selection tile and first timeline node |
| F | Generate Block | +BLOCK | Add command event; score + base amount; combo starts | Show basic block in output preview |
| R | Upgrade Structure | JOINT / STACK | Increase combo; mark structure upgrade | Add supports, joints, or stacked structure |
| F | Add Clay / Voxel Shell | CLAY / VOXEL | Interpret second F in sequence context | Add clay layer, voxel shell, or soft cover |
| D | Confirm Node | LOCK | Set workflow state to confirmed | Show LOCKED / Confirmed state |
| B | Prepare Print | PRINT / EXPORT | Finalize workflow command packet | Show print platform, slicing lines, STL/Print Ready |

The second `F` must be context-sensitive. A first `F` after `U` means Generate Block. A second `F` after `U F R` means Add Clay / Voxel Shell.

## 7. Expanded Move Command Design

The plugin should separate raw move, normalized move, workflow command, and Agent intent.

Example event:

```json
{
  "source": "cstimer-rubikflow",
  "event": "workflow.move",
  "rawMove": "F'",
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

Normalization rules for the first prototype:

- `U`, `U'`, `U2` all belong to the Select Module family.
- `F`, `F'`, `F2` all belong to the Generate / Material family, with sequence context deciding which action.
- `R`, `R'`, `R2` belong to Upgrade Structure.
- `D`, `D'`, `D2` belong to Confirm Node.
- `B`, `B'`, `B2` belong to Prepare Print.
- `L`, `L'`, `L2` can be reserved for Undo / Back / Repair in a later version.

Later mapping can use richer grammar:

- Same face repeated: strengthen current command.
- Opposite faces: branch or compare workflow path.
- Slice / rotation moves: mode switch.
- Solved cube state: reset workflow.
- Scrambled cube state: initialize material bank.
- Full solve reconstruction: generate an Agent prompt from the user's whole interaction session.

## 8. Plugin UI

The csTimer plugin UI should live as a tool panel at first. It should not replace csTimer's timer view.

Minimum UI sections:

- Connection: Smart cube connection status, device name, battery if available, Web Mock / Blender / WebGL bridge status.
- Detected Move: last raw move, normalized move, face highlight, timestamp.
- Mapped Action: current RubikFlow command, active tile, confidence, sequence context.
- Workflow-o-pedia: 20 tiles in a compact grid: `+BLOCK`, `CLAY`, `VOXEL`, `JOINT`, `MIRROR`, `SCALE`, `COLOR`, `SCAN`, `AGENT`, `PRINT`, `EXPORT`, `SHELL`, `HOLLOW`, `STACK`, `LOCK`, `LOOP`, `CHECK`, `FIX`, `BUILD`, `SAVE`.
- Timeline: SELECT MODULE -> GENERATE BLOCK -> UPGRADE STRUCTURE -> ADD CLAY -> CONFIRM -> PREPARE PRINT.
- Output State: Ready, Basic Block, Upgraded Structure, Clay/Voxel Shell, Locked, Print Ready.
- Metrics: Creation Score, Combo, Printability.
- Debug Log: last N events, last outbound payload, errors.
- Controls: Start mock sequence, reset workflow, connect bridge, copy event payload.

The UI should feel like a utility panel inside csTimer, not a landing page. It should be dense, readable, and focused on repeated live use.

## 9. Data Flow

Prototype data flow:

```text
Keyboard/userscript simulated move
-> RubikFlow overlay
-> workflow state reducer
-> UI update
-> optional postMessage/WebSocket/local endpoint
-> Web Mock / Blender / WebGL
```

Real smart cube data flow:

```text
Smart cube hardware
-> csTimer hardware driver
-> GiikerCube callback / giikerutil
-> RubikFlow plugin listener
-> move normalizer
-> workflow mapper
-> plugin UI update
-> Agent / Web Mock / Blender / WebGL bridge
```

Solve reconstruction data flow:

```text
Smart cube solve
-> timer.giiker records move sequence and timestamps
-> kernel.pushSignal("time" / "timestd" / "giirecons")
-> RubikFlow plugin packages session summary
-> Agent interprets the full interaction
-> generated structure plan is visualized and exported
```

## 10. External Integration

### 10.1 RubikFlow Web Mock

The Web Mock should be the first external target because it is fast to iterate. The csTimer plugin can send move events by:

- `window.postMessage` when embedded or side-by-side in the same browser context.
- `BroadcastChannel` when both pages run under compatible browser scope.
- `localStorage` event for a simple no-server prototype.
- WebSocket for the first robust bridge.

The Web Mock should mirror:

- Detected Move.
- Mapped Action.
- 20-tile Workflow-o-pedia.
- Timeline.
- Output Preview.
- Score / Combo / Printability.

### 10.2 Blender

Blender should remain the high-quality visualization stage. The csTimer plugin should not directly own Blender scene logic. It should emit a clean command stream that a Blender bridge can consume.

Blender should show:

- A visible smart cube digital twin in its own input zone.
- Detected Move and Mapped Action.
- Roll-inspired workflow stage.
- Output preview progression from empty to print-ready.
- Complete orthographic 16:9 view with no missing core elements.

Possible bridge options:

- Local WebSocket server consumed by a Blender Python add-on/script.
- JSON command file watched by Blender during early development.
- Manual export/import of a recorded command session for deterministic demos.

### 10.3 WebGL

WebGL can sit between Web Mock and Blender:

- Faster live preview than Blender.
- Runs in browser beside csTimer.
- Useful for cube digital twin, tile board, and output object preview.
- Can later share geometry/export data with Blender or Agent-generated assets.

## 11. Agent Layer

The Agent should not be required for the earliest overlay demo, but the plugin API should be designed for it.

Agent responsibilities:

- Interpret raw move sequences into higher-level workflow operations.
- Suggest next moves or next workflow tile.
- Detect invalid workflow states.
- Generate block, clay, voxel, connector, and print-preparation plans.
- Summarize solve/session history into reusable workflow presets.

The plugin should send structured facts, not screenshots:

- Move history.
- Current cube state if available.
- Current workflow state.
- Active tile.
- Score, combo, printability.
- Output mode.
- Any reconstruction string from csTimer.

## 12. Phased Roadmap

### Phase 0: Documentation and Alignment

- Create this plugin plan.
- Create a memory brief for future work.
- Confirm csTimer is the host and input endpoint.
- No csTimer source changes yet.

### Phase 1: Overlay Mock

- Create a userscript or local overlay against csTimer.
- Simulate `U F R F D B`.
- Render RubikFlow panel with Detected Move, Mapped Action, tiles, timeline, score, combo, printability.
- Produce structured JSON events.
- Keep all logic removable.

### Phase 2: Experiment Move Injector

- Use an experiment-style script to inject deterministic moves.
- Reuse the spirit of `experiment/bleHack.js` only for local testing.
- Validate sequence state transitions and second-`F` context behavior.

### Phase 3: Web Mock Bridge

- Send move events to RubikFlow Web Mock.
- Update Web Mock in real time from csTimer-originated events.
- Add bridge status to plugin UI.
- Record and replay sessions.

### Phase 4: Source Tool Plugin

- Add `src/js/tools/rubikflow.js`.
- Register it through `tools.regTool`.
- Add settings through `kernel.regProp`.
- Listen to smart cube and timer signals through `kernel.regListener`.
- Keep the first source implementation small and reversible.

### Phase 5: Real Smart Cube Integration

- Hook into `giikerutil` / `GiikerCube` move events carefully.
- Preserve csTimer's normal timer behavior.
- Normalize raw moves into workflow commands.
- Add debug mode for device data and event payloads.

### Phase 6: Blender and WebGL Live Bridge

- Emit WebSocket or file-based command stream.
- Drive Blender digital twin and Roll-inspired stage.
- Drive WebGL preview for lower-latency browser visualization.
- Keep csTimer responsible for input and command emission, not scene ownership.

### Phase 7: Agent and Physical Output Pipeline

- Add Agent command interpretation.
- Generate block, clay, voxel, connector, and print-preparation instructions.
- Export STL/OBJ hints or real geometry through downstream tools.
- Add reusable workflow presets and Redstone-like node chaining.

## 13. Acceptance Checklist

Every future implementation should satisfy:

- csTimer remains the host.
- The plugin treats csTimer as smart cube input endpoint and workflow trigger.
- The plugin can run without modifying external projects.
- RubikFlow core ideas are visible: cube input, Roll-inspired workflow, Agent intent, physical output path.
- U/F/R/F/D/B mapping works.
- The second `F` is context-aware.
- Plugin UI shows connection, detected move, mapped action, tiles, timeline, output state, score, combo, printability, and debug log.
- External events are structured and replayable.
- Normal csTimer timing and smart cube behavior are not broken.
- No direct edits are made to generated `dist/js/cstimer.js` for long-term work.
- No source integration happens before the overlay/mock proves the workflow.

## 14. Immediate Next Step

The next implementation step should be an overlay mock, not a core source edit:

1. Load csTimer locally or through source mode.
2. Inject a RubikFlow overlay panel.
3. Simulate `U F R F D B`.
4. Generate the same event payload shape that future real cube integration will use.
5. Send optional events to a Web Mock target.
6. Only after the interaction feels right, promote the overlay into `src/js/tools/rubikflow.js`.
