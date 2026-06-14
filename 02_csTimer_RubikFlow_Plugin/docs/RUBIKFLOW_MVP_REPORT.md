# RubikFlow csTimer Overlay MVP Report

## Daily Closeout Archive

Current runnable file:

```text
experiment/rubikflow-overlay-demo.html
```

Full local path:

```text
D:\codex-work\cstimer-plugin-dev\cstimer\experiment\rubikflow-overlay-demo.html
```

Today's closeout checkpoint is the MVP 3 overlay demo. The current demo establishes csTimer as the host surface and keeps RubikFlow Agent as an overlay-style plugin prototype.

### MVP 3 Completed Functions

- Left side: static csTimer mock page.
- Right side: RubikFlow Agent Overlay.
- Keyboard input for `U / F / R / D / B`.
- `Run U F R F D B` sequence button.
- `Reset` button.
- Event Log.
- `Export JSON`.
- Output Preview.
- Context-aware second `F`, mapped to `CLAY / ADD_CLAY_SHELL`.

### How To Open

Double-click:

```text
D:\codex-work\cstimer-plugin-dev\cstimer\experiment\rubikflow-overlay-demo.html
```

No local server or build step is required for this checkpoint because the demo is a single static HTML file.

### How To Test

Click the page, then press:

```text
U -> F -> R -> F -> D -> B
```

Expected flow:

| Input | Expected Command |
| --- | --- |
| `U` | `SELECT_MODULE` |
| first `F` | `GENERATE_BLOCK` |
| `R` | `UPGRADE_LOGIC` |
| second `F` | `ADD_CLAY_SHELL` |
| `D` | `CONFIRM_LOCK` |
| `B` | `PREPARE_PRINT` |

You can also click `Run U F R F D B` to execute the same sequence automatically.

### Current Limitations

- No real Bluetooth smart cube is connected.
- No real csTimer move event is connected yet.
- The left side is a csTimer mock, not the real `timer.php` runtime.
- This is still an overlay MVP, not the formally integrated csTimer plugin.

### Tomorrow's Starting Point

MVP 4 should start by abstracting the overlay input path into a public event adapter:

```text
window.RubikFlowAgent
```

Planned MVP 4 methods:

- `receiveMove(move)`
- `getEvents()`
- `getState()`
- `reset()`
- `runSequence()`
- `exportEvents()`

The goal is to let future real csTimer move events and smart cube events call one unified entry instead of being tied directly to keyboard or button handlers.

### Build Note

No build was run and no build is needed for this closeout checkpoint. The current artifact is a standalone HTML demo that can be opened directly from disk.

## What Changed

The first-stage RubikFlow MVP is implemented in:

```text
experiment/rubikflow-overlay-demo.html
```

The page is now fully static and can be opened by double-clicking the HTML file. It contains:

- A static csTimer mock area on the left.
- A RubikFlow Agent Overlay on the right.
- Keyboard simulation for `U / F / R / D / B`.
- Timeline highlighting for `SELECT -> BLOCK -> LOGIC -> CLAY -> LOCK -> PRINT`.
- Output Preview states for logic, clay shell, lock, and print preparation.

No real Bluetooth cube integration is included in this MVP.

## Why The Page Does Not iframe PHP

The original overlay prototype used an iframe pointing to:

```text
../dist/timer.php
```

That is not reliable for a double-clickable local MVP because browsers do not execute PHP files when they are opened directly from disk. Instead, the browser shows the PHP source or fails to render it as an application.

For this first-stage MVP, running the csTimer backend is not required. The PHP iframe was replaced with a static csTimer mock area so the demo works immediately from the filesystem.

## How To Open

Double-click this file:

```text
D:\codex-work\cstimer-plugin-dev\cstimer\experiment\rubikflow-overlay-demo.html
```

Expected result:

- Left side: static csTimer mock page with timer `0.00`, scramble text, and session / ao5 / ao12 panels.
- Right side: RubikFlow Agent Overlay.

## Keyboard Test

Click anywhere on the page, then press:

| Key | Workflow Stage | Agent Command | Output Preview |
| --- | --- | --- | --- |
| `U` | SELECT MODULE | SELECT_MODULE | Ready / selected state |
| `F` | GENERATE BLOCK | GENERATE_BLOCK | Basic block |
| `R` | UPGRADE LOGIC | UPGRADE_LOGIC | Grey base, red signal lines, logic nodes |
| second `F` | ADD CLAY SHELL | ADD_CLAY_SHELL | Base with orange clay shell |
| `D` | CONFIRM LOCK | CONFIRM_LOCK | Shell with locked state |
| `B` | PREPARE PRINT | PREPARE_PRINT | Print bed, slicing lines, print ready |

The page also includes a `Run U F R F D B` button to play the full MVP sequence automatically.

## Current Limitations

- The left csTimer area is a static mock, not the real csTimer runtime.
- The timer does not count.
- The scramble and session stats are static.
- There is no real Bluetooth smart cube connection.
- The RubikFlow state is driven only by keyboard events and the built-in demo sequence button.

## MVP 2 Overlay Function Upgrade

The second MVP pass keeps the same static HTML entry point and upgrades the RubikFlow Overlay into a clearer product-like workflow panel.

### Changed Functions

- Improved the RubikFlow Overlay copy so the left side is clearly the original speedcubing timer area and the right side is the RubikFlow Agent plugin mock.
- Added a clearer READY state for the Output Preview.
- Added a SELECT preview state that shows a selected workflow module.
- Improved the BLOCK, LOGIC, CLAY, LOCK, and PRINT preview states.
- Added human-readable Event Log lines such as `[01] U -> SELECT_MODULE`.
- Added `Export JSON` for the current workflow event log.
- Added clipboard fallback behavior: if copy is blocked, the JSON is shown inside the overlay.

### How To Open The Demo

Double-click:

```text
D:\codex-work\cstimer-plugin-dev\cstimer\experiment\rubikflow-overlay-demo.html
```

No PHP server is required for this MVP. The csTimer area is intentionally static so the file can run directly from disk.

### How To Test U / F / R / D / B

Click the page and press:

| Key | Timeline Stage | Agent Command |
| --- | --- | --- |
| `U` | SELECT | SELECT_MODULE |
| first `F` | BLOCK | GENERATE_BLOCK |
| `R` | LOGIC | UPGRADE_LOGIC |
| second `F` | CLAY | ADD_CLAY_SHELL |
| `D` | LOCK | CONFIRM_LOCK |
| `B` | PRINT | PREPARE_PRINT |

The `Run U F R F D B` button executes the same sequence automatically. `Reset` clears the workflow state and returns to READY.

### Timeline Behavior

The Timeline shows:

```text
SELECT -> BLOCK -> LOGIC -> CLAY -> LOCK -> PRINT
```

- Completed steps turn green.
- The current step is highlighted blue.
- Upcoming steps remain grey.
- The second `F` is treated as CLAY / ADD_CLAY_SHELL instead of repeating the first F / GENERATE_BLOCK action.

### Output Preview Meaning

| Preview Stage | Meaning |
| --- | --- |
| READY | Empty work area waiting for cube input |
| SELECT | Selected workflow module |
| BLOCK | Grey base block |
| LOGIC | Grey base plus red signal lines and red logic nodes |
| CLAY | Base with orange clay / voxel shell |
| LOCK | Shell with lock labels and locked state |
| PRINT | Print bed, slicing lines, and PRINT READY label |

### Event Log And Export JSON

The Event Log records every manual or automated move. Example:

```text
[01] U -> SELECT_MODULE
[02] F -> GENERATE_BLOCK
[03] R -> UPGRADE_LOGIC
[04] F -> ADD_CLAY_SHELL
[05] D -> CONFIRM_LOCK
[06] B -> PREPARE_PRINT
```

`Reset` clears the log.

`Export JSON` exports the current workflow event log as an array:

```json
[
  {
    "step": 1,
    "move": "U",
    "stage": "SELECT",
    "command": "SELECT_MODULE",
    "output": "Module selected"
  }
]
```

When browser clipboard access is allowed, the JSON is copied to the clipboard. If clipboard access is blocked, the same JSON is displayed inside the overlay.

### Next Stage: Real csTimer Move Event / Smart Cube Event

The next integration stage should replace keyboard events with real csTimer-originated move events while keeping the same workflow reducer and event JSON shape.

Recommended path:

1. Keep this HTML as the visual mock and interaction reference.
2. Add a userscript or source tool prototype that listens to csTimer runtime events.
3. Bridge from `GiikerCube` / `giikerutil` / `timer.giiker` into the RubikFlow command mapper.
4. Preserve the keyboard mock as a debug fallback.
5. Promote stable logic into `src/js/tools/rubikflow.js` only after the event mapping is proven.

## MVP 3 Interaction and Event Structure Upgrade

The third MVP pass turns the overlay into a more stable plugin prototype. It keeps the same static entry point and still does not connect to real Bluetooth hardware.

### Added Interactions

- The Timeline steps are now clickable controls.
- Clicking `U SELECT`, `F BLOCK`, `R LOGIC`, `F CLAY`, `D LOCK`, or `B PRINT` triggers the same workflow update as keyboard input.
- Keyboard input remains active for `U / F / R / D / B`.
- `Run U F R F D B` still executes the full sequence automatically.
- `Reset` returns the overlay to READY and clears all recorded events.

### Unified Event Structure

Every manual key press, clickable Timeline step, and Run Sequence action creates the same event object shape:

```json
{
  "step": 1,
  "move": "U",
  "face": "UP",
  "stage": "SELECT",
  "command": "SELECT_MODULE",
  "output": "Module selected",
  "timestamp": 1710000000000
}
```

The overlay stores these objects in one workflow event array. `Export JSON` reads from that array directly.

### Keyboard And Button Triggering

Keyboard mapping:

| Input | Stage | Command |
| --- | --- | --- |
| `U` | SELECT | SELECT_MODULE |
| first `F` | BLOCK | GENERATE_BLOCK |
| `R` | LOGIC | UPGRADE_LOGIC |
| second `F` | CLAY | ADD_CLAY_SHELL |
| `D` | LOCK | CONFIRM_LOCK |
| `B` | PRINT | PREPARE_PRINT |

Clickable step mapping:

| Button | Stage | Command |
| --- | --- | --- |
| `U SELECT` | SELECT | SELECT_MODULE |
| `F BLOCK` | BLOCK | GENERATE_BLOCK |
| `R LOGIC` | LOGIC | UPGRADE_LOGIC |
| `F CLAY` | CLAY | ADD_CLAY_SHELL |
| `D LOCK` | LOCK | CONFIRM_LOCK |
| `B PRINT` | PRINT | PREPARE_PRINT |

The two `F` steps are separate Timeline buttons. Keyboard input still treats the first `F` as BLOCK and the second/contextual `F` as CLAY.

### Event Log Behavior

The Event Log shows a readable line for each event:

```text
[01] U -> SELECT_MODULE
[02] F -> GENERATE_BLOCK
[03] R -> UPGRADE_LOGIC
[04] F -> ADD_CLAY_SHELL
[05] D -> CONFIRM_LOCK
[06] B -> PREPARE_PRINT
```

- New events scroll the log to the bottom.
- `Reset` clears the log.
- `Run U F R F D B` produces all six events.
- Manual keyboard input and clicked Timeline buttons use the same logging path.

### Export JSON

`Export JSON` exports the unified workflow event array.

- Clipboard is tried first.
- If the browser blocks clipboard access, the JSON appears in the overlay.
- Empty workflows export as `[]`.

Example exported data:

```json
[
  {
    "step": 1,
    "move": "U",
    "face": "UP",
    "stage": "SELECT",
    "command": "SELECT_MODULE",
    "output": "Module selected",
    "timestamp": 1710000000000
  }
]
```

### Output Preview Stages

| Stage | Meaning |
| --- | --- |
| READY | Empty work area |
| SELECT | Selected / active module |
| BLOCK | Grey base block |
| LOGIC | Grey base, red signal lines, and red nodes |
| CLAY | Base with orange clay / voxel shell |
| LOCK | Orange shell, lock labels, and locked state |
| PRINT | Print bed, slicing lines, and PRINT READY |

### Next Stage: Real csTimer Move Event / Smart Cube Event

The next stage should replace simulated input with real csTimer events while preserving the MVP 3 event shape.

Recommended next steps:

1. Keep keyboard and button triggering as a debug fallback.
2. Create a userscript or small source tool that listens to csTimer runtime events.
3. Map real move data into the same `{ step, move, face, stage, command, output, timestamp }` object.
4. Hook smart cube events near `GiikerCube`, `giikerutil`, and `timer.giiker`.
5. Only after stable event capture, promote the overlay into `src/js/tools/rubikflow.js`.

## MVP 4 Event Adapter and Public API

The fourth MVP pass turns the overlay from a pure demo page into a small event-adapter prototype. The page is still static and still does not connect to a real Bluetooth cube, but its input model now matches the shape needed by future csTimer move events.

### Why There Is A Unified Event Entry

MVP 3 allowed keyboard input, Timeline button clicks, and Run Sequence to trigger the workflow, but each source was still close to the UI. MVP 4 routes those inputs through one adapter entry:

```text
window.RubikFlowAgent.receiveMove(move)
```

This matters because a real csTimer plugin should not care whether a move came from a keyboard fallback, a clicked test button, a scripted replay, a csTimer smart cube callback, or a later bridge. All of them should produce the same workflow update and the same replayable event object.

### Public API

The page now exposes:

