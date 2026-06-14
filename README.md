# 我的世界agent

> A smart-cube-driven Agent workflow prototype.  
> 一个用“智能魔方动作”驱动 Agent 工作流的原型项目。

我的世界agent 的目标是让实体魔方不只是玩具，而是成为 AI 工作流、可视化建模和可打印输出的控制器。

---

## 1. Project Overview / 项目简介

我的世界agent explores a new interaction model:

```text
Smart Cube Move
-> csTimer Input
-> RubikFlow Agent
-> Workflow Timeline
-> Output Preview
-> Buildable / Printable Result
```

传统交互通常是：

```text
Mouse Click -> Software Command
鼠标点击 -> 软件执行命令
```

我的世界agent 希望实现：

```text
Smart Cube Rotation -> Workflow Tile -> Agent Command -> Visual Output
智能魔方转动 -> 工作流模块 -> Agent 命令 -> 可视化输出
```

用户通过转动魔方，例如 `U / F / R / F / D / B`，触发不同的工作流阶段，让 Agent 根据动作执行对应任务。

---

## 2. Core Workflow / 核心工作流

当前工作流被设计为 6 个阶段：

```text
SELECT -> BLOCK -> LOGIC -> CLAY -> LOCK -> PRINT
```

| Stage | 中文含义 | Description |
|---|---|---|
| SELECT | 选择模块 | Select a workflow module |
| BLOCK | 生成方块 | Generate a base block |
| LOGIC | 构建逻辑 | Add redstone-like logic nodes and signal lines |
| CLAY | 添加外壳 | Add clay / voxel shell |
| LOCK | 锁定结构 | Validate and lock the structure |
| PRINT | 准备打印 | Prepare printable output |

---

## 3. Repository Structure / 项目结构

```text
我的世界agent/
├─ 01_RubikFlow_Blender_WebMock/
├─ 02_csTimer_RubikFlow_Plugin/
├─ 00_README_FOR_LEADER.md
└─ README.md
```

| Folder / File | 中文说明 | English Description |
|---|---|---|
| `01_RubikFlow_Blender_WebMock` | RubikFlow 视觉原型、Blender Demo、Web Mock、WebGL 参考 | Visual prototype, Blender demo, Web Mock and WebGL direction |
| `02_csTimer_RubikFlow_Plugin` | csTimer 插件 MVP，用于模拟智能魔方输入和工作流触发 | csTimer plugin MVP for smart cube input and workflow triggering |
| `00_README_FOR_LEADER.md` | 项目快速说明 | Quick project summary |
| `README.md` | GitHub 首页项目说明 | Main GitHub project README |

---

# Part 1: RubikFlow Blender / Web Mock

## 4. Main Path / 主要路径

```text
01_RubikFlow_Blender_WebMock/
```

## 5. Recommended Demo / 推荐打开文件

```text
01_RubikFlow_Blender_WebMock/web/rubikflow_web_mock.html
```

Open method / 打开方式：

```text
Double-click rubikflow_web_mock.html
直接双击 rubikflow_web_mock.html
```

This HTML file is currently the most stable visual prototype.  
这个 HTML 文件是当前最稳定的前端视觉原型。

It can be opened directly in a browser without installing dependencies or running a server.  
它可以直接用浏览器打开，不需要安装依赖，也不需要启动服务器。

---

## 6. Current Web Mock Features / Web Mock 当前功能

The Web Mock currently includes:

当前 Web Mock 包含：

- Smart Cube Input / 智能魔方输入区
- `U / F / R / F / D / B` move sequence / 魔方动作步骤条
- Active Face On Top / 当前激活面
- Cube Command Lens / 魔方命令透镜
- RubikFlow Agent title area / RubikFlow Agent 标题区
- Workflow-o-pedia / 工作流模块库
- Agent State / Agent 状态
- Agent Function Pipeline / Agent 功能管线
- Output Preview / 输出预览
- Workflow Timeline / 工作流时间线
- LOGIC / CLAY / LOCK key visual states / 三个关键视觉状态

---

## 7. Web Mock Layout / Web Mock 四区布局

| Area | 中文说明 | English Description |
|---|---|---|
| Left: Smart Cube Input | 左侧智能魔方输入区，展示当前 move、Active Face 和 Cube Command Lens | Simulates smart cube input and current move |
| Middle: RubikFlow Agent / Workflow-o-pedia | 中间工作流区，展示 20 个 workflow tile 和触发命令 | Shows workflow tiles and triggered command |
| Right: Agent State / Pipeline / Output Preview | 右侧状态和输出区，展示 Agent 执行状态和视觉结果 | Shows agent status and visual output |
| Bottom: Workflow Timeline | 底部时间线，展示完整工作流进度 | Shows full workflow progress |

