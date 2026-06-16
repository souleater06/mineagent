# RubikFlow Agent

一句话简介：RubikFlow Agent 是一个把智能魔方动作映射为 AI 工作流命令的交互原型，用实体旋转输入驱动可视化、可组合、可生成、可打印的 Agent 流程。

当前项目处于 **Demo / MVP** 阶段，包含两个互补部分：

- `01_RubikFlow_Blender_WebMock`：负责产品视觉、Web Mock、Blender / WebGL 方向参考。
- `02_csTimer_RubikFlow_Plugin`：负责智能魔方输入端、csTimer Plugin MVP、动作事件模拟。

## 核心链路

RubikFlow Agent 想验证的核心方向是：魔方动作不仅是计时或游戏输入，也可以成为 AI 工作流的实体控制器。

```text
Smart Cube
-> csTimer Input
-> RubikFlow Agent
-> Workflow-o-pedia
-> Output Preview
-> Blender / WebGL / 3D Printable Result
```

当前原型中，完整动作序列为：

```text
U -> F -> R -> F -> D -> B
```

对应工作流阶段为：

```text
SELECT -> BLOCK -> LOGIC -> CLAY -> LOCK -> PRINT
```

## 项目结构

```text
RubikFlow-Agent/
├── README.md
├── 00_README_FOR_LEADER.md
├── 01_RubikFlow_Blender_WebMock/
│   ├── web/
│   │   ├── rubikflow_web_mock.html
│   │   └── README.md
│   ├── docs/
│   │   ├── REFERENCE_PROJECTS.md
│   │   ├── LAYOUT_REFACTOR_REPORT.md
│   │   └── RUBIKFLOW_BLENDER_WEBMOCK_AGENT_HANDOFF.md
│   ├── refs/
│   ├── rubikflow_agent_demo.py
│   ├── rubikflow_agent_clean_demo.py
│   ├── memorize.md
│   └── task.md
└── 02_csTimer_RubikFlow_Plugin/
    ├── experiment/
    │   └── rubikflow-overlay-demo.html
    └── docs/
        ├── RUBIKFLOW_CSTIMER_PLUGIN_PLAN.md
        ├── RUBIKFLOW_MEMORY_BRIEF.md
        ├── RUBIKFLOW_MVP_REPORT.md
        └── RUBIKFLOW_PLUGIN_AGENT_HANDOFF.md
```

## 两个部分分别是什么

### 1. RubikFlow Blender / Web Mock

路径：

```text
01_RubikFlow_Blender_WebMock/
```

这个部分是 RubikFlow Agent 的视觉原型和 Blender / WebGL 参考项目，重点展示产品界面、工作流状态和输出预览。

主要内容包括：

- Smart Cube Input
- Active Face On Top
- Cube Command Lens
- Workflow-o-pedia
- Agent State
- Agent Function Pipeline
- Output Preview
- Workflow Timeline
- LOGIC / CLAY / LOCK 三个关键视觉状态

当前最稳定、最适合展示的文件是：

```text
01_RubikFlow_Blender_WebMock/web/rubikflow_web_mock.html
```

Blender Python Demo 已经验证过部分视觉方向，但当前仍存在布局、文字重叠和可读性问题。因此，现阶段建议以 Web Mock 作为视觉标准，后续再反向指导 Blender / WebGL / Three.js 重构。

### 2. csTimer RubikFlow Plugin MVP

路径：

```text
02_csTimer_RubikFlow_Plugin/
```

这个部分是 RubikFlow Agent 的输入端原型，用于探索如何让 csTimer 成为智能魔方动作输入的 host，并把 move event 转换成 RubikFlow Agent 的 workflow event。

主要链路是：

```text
Smart Cube Move / Keyboard Move
-> csTimer Input Layer
-> RubikFlow Agent Overlay
-> Workflow Event
-> Output Preview
-> JSON Export
```

当前主要 demo 文件是：

```text
02_csTimer_RubikFlow_Plugin/experiment/rubikflow-overlay-demo.html
```

该 demo 左侧是 csTimer mock 页面，右侧是 RubikFlow Agent Overlay，可通过键盘动作或 Run Sequence 模拟完整工作流。

## 快速打开方式

### 查看产品视觉原型

直接用浏览器打开：

```text
01_RubikFlow_Blender_WebMock/web/rubikflow_web_mock.html
```

该文件是单文件 HTML，不需要安装依赖，也不需要启动服务器。

### 查看 csTimer Plugin MVP

直接用浏览器打开：

```text
02_csTimer_RubikFlow_Plugin/experiment/rubikflow-overlay-demo.html
```

打开后可以按键盘测试：

```text
U F R F D B
```

也可以点击页面中的 `Run Sequence` 自动执行完整流程。

## 当前功能

### Web Mock 已完成内容

- 展示 RubikFlow Agent 产品界面草稿。
- 展示 Smart Cube Input 与当前 move。
- 展示 Workflow-o-pedia 的 tile 体系。
- 展示 Agent State、Agent Function Pipeline 和 Output Preview。
- 支持 SELECT / BLOCK / LOGIC / CLAY / LOCK / PRINT 的 Timeline 表达。
- 对齐 LOGIC、CLAY、LOCK 三个关键输出状态。

