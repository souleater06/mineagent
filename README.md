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

《魔方》完整上下文摘要（更新版）

一、故事主线

木叶村一名酷似少年鸣人的青涩忍者捡到一个普通魔方，却发现其中蕴藏不祥力量。少年手持魔方时，被远处开启写轮眼的宇智波斑凝视窥探，感受到压迫。

魔方失控震动，少年回忆其来自某位师傅的“不言之教”，是一颗名为“界核”的蓝色发光球体。

魔方脱手飞出窗外，引发多名忍者激烈争夺，呈现黑白单色剪影风格（类似《青鸟》MV），灯光快速闪现不同颜色，形成定格关键帧。

争夺中，魔方被弹飞，落入该少年手中，争夺平息。少年成为不被察觉的“容器”。

多年后，宇智波佐助发现端倪，开启写轮眼追溯因果，通过鱼眼镜头特写重现争夺往事，判定魔方觉醒将引发新一轮血战，决定亲手终结它。

佐助带领那名酷似鸣人的少年及第三名忍者，三人查克拉（风、雷、火）同时注入魔方，将其激活——

魔方爆出神秘蓝光，内部涌现大蛇丸的灵魂，灵魂形态无限扩张，笼罩整个地球/世界。

魔方完成最后一次旋转归位，木叶村陷入集体恐惧：水倒流、火变黑、孩童同时睁眼现出蛇瞳——大蛇丸的灵魂侵入全村意识。

大蛇丸的灵魂开始消散，形态逐渐透明化为光点。但在消散之际，他转向镜头/观众，缓缓伸手，穿越屏幕，逼近观众，宣告“找到你了”，暗示观众将成为下一个“容器”。

---

二、核心设定

元素 说明
魔方 / 界核 来自异界的蓝色发光球体，非武器而是“种子”，需要三种查克拉属性同时注入激活，归位后释放灵魂
大蛇丸 灵魂封存于魔方内，被激活后释放，不直接攻击，而是以恐惧侵蚀整个木叶村，最后试图穿越屏幕寻找观众
写轮眼 宇智波斑用于窥探魔方本质；佐助用于追溯因果、回忆争夺历史
三人激活条件 佐助（雷）+ 少年（风）+ 第三名忍者（火）同时转动魔方

---

三、关键角色一览（更新）

角色 定位 形象特征 关键动作
木叶少年忍者 魔方持有者 / 命运容器 酷似少年鸣人——金发、胡须纹理、橙色衣着、眼神倔强带阳光气质 捡到魔方→遭遇压迫→卷入争夺→参与激活→见证大蛇丸出世
宇智波斑 观察者（开场） 经典宇智波装扮，威严冷峻 远处开启写轮眼，凝视少年与魔方
宇智波佐助 主导者 黑衣、冷峻、写轮眼 追踪真相→召集三人→启动魔方→目睹大蛇丸降临
第三名忍者 协助者 待定（可设计为原创角色或某位木叶忍者） 提供“火”属性查克拉，参与三人合体转动
大蛇丸 终极威胁 苍白肤色、蛇瞳、阴冷气质 灵魂从魔方释放→笼罩世界→入侵木叶意识→消散中穿越屏幕→指向观众

---

四、这个设定带来的叙事张力（新增）

1. 命运的讽刺：魔方偏偏落入“像鸣人”的孩子手中，而鸣人曾是九尾人柱力、被全村恐惧的容器——历史似乎在重演，只是这次封印的不是尾兽，是大蛇丸的灵魂。
2. 佐助与少年的互动：佐助带领这个“少年鸣人”转动魔方时，可能会有瞬间的恍惚——那张脸、那份倔强，仿佛又回到了第七班的时光。这为佐助的决断增添了情感厚度。
3. 大蛇丸的选择：大蛇丸的灵魂选择入侵木叶的集体意识，也许并非随机——他看到了这个“像鸣人”的孩子，如同当年他觊觎佐助的身体一样，对“容器”有着执念。
4. 观众的代入感：当观众看到“少年鸣人”被卷入命运的漩涡，联想到原作中鸣人的成长之路，会产生更强的情感共鸣。

---

五、当前进度

· 已完成：序幕 + 第一幕 + 第二幕 + 第三幕 + 尾声（第四幕）
· 故事状态：全剧终
· 待确认：第三名忍者的具体身份（可设计为小樱、佐井、或原创角色）

---

如果您希望我基于这个更新（少年=鸣人形象）调整某一段的具体台词或动作细节，或者您想为“第三名忍者”赋予特定身份，随时告诉我！