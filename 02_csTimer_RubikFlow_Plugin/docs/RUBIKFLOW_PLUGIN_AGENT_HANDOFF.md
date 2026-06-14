# RubikFlow csTimer Plugin Agent Handoff

## 1. Project Positioning

This csTimer repository is being used as the host for a RubikFlow Agent plugin prototype.

The product direction is:

```text
Cube move -> csTimer input surface -> RubikFlow workflow command -> visual / Agent / output pipeline
```

In this direction, csTimer is not just a speedcubing timer. It becomes the smart cube action input endpoint and workflow trigger. RubikFlow Agent is the overlay / plugin layer that interprets cube moves as workflow commands.

This handoff is for the csTimer-side plugin work only.

## 2. Current Demo Path

Runnable demo file:

```text
D:\codex-work\cstimer-plugin-dev\cstimer\experiment\rubikflow-overlay-demo.html
```

Relative path:

```text
experiment/rubikflow-overlay-demo.html
```

The demo is a standalone static HTML file and can be opened directly from disk.

## 3. Current MVP Functions

The current overlay demo includes:

- Left side: static csTimer mock page.
- Right side: RubikFlow Agent Overlay.
- Keyboard input for `U / F / R / D / B`.
- Clickable workflow Timeline buttons.
- `Run U F R F D B` sequence button.
- `Reset`.
- Event Log.
- `Export JSON`.
- Output Preview.
- Context-aware second `F`, mapped to `CLAY / ADD_CLAY_SHELL`.

The left csTimer area is intentionally a mock. It exists to communicate where the original timer surface will remain while the RubikFlow plugin runs as an overlay / tool panel.

## 4. U / F / R / F / D / B Mapping

Initial deterministic demo sequence:

```text
U -> F -> R -> F -> D -> B
```

Mapping:

| Move | Workflow Stage | Agent Command | Meaning |
| --- | --- | --- | --- |
| `U` | `SELECT` | `SELECT_MODULE` | Select a workflow module / starting node. |
| first `F` | `BLOCK` | `GENERATE_BLOCK` | Generate the base block. |
| `R` | `LOGIC` | `UPGRADE_LOGIC` | Add logic lines / structure upgrade. |
| second `F` | `CLAY` | `ADD_CLAY_SHELL` | Add clay / voxel shell. |
| `D` | `LOCK` | `CONFIRM_LOCK` | Confirm and lock the workflow node. |
| `B` | `PRINT` | `PREPARE_PRINT` | Prepare print / export state. |

Important behavior: the second `F` is contextual. It must not repeat `GENERATE_BLOCK`; after the workflow has progressed through `U F R`, the next `F` means `CLAY / ADD_CLAY_SHELL`.

## 5. How To Open And Test

Open:

```text
D:\codex-work\cstimer-plugin-dev\cstimer\experiment\rubikflow-overlay-demo.html
```

Recommended test:

1. Double-click the HTML file.
2. Click anywhere on the page so it has focus.
3. Press `U`.
4. Press `F`.
5. Press `R`.
6. Press `F`.
7. Press `D`.
8. Press `B`.

Alternative test:

- Click `Run U F R F D B`.

Expected result:

- Timeline advances through `SELECT -> BLOCK -> LOGIC -> CLAY -> LOCK -> PRINT`.
- Output Preview changes state as the workflow advances.
- Event Log records each move.
- `Export JSON` exports the workflow event array.

No build step is needed for this demo because it is a single static HTML file.

## 6. Current Limitations

- No real Bluetooth smart cube is connected.
- No real csTimer move event is connected yet.
- The left side is a csTimer mock, not real `timer.php`.
- This is an overlay MVP, not the formally integrated csTimer plugin.
- No `src`, `dist`, or `lib` integration should be attempted at this checkpoint.
- No external CDN, database, or backend service is required for the current demo.

## 7. Relationship To `D:\codex-blender\rubikflow-agent`

`D:\codex-blender\rubikflow-agent` is the separate RubikFlow Agent / Blender-side project context. It contains the broader product direction and creative workflow ideas.

For this csTimer plugin project:

- Treat that project as upstream product context only.
- Do not modify files in `D:\codex-blender\rubikflow-agent` from this repository.
- Do not continue building a standalone Blender demo here.
- Keep csTimer as the host and move-input endpoint.
- Future Blender / WebGL / Web Mock work should consume structured events emitted from the csTimer plugin, not be mixed directly into csTimer source during this MVP stage.

## 8. Next Step: MVP 4 `window.RubikFlowAgent` API

The next engineering step is MVP 4: abstract the demo input path into a public event adapter that future csTimer and smart cube events can call.

Target API:

```js
window.RubikFlowAgent.receiveMove(move)
window.RubikFlowAgent.getEvents()
window.RubikFlowAgent.getState()
window.RubikFlowAgent.reset()
window.RubikFlowAgent.runSequence()
window.RubikFlowAgent.exportEvents()
```

Expected design:

- Keyboard input calls `receiveMove(move)`.
- Timeline button clicks call `receiveMove(move)`.
- `Run Sequence` calls `receiveMove(move)` for each move.
- Future real csTimer move events call the same `receiveMove(move)`.
- Event objects should remain structured and replayable.
- Event `source` should distinguish keyboard, button, sequence, and future external/csTimer events.

The goal is to make the overlay a plugin-shaped adapter before touching real csTimer internals.

## 9. Explicit Scope Guard

Do not involve AuthentiX.

Do not mention, integrate, modify, or design around AuthentiX in this csTimer RubikFlow plugin work.

Also do not:

- Connect a real Bluetooth cube yet.
- Modify the RubikFlow Blender project.
- Modify csTimer `src`, `dist`, or `lib` for the current handoff step.
- Replace the static HTML demo with a real PHP-backed csTimer runtime before the overlay adapter is stable.