### csTimer Plugin MVP 已完成内容

- 提供 csTimer mock 页面。
- 提供 RubikFlow Agent Overlay。
- 支持键盘输入 `U / F / R / D / B`。
- 支持 `Run Sequence` 和 `Reset`。
- 记录 Event Log。
- 支持 Export JSON。
- 根据输入动作更新 Workflow Stage。
- 支持第二次 `F` 识别为 `CLAY / ADD_CLAY_SHELL`。

## JSON / CSV Export Interface

两个网页端 demo 都提供统一的全局导出接口，方便后续给组长、Agent 或外部程序读取工作流事件数据。

支持页面：

- `01_RubikFlow_Blender_WebMock/web/rubikflow_web_mock.html`
- `02_csTimer_RubikFlow_Plugin/experiment/rubikflow-overlay-demo.html`

全局接口：

```js
window.RubikFlowAgent.getState()
window.RubikFlowAgent.getEvents()
window.RubikFlowAgent.exportJSON()
window.RubikFlowAgent.exportCSV()
window.RubikFlowAgent.downloadJSON()
window.RubikFlowAgent.downloadCSV()
```

导出文件：

- `downloadJSON()` 下载 `rubikflow-events.json`
- `downloadCSV()` 下载 `rubikflow-events.csv`

事件字段：

```text
index,timestamp,move,face,workflowStage,triggeredTile,agentCommand,result,outputState,source
```

JSON 顶层结构：

```json
{
  "project": "我的世界agent",
  "type": "rubikflow-workflow-events",
  "version": "0.1.0",
  "generatedAt": "ISO time",
  "currentState": {},
  "events": []
}
```

页面内均提供 `Export JSON` 和 `Export CSV` 按钮；两个 demo 都不需要后端、数据库或 npm 依赖，双击 HTML 文件即可测试。

## 工作流映射表

| Cube Move | Stage | Agent Command | 含义 |
| --- | --- | --- | --- |
| U | SELECT | SELECT_MODULE | 选择工作流模块 |
| F | BLOCK | GENERATE_BLOCK | 生成基础方块 |
| R | LOGIC | UPGRADE_LOGIC | 构建类似红石逻辑的节点与信号线 |
| F | CLAY | ADD_CLAY_SHELL | 添加粘土 / 体素外壳 |
| D | LOCK | CONFIRM_LOCK | 确认并锁定结构 |
| B | PRINT | PREPARE_PRINT | 准备 3D 打印输出 |

完整 Timeline：

```text
SELECT -> BLOCK -> LOGIC -> CLAY -> LOCK -> PRINT
```

## 当前限制

### Web Mock 限制

- 当前仍是 HTML 原型，不是正式 WebGL / Three.js 版本。
- Smart Cube Input 的 3x3 魔方视觉仍可继续优化。
- 不同状态下的图层、覆盖关系和响应式表现仍需检查。
- 尚未接入真实智能魔方输入。

### Blender Demo 限制

- 复杂 UI 在 Blender 中容易出现文字与面板重叠。
- 当前 Blender Demo 不建议作为最终展示版本。
- 更建议先以 Web Mock 固化界面与交互标准，再重建 Blender / WebGL 版本。

### csTimer Plugin 限制

- 当前左侧仍是 csTimer mock，不是真实 `timer.php`。
- 尚未接入 csTimer 内部真实 move event。
- 尚未接入真实蓝牙智能魔方。
- 当前仍是 experiment demo，不是正式 csTimer plugin。

## 后续路线

1. 继续优化 Web Mock 的 Smart Cube Input、Output Preview 和关键状态视觉。
2. 抽象统一事件接口，例如 `window.RubikFlowAgent.receiveMove(move)`。
3. 将键盘输入、按钮点击、Run Sequence、csTimer move event 和 smart cube event 统一到同一套事件入口。
4. 接入真实 csTimer move event。
5. 接入真实蓝牙智能魔方事件。
6. 基于 Web Mock 视觉标准重建 WebGL / Three.js 或稳定版 Blender 展示。
7. 将 Output Preview 从静态视觉原型推进到可构建、可导出、可打印的结果表达。

## 交接文档位置

### Blender / Web Mock 交接文档

```text
01_RubikFlow_Blender_WebMock/docs/RUBIKFLOW_BLENDER_WEBMOCK_AGENT_HANDOFF.md
```

用于说明 RubikFlow / Blender / Web Mock 侧的项目上下文、当前状态和后续开发建议。

### csTimer Plugin 交接文档

```text
02_csTimer_RubikFlow_Plugin/docs/RUBIKFLOW_PLUGIN_AGENT_HANDOFF.md
```

用于说明 csTimer Plugin MVP 的项目上下文、事件映射、当前功能和后续集成方向。

## 当前结论

RubikFlow Agent 当前最重要的验证结果是：魔方动作可以被映射成 Agent 工作流命令。

本项目不是普通计时器，也不是普通魔方游戏；它的重点是用智能魔方作为实体输入设备，驱动一个可视化、可组合、可生成、可打印的 Agent 工作流。