---

## 8. Workflow-o-pedia Modules / 工作流模块

Workflow-o-pedia currently includes 20 workflow modules:

Workflow-o-pedia 当前包含 20 个工作流模块：

```text
BLOCK
CLAY
VOXEL
JOINT
MIRROR
SCALE
COLOR
SCAN
AGENT
PRINT
EXPORT
SHELL
HOLLOW
STACK
LOCK
LOOP
CHECK
FIX
BUILD
SAVE
```

These tiles represent different functional modules that the Agent can trigger.  
这些 tile 表示 Agent 可以触发的不同功能模块。

---

# Part 2: csTimer RubikFlow Plugin MVP

## 9. Main Path / 主要路径

```text
02_csTimer_RubikFlow_Plugin/
```

## 10. Recommended Demo / 推荐打开文件

```text
02_csTimer_RubikFlow_Plugin/experiment/rubikflow-overlay-demo.html
```

Open method / 打开方式：

```text
Double-click rubikflow-overlay-demo.html
直接双击 rubikflow-overlay-demo.html
```

This demo is a standalone HTML prototype.  
该 demo 是一个单文件 HTML 原型，可以直接在浏览器中打开。

The left side is a csTimer mock page, and the right side is a RubikFlow Agent Overlay.  
左侧是 csTimer mock 页面，右侧是 RubikFlow Agent Overlay。

---

## 11. Current Plugin MVP Features / 插件 MVP 当前功能

The current csTimer plugin MVP includes:

当前 csTimer 插件 MVP 包含：

- Static csTimer mock page / 静态 csTimer 模拟页面
- RubikFlow Agent overlay / RubikFlow Agent 浮层
- Keyboard input: `U / F / R / D / B` / 键盘输入模拟魔方动作
- Run Sequence / 自动运行完整序列
- Reset / 重置
- Event Log / 事件日志
- Export JSON / 导出 JSON
- Output Preview / 输出预览
- Workflow stage switching / 工作流阶段切换
- The second `F` move is mapped to `CLAY / ADD_CLAY_SHELL` / 第二次 `F` 会映射到 CLAY 阶段

---

## 12. How To Test / 如何测试

Open this file:

打开这个文件：

```text
02_csTimer_RubikFlow_Plugin/experiment/rubikflow-overlay-demo.html
```

Then press these keyboard keys:

然后按键盘测试：

| Key | Stage | Agent Command | 中文说明 |
|---|---|---|---|
| U | SELECT | SELECT_MODULE | 选择工作流模块 |
| F | BLOCK | GENERATE_BLOCK | 生成基础方块 |
| R | LOGIC | UPGRADE_LOGIC | 构建逻辑网络 |
| F | CLAY | ADD_CLAY_SHELL | 添加粘土 / 体素外壳 |
| D | LOCK | CONFIRM_LOCK | 确认并锁定结构 |
| B | PRINT | PREPARE_PRINT | 准备打印输出 |

You can also click:

也可以点击：

```text
Run U F R F D B
```

to automatically run the full sequence.  
自动执行完整序列。

---

# 13. Move Mapping / 动作映射

| Cube Move | Stage | Agent Command | Meaning | 中文说明 |
|---|---|---|---|---|
| U | SELECT | SELECT_MODULE | Select a workflow module | 选择工作流模块 |
| F | BLOCK | GENERATE_BLOCK | Generate a base block | 生成基础方块 |
| R | LOGIC | UPGRADE_LOGIC | Build a logic network | 构建逻辑网络 |
| F | CLAY | ADD_CLAY_SHELL | Add clay / voxel shell | 添加粘土 / 体素外壳 |
| D | LOCK | CONFIRM_LOCK | Confirm and lock the structure | 确认并锁定结构 |
| B | PRINT | PREPARE_PRINT | Prepare printable output | 准备打印输出 |

Full sequence / 完整序列：

```text
U -> F -> R -> F -> D -> B
```

Corresponding workflow / 对应工作流：

```text
SELECT -> BLOCK -> LOGIC -> CLAY -> LOCK -> PRINT
```

---

# 14. Key Visual States / 关键视觉状态

## LOGIC / R Stage

```text
Move: R
Active Face: R FACE
Workflow Tile: JOINT
Agent Command: UPGRADE LOGIC
Result: ACTIVE
```

Output Preview:

```text
Grey base + red signal lines + logic nodes
灰色底板 + 红色信号线 + 逻辑节点
```

Meaning:

```text
The R move triggers the LOGIC stage.
The Agent upgrades the structure with redstone-like logic connections.

用户转动 R 面，触发 LOGIC 阶段。
Agent 会增加类似红石逻辑的连接和节点。
```

---

## CLAY / F Stage

