# RubikFlow Agent Web Mock

This folder contains a single-file HTML front-end draft for RubikFlow Agent.

## Purpose

- Define the RubikFlow Agent UI structure before rebuilding it in Blender, WebGL, or Three.js.
- Lock down the core visual language: cream background, rounded cards, soft colored workflow tiles, clear timeline, and readable output preview.
- Show the three key workflow states: `LOGIC`, `CLAY`, and `LOCK`.

## How To Open

Double-click:

```text
rubikflow_web_mock.html
```

No build step, server, CDN, database, or external asset is required.

The mock is designed for a 1920 x 1080 browser window with no page scrollbars. The `LOGIC`, `CLAY`, and `LOCK` buttons sit in the RubikFlow Agent header and switch the keyframe state without covering the metric cards.

## Layout Notes

- The page uses a fixed 16:9 app shell with left, center, right, and bottom timeline regions.
- The Smart Cube Input illustration is a CSS-only 2.5D input cube with a strict 3 x 3 `cubelet` top face, one low dark offset base layer, a contact shadow, and a contained `cube-arrow`. It avoids rear flaps, vertical side plates, and floating supports.
- The right column is a strict grid: metrics, Agent State, Agent Function Pipeline, then Output Preview. Output Preview stays in its own row and does not float over the pipeline.
- The CSS defines semantic layer tokens for background, panels, content, cube body, arrows, highlights, text, and overlays. Text and state labels stay above highlights, while Output Preview elements are clipped inside their card.

## Future Use

Use this HTML mock as a visual and layout reference for:

- a cleaner Blender recreation
- a WebGL / Three.js interactive prototype
- future smart-cube input integration
- future Agent-driven block / clay / voxel / print workflows