当前最稳定的展示入口是：

```text
01_RubikFlow_Blender_WebMock/web/rubikflow_web_mock.html
```

当前最重要的输入端 MVP 是：

```text
02_csTimer_RubikFlow_Plugin/experiment/rubikflow-overlay-demo.html
```



#魔方智能觉醒（* *）
---

《魔方循环》完整上下文摘要（更新版）


好，接上。简洁直给：

---

克里斯走出咖啡馆，阳光照在脸上。他手插口袋，魔方在口袋里。他走了大概二十步，口袋里传来极其细微的震动——不是手机，是魔方在转。他停下，把魔方掏出来。魔方在他掌心里自己转了一格，然后停了。他低头看那一格——蓝色的那一面，转到了正上方。他不记得自己拧过这一面。他回到咖啡馆，把设备重新打开，调出刚才跑完的模型日志。日志最后一行显示的不是测试结果，而是一段预测文本，时间戳是：三分钟前。内容只有一句话：“你今天会回去。”他盯着那句话看了很久。然后他敲了一行命令：模型是否能生成时间维度的操作界面。设备沉默了两秒。屏幕上弹出一个新的窗口。窗口里是一张地图，地图上有一个坐标，坐标位置就是昨天黄昏他坐着的那个路沿。窗口旁边有一个滑动条，标注着“时间偏移量”。他把滑动条往回拉了一格——代表大约十五小时。地图没变，但窗口角落里跳出一行字：“目标时间窗口已锁定。是否执行？”他的手指在键盘上停了五秒。然后他按下回车。

设备发出低频的嗡鸣，像什么内部系统在重新校准。屏幕上的地图开始模糊，像水彩被水冲开。他眼前的咖啡馆在变淡——不是消失，是像画纸被一层层剥离。三秒后他发现自己蹲在昨天的路沿旁边，手里拿着设备，身边放着一个银白色外壳。他抬头。路灯亮着。街上没有人。然后他看见——前面五米处，有一个男人坐在路沿上，低着头，旁边放着一台银白色设备。那是昨天的自己。而在那个“昨天的自己”面前，蹲着一个穿深色外套、帽檐压低的人，正伸出手——手里托着一个魔方。克里斯站起来，走过去。那个递魔方的人没有抬头，没有转身。克里斯走到他身边，蹲下。他说：“我来拿回那个魔方。”递魔方的手停住了。那只手悬在空中，魔方还托在掌心。帽檐下方传来一个声音，很轻，像嗓子很久没用过：“你确定？”克里斯说：“我确定。”那人把魔方收回去，又递出来——递向克里斯。克里斯伸手接住。指尖碰到魔方的瞬间，那个穿深色外套的人消失了。就像没存在过。克里斯蹲在原地，手里握着魔方。他侧头看向“昨天的自己”——那个自己还在低头看设备，完全没有注意到旁边发生了什么。克里斯站起来，退了两步，退回路灯照不到的阴影里。他没有回到未来。他只是在阴影里站了很久，看着昨天的自己坐在那里，然后被另一个自己递出魔方，然后茫然地接过去。他看着昨天的自己开始转魔方，看着昨天的自己停下来，看着昨天的自己眼睛亮起来——然后他看着昨天的自己猛地站起来，蹲下打开设备，开始改代码。

克里斯在阴影里蹲下，低头看手里的魔方。魔方没有转。完全静止。他把魔方收进口袋。他知道现在口袋里有两个魔方——一个是刚才拿回来的，一个是他在昨天那个时间线上还没被“递出”的。他不知道自己该保留哪一个。他也不知道他刚才从谁手里接回了魔方。那个穿深色外套的人没有脸。或者说，他没有记住脸。他只知道刚才那句话是他的声音。“你确定？”——那是他自己的声音。他坐回阴影里，关掉设备屏幕。他没有选择回到“现在”的时间点。他选择留在这一夜的阴影里，等到天亮。等到昨天的自己站起来走进咖啡馆，等到阳光照亮街道。然后他会站起来，走到下一个街角，遇到下一个人——然后从口袋里掏出一个魔方，递过去。他会在帽檐下压低声音说：“试试看。”

他知道那个人会接过去。他知道那个人会转。他知道那个人会调通。他知道那个人会回来。他已经回来了。他现在要做的就是递出去。

天亮之前，他在阴影里坐着，手里握着一个魔方，口袋里还有一个。两个都是真的。两个都在等他选择哪一个递出去。他低头看手里的魔方——表面有一格蓝色，在黑暗中发着极其微弱的光。他把那个魔方放回口袋，然后从口袋里拿出另一个。

这一个没有发光。只是一个普通魔方。褪色的、旧旧的、边角磨损的。像在街上被人递过很多次。他握紧它，站起来，走出阴影。路灯在六点整熄灭。街道开始有人走动。克里斯站在路口，手里握着一个褪色的魔方。

他看到一个人走过来——年轻、疲倦、手里拎着一个银白色的设备。克里斯没有犹豫。他蹲下身，把魔方递了出去。

那个人停下了。
---时间线收束

全篇完成。闭环。