```text
Move: F
Active Face: F FACE
Workflow Tile: CLAY
Agent Command: ADD CLAY
Result: BUILDING
```

Output Preview:

```text
Orange clay / voxel shell
橙色粘土 / 体素外壳
```

Meaning:

```text
The second F move triggers the CLAY stage.
The Agent adds a clay or voxel shell to the structure.

用户第二次转动 F 面，触发 CLAY 阶段。
Agent 会为结构添加粘土外壳或体素壳体。
```

---

## LOCK / D Stage

```text
Move: D
Active Face: D FACE
Workflow Tile: LOCK
Agent Command: CONFIRM LOCK
Result: LOCKED
```

Output Preview:

```text
Lock icons / confirmed shell / locked state
锁定图标 / 确认外壳 / 已锁定状态
```

Meaning:

```text
The D move triggers the LOCK stage.
The Agent validates and locks the structure.

用户转动 D 面，触发 LOCK 阶段。
Agent 会验证并锁定当前结构。
```

---

# 15. Important Files / 重要文件

## RubikFlow Blender / Web Mock

```text
01_RubikFlow_Blender_WebMock/
├─ web/
│  ├─ rubikflow_web_mock.html
│  └─ README.md
├─ docs/
│  ├─ REFERENCE_PROJECTS.md
│  ├─ LAYOUT_REFACTOR_REPORT.md
│  └─ RUBIKFLOW_BLENDER_WEBMOCK_AGENT_HANDOFF.md
├─ refs/
├─ renders/
├─ memorize.md
├─ task.md
├─ README.md
├─ rubikflow_agent_demo.py
└─ rubikflow_agent_clean_demo.py
```

| File | 中文说明 | English Description |
|---|---|---|
| `memorize.md` | RubikFlow Agent 的核心记忆文件 | Core memory of the RubikFlow Agent concept |
| `web/rubikflow_web_mock.html` | 当前最稳定的视觉原型 | Main visual prototype |
| `web/README.md` | Web Mock 使用说明 | Web Mock usage guide |
| `rubikflow_agent_demo.py` | 早期 Blender Python Demo | Early Blender Python demo |
| `rubikflow_agent_clean_demo.py` | 后续清理版 Blender Demo | Later cleaned Blender demo attempt |
| `docs/REFERENCE_PROJECTS.md` | 参考项目和二创方向 | Reference projects and remix direction |
| `docs/LAYOUT_REFACTOR_REPORT.md` | 布局重构和视觉 Bugfix 记录 | Layout refactor and visual bugfix record |
| `docs/RUBIKFLOW_BLENDER_WEBMOCK_AGENT_HANDOFF.md` | Blender / Web Mock 交接文档 | Handoff document for Blender / Web Mock side |

---

## csTimer RubikFlow Plugin

```text
02_csTimer_RubikFlow_Plugin/
├─ experiment/
│  └─ rubikflow-overlay-demo.html
└─ docs/
   ├─ RUBIKFLOW_CSTIMER_PLUGIN_PLAN.md
   ├─ RUBIKFLOW_MEMORY_BRIEF.md
   ├─ RUBIKFLOW_MVP_REPORT.md
   └─ RUBIKFLOW_PLUGIN_AGENT_HANDOFF.md
```

| File | 中文说明 | English Description |
|---|---|---|
| `experiment/rubikflow-overlay-demo.html` | 当前插件 MVP demo | Main plugin MVP demo |
| `docs/RUBIKFLOW_CSTIMER_PLUGIN_PLAN.md` | 插件开发计划 | Plugin development plan |
| `docs/RUBIKFLOW_MEMORY_BRIEF.md` | 插件方向上下文简报 | Context brief for plugin direction |
| `docs/RUBIKFLOW_MVP_REPORT.md` | 当前 MVP 功能报告 | Current MVP report |
| `docs/RUBIKFLOW_PLUGIN_AGENT_HANDOFF.md` | 插件侧交接文档 | Handoff document for plugin side |

---

# 16. Current Status / 当前状态

Completed / 已完成：

- RubikFlow Agent product concept / 产品概念整理
- Web Mock visual prototype / Web Mock 前端草稿
- LOGIC / CLAY / LOCK key visual states / 三个关键视觉状态
- Blender Python demo exploration / Blender Python Demo 探索
- csTimer plugin MVP demo / csTimer 插件 MVP demo
- `U / F / R / F / D / B` workflow mapping / 工作流映射
- Event Log / 事件日志
- Export JSON / JSON 导出
- Two Agent handoff documents / 两份 Agent 交接文档

Not completed yet / 尚未完成：