| Method | Purpose |
| --- | --- |
| `window.RubikFlowAgent.receiveMove(move)` | Receives one `U / F / R / D / B` move and updates the RubikFlow workflow. Console calls default to `source: "external"`. |
| `window.RubikFlowAgent.runSequence()` | Runs the fixed `U F R F D B` demo sequence with `source: "sequence"`. |
| `window.RubikFlowAgent.reset()` | Resets current move, active face, workflow stage, output preview, event log, and export panel. |
| `window.RubikFlowAgent.getEvents()` | Returns the current workflow event array. |
| `window.RubikFlowAgent.exportEvents()` | Runs the same JSON export/copy behavior as the `Export JSON` button. |
| `window.RubikFlowAgent.getState()` | Returns current move, active face, stage, command, output, current step, and events. |

### Unified Input Sources

All MVP input paths now call `receiveMove`:

| Input Path | Source Value |
| --- | --- |
| Keyboard `U / F / R / D / B` | `keyboard` |
| Clicked Timeline step button | `button` |
| `Run U F R F D B` | `sequence` |
| Console call or Developer Test send | `external` |

The second `F` behavior is preserved. The first contextual `F` maps to `BLOCK / GENERATE_BLOCK`; the second contextual `F` maps to `CLAY / ADD_CLAY_SHELL`. Clicking the two Timeline `F` buttons also routes through `receiveMove` while preserving their explicit target stage.

### Event Shape

Every accepted move now records:

```json
{
  "step": 1,
  "move": "U",
  "face": "UP",
  "stage": "SELECT",
  "command": "SELECT_MODULE",
  "output": "Module selected",
  "timestamp": 1710000000000,
  "source": "keyboard"
}
```

`source` can be `keyboard`, `button`, `sequence`, or `external`.

### Console Test

Open the demo file, then run this in the browser console:

```js
window.RubikFlowAgent.receiveMove("R")
```

Expected result:

- The overlay moves to `LOGIC / UPGRADE_LOGIC`.
- The Output Preview shows the logic network state.
- The Event Log records an event with `source: "external"`.

To inspect events:

```js
window.RubikFlowAgent.getEvents()
```

To inspect current state:

```js
window.RubikFlowAgent.getState()
```

### Developer Test Area

The Overlay bottom now includes a small Developer Test area:

```text
Console test: window.RubikFlowAgent.receiveMove("R")
```

Use the input to enter `U`, `F`, `R`, `D`, or `B`, then click `Send Move`. This simulates a future csTimer-internal move event by calling the same public event entry. It intentionally does not connect to real Bluetooth hardware.

### Next Stage: Real csTimer Move Event / Smart Cube Event

The next implementation stage should keep this API stable and replace the mock input source with real csTimer-originated move events:

1. Keep keyboard and Developer Test input as debug fallbacks.
2. Listen near csTimer's smart cube systems such as `GiikerCube`, `giikerutil`, and `timer.giiker`.
3. Normalize real move notation into `U / F / R / D / B` families before calling `window.RubikFlowAgent.receiveMove(move)`.
4. Preserve the event object shape, especially `source`, so recorded sessions stay replayable.
5. Only after this adapter proves stable, promote the logic into a real `src/js/tools/rubikflow.js` tool module.

## Next Stage: Real csTimer Page

There are two practical paths for connecting this to the real csTimer page later.

### Option A: Local PHP Server

Run csTimer through a local server that can execute PHP, then load the real `timer.php` page from `http://localhost/...`.

The RubikFlow overlay can then be injected as:

- A userscript.
- A browser dev overlay.
- A separate local HTML wrapper that iframes the served csTimer page.

This keeps the first integration reversible while allowing real csTimer behavior.

### Option B: Source Tool Plugin

Promote the overlay logic into:

```text
src/js/tools/rubikflow.js
```

Then register it through csTimer's existing tool system:

```text
tools.regTool(...)
kernel.regListener(...)
kernel.regProp(...)
```

This is the cleaner long-term integration path, but it should happen after the overlay behavior and move mapping are stable.

## Next Stage: Real Smart Cube Events

The real smart cube integration should not start from raw Web Bluetooth code. csTimer already has smart cube infrastructure. The RubikFlow plugin should listen near these existing systems:

- `src/js/tools/bluetoothutil.js`
- `src/js/timer/giiker.js`
- `src/js/hardware/bluetooth.js`
- `GiikerCube` callbacks
- `kernel` signals such as `time`, `timestd`, `timerStatus`, `scramble`, and `giirecons`

The intended flow is:

```text
Smart cube hardware
-> csTimer smart cube driver
-> normalized cube move
-> RubikFlow command mapper
-> Overlay / Web Mock / Blender / WebGL bridge
```