- Real Bluetooth smart cube connection / 真实蓝牙智能魔方接入
- Real csTimer move event integration / csTimer 真实 move event 接入
- Official csTimer plugin integration / 正式 csTimer 插件集成
- WebGL / Three.js production version / WebGL 或 Three.js 正式版本
- Stable final Blender version / 稳定的 Blender 最终版本
- Backend / database / 后端或数据库

---

# 17. Current Limitations / 当前限制

## Web Mock

- Smart Cube Input visual still needs improvement.  
  Smart Cube Input 的 3×3 魔方视觉仍可继续优化。

- Layer and z-index issues should continue to be checked.  
  不同状态下仍需要继续检查图层覆盖问题。

- It is currently an HTML prototype, not a WebGL production version.  
  当前只是 HTML 原型，不是正式 WebGL。

- It does not use real smart cube input yet.  
  当前还没有真实智能魔方输入。

## Blender Demo

- Complex UI elements in Blender can overlap easily.  
  复杂 UI 在 Blender 中容易重叠。

- Some text and panels are still not stable enough.  
  部分文字和面板可读性仍不够稳定。

- The current Blender demo should not be treated as the final display version.  
  当前不建议把 Blender Demo 当最终展示版本。

- The Web Mock should be used as the main visual reference for future Blender / WebGL reconstruction.  
  后续更建议以 Web Mock 为标准重新构建 Blender / WebGL 版本。

## csTimer Plugin

- The left side is currently a csTimer mock, not the real `timer.php`.  
  当前左侧是 csTimer mock，不是真实 `timer.php`。

- Real csTimer internal move events are not connected yet.  
  当前还没有接入 csTimer 内部真实事件。

- Real Bluetooth smart cube input is not connected yet.  
  当前还没有接入真实蓝牙智能魔方。

- The current version is still an `experiment/` demo, not a formal plugin.  
  当前仍是 `experiment/` demo，不是正式插件。

---

# 18. Recommended Next Steps / 后续路线

## Web Mock Direction

Continue improving / 继续优化：

```text
01_RubikFlow_Blender_WebMock/web/rubikflow_web_mock.html
```

Focus / 重点：

- Improve the 3×3 Smart Cube Input visual.  
  优化 Smart Cube Input 中的 3×3 智能魔方视觉。

- Stabilize LOGIC / CLAY / LOCK visual states.  
  稳定 LOGIC / CLAY / LOCK 三个视觉状态。

- Check all z-index and layer issues.  
  检查所有 z-index 和图层覆盖问题。

- Keep the layout readable at 1920×1080.  
  保持 1920×1080 下清晰可读。

- Later rebuild it with WebGL / Three.js or use it as a Blender reconstruction reference.  
  后续可以拆成 WebGL / Three.js，或作为 Blender 重构参考。

---

## csTimer Plugin Direction

Continue to MVP 4 and abstract a unified API:

继续推进 MVP 4，抽象统一事件接口：

```js
window.RubikFlowAgent.receiveMove(move)
window.RubikFlowAgent.runSequence()
window.RubikFlowAgent.reset()
window.RubikFlowAgent.getEvents()
window.RubikFlowAgent.getState()
window.RubikFlowAgent.exportEvents()
```

Goal / 目标：

```text
Keyboard input
Button click
Run Sequence
Future csTimer move event
Future Bluetooth smart cube event

键盘输入
按钮点击
自动序列
未来 csTimer move event
未来蓝牙智能魔方事件
```

Unified entry / 统一入口：

```js
window.RubikFlowAgent.receiveMove(move)
```

---

# 19. Handoff Documents / 交接文档

Blender / Web Mock handoff:

Blender / Web Mock 侧交接文档：

```text
01_RubikFlow_Blender_WebMock/docs/RUBIKFLOW_BLENDER_WEBMOCK_AGENT_HANDOFF.md
```

csTimer Plugin handoff:

csTimer 插件侧交接文档：

```text
02_csTimer_RubikFlow_Plugin/docs/RUBIKFLOW_PLUGIN_AGENT_HANDOFF.md
```

These two documents are intended for future Agents to quickly understand the project context.

这两份文档用于帮助后续 Agent 快速理解项目上下文。

---

# 20. Final Summary / 最终总结

我的世界agent is an early MVP prototype.

我的世界agent 当前是一个早期 MVP 原型。

It has already verified one key idea:

它已经验证了一个核心方向：

```text
Cube moves can be mapped into Agent workflow commands.
魔方动作可以被映射成 Agent 工作流命令。
```

This project is not just a timer, not just a cube game, and not just a static UI mockup.

这个项目不是普通计时器，不是普通魔方游戏，也不是单纯的静态 UI 草稿。

It is an exploration of a physical, programmable, visual Agent workflow system controlled by smart cube moves.

它探索的是一种由智能魔方动作控制的、实体化的、可编程的、可视化的 Agent 工作流系统。
