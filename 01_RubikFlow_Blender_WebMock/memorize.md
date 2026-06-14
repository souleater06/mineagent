# 1. Project Definition / 项目定义
中文

RubikFlow Agent 是一个结合：

App Store 游戏 Roll 的界面风格和机制逻辑
实体智能魔方作为用户真实操作工具
Blender 作为 Roll-like 工作流演示舞台
Agent 作为动作理解和创作生成大脑
方块、粘土、体素、3D 打印作为最终输出方向

的交互式 3D 创作系统。

用户现实中转动实体智能魔方，系统识别魔方动作，把每一次转动映射成一个工作流指令，然后在 Blender 中用类似 Roll 的视觉和机制展示：

工作流节点高亮
流程推进
模型生成
材料变化
创作分数增长
Combo 连击变化
可打印性变化
最终进入方块、粘土、体素或 3D 打印输出

核心一句话：

用魔方转动来编程，用 Blender 看见 Roll 风格工作流，用 Agent 生成可制作、可打印的作品。

## English

RubikFlow Agent is an interactive 3D creation system that combines:

the visual style and mechanics of the App Store game Roll
a physical smart cube as the user’s real-world input device
Blender as a Roll-like workflow visualization stage
an Agent as the brain for interpreting actions and generating creations
blocks, clay, voxels, and 3D printing as final output directions

The user physically rotates a smart cube. The system detects the cube move, maps it into a workflow command, and visualizes the result inside Blender through a Roll-inspired interface:

workflow node activation
timeline progression
model generation
material transformation
creation score growth
combo changes
printability updates
final block, clay, voxel, or 3D-print preparation

Core sentence:

Program by rotating a smart cube, visualize the Roll-inspired workflow in Blender, and let the Agent generate buildable and printable creations.

# 2. What This Project Is Not / 本项目不是做什么
中文

本项目不是：

不是单纯复刻 Roll 游戏。
不是普通骰子游戏。
不是只做一个 Blender 魔方动画。
不是只做静态 UI 面板。
不是把魔方当装饰物。
不是把 Blender 里的魔方删除，只保留 Roll UI。
不是把 Roll UI 和魔方随便摆在一个 3D 空间里。
不是只做视觉演示而没有动作映射逻辑。
不是只做一个好看的界面而没有 Agent 创作流程。
不是让魔方和 Roll 工作流互相穿插、遮挡、混乱。

必须牢记：

魔方是输入设备，Roll-inspired 界面是工作流反馈，Blender 是可视化舞台，Agent 是理解和生成的大脑。

## English

This project is not:

Not a pure clone of the Roll game.
Not a normal dice game.
Not just a Blender Rubik's cube animation.
Not just a static UI panel.
Not using the cube as decoration.
Not removing the cube from Blender and keeping only the Roll UI.
Not randomly placing Roll UI panels and a cube in 3D space.
Not a visual-only demo without move-to-workflow logic.
Not a pretty interface without an Agent-driven creation process.
Not allowing the cube and workflow UI to intersect, overlap, or become visually confusing.

Always remember:

The cube is the input device, the Roll-inspired UI is the workflow feedback, Blender is the visualization stage, and the Agent is the brain that interprets and generates.

# 3. Core Concept / 核心概念
中文

这个项目的核心不是“做一个魔方”，也不是“做一个 Roll 游戏界面”。

核心是：

实体智能魔方转动
-> 系统识别 Detected Move
-> Agent 映射为 Mapped Action
-> Roll-inspired 工作流节点高亮
-> Blender 生成物变化
-> 方块 / 粘土 / 体素 / 3D 打印输出

Roll 游戏里：

骰子 / Dice
-> 掷骰 / Roll
-> 触发格子 / Tile
-> 获得加成 / Bonus
-> 数字增长 / Score
-> 解锁升级 / Upgrade

RubikFlow Agent 里：

智能魔方 / Smart Cube
-> 转动魔方面 / Rotate Face
-> 触发工作流节点 / Workflow Tile
-> 生成结构变化 / Model Operation
-> 创作分数和可打印性变化 / Creation Score & Printability
-> 输出方块、粘土、3D 打印结果
## English

The core of this project is not “making a cube” or “making a Roll UI”.

The core is:

Physical smart cube rotation
-> Detected Move
-> Agent maps it to a Mapped Action
-> Roll-inspired workflow node activation
-> Blender output changes
-> Block / clay / voxel / 3D-print output

In Roll:

Dice
-> Roll
-> Tile trigger
-> Bonus
-> Score growth
-> Upgrade

In RubikFlow Agent:

Smart Cube
-> Rotate Face
-> Workflow Tile Activation
-> Model Operation
-> Creation Score & Printability
-> Block, clay, and 3D-print output
# 4. Roll-to-RubikFlow Mapping / Roll 游戏与 RubikFlow 的对应关系
中文

Roll 游戏的核心不是“骰子外观”，而是：

一个简单动作触发格子、加成、数值增长和升级连锁。

RubikFlow Agent 要把这个机制从“骰子游戏”升级为“魔方驱动的创作工作流”。

## English

The core of Roll is not just the visual appearance of dice. Its core mechanic is:

A simple action triggers tiles, bonuses, numerical growth, and upgrade chains.

RubikFlow Agent transforms this from a dice game into a cube-driven creative workflow system.

| Roll Game Element | RubikFlow Agent Element | 中文解释 | English Explanation |
| --- | --- | --- | --- |
| Dice | Smart Cube | 骰子变成实体智能魔方 | The dice becomes a physical smart cube |
| Roll Dice | Rotate Cube Face | 掷骰变成转动魔方面 | Rolling becomes rotating a cube face |
| Dice Result | Detected Move | 点数变成 U/F/R/D/B 动作 | Dice result becomes a detected move |
| Dice-o-pedia | Workflow-o-pedia | 骰子图鉴变成工作流图鉴 | Dice encyclopedia becomes workflow encyclopedia |
| Tile Bonus | Workflow Node Activation | 格子加成变成节点触发 | Tile bonus becomes workflow node activation |
| Combo Multiplier | Move Combo | 倍率变成连续动作组合 | Multiplier becomes move combo |
| Shop / Upgrade | Node Upgrade / Material Upgrade | 商店升级变成节点/材料升级 | Shop upgrades become node/material upgrades |
| Score | Creation Score / Printability | 分数变成创作分和可打印性 | Score becomes creation score and printability |
| Treasury / Bank | Asset Bank / Material Bank | 金库变成资源/材料库 | Treasury becomes asset/material bank |
| Leaderboard | Preset Library / Best Builds | 排行榜变成最佳作品库 | Leaderboard becomes preset/build library |
# 5. Role of the Physical Smart Cube / 实体智能魔方的角色
中文

实体智能魔方是用户真实操作的工具。

用户不是用鼠标点按钮，而是用手转动魔方来控制工作流。

实体智能魔方的角色是：

空间交互控制器
工作流遥控器
创作命令输入器
类似“我的世界红石开关”的物理逻辑输入设备
把现实手部动作转化为数字创作命令的硬件入口
## English

The physical smart cube is the real-world input tool.

The user does not click buttons with a mouse. The user controls the workflow by physically rotating the cube.

The physical smart cube acts as:

a spatial interaction controller
a workflow remote
a creative command input device
a physical logic switch similar to Minecraft Redstone
a hardware gateway that converts hand motion into digital creation commands
# 6. Role of the Cube in Blender / Blender 中魔方的角色
中文

Blender 中必须有魔方。

Blender 里的魔方不是装饰，不是主 UI 的一部分，也不能删除。

它是现实实体智能魔方的数字孪生，用来让观众直观看到：

用户现实中转了哪一面魔方
↓
系统识别成什么动作
↓
这个动作映射成哪个工作流命令
↓
Roll-inspired 主工作流界面发生什么变化

Blender 中的魔方必须：

清楚可见。
不要太小。
不要跑出相机。
不要和主 UI 穿插。
保持独立区域。
显示 Detected Move。
显示 Mapped Action。
有转动提示或高亮。
表达“这是现实智能魔方的输入映射器”。
## English

There must be a cube inside Blender.

The cube in Blender is not decoration, not part of the main UI, and must not be removed.

It is the digital twin of the physical smart cube. It helps the viewer understand:

Which cube face the user rotated in the real world
↓
What move the system detected
↓
What workflow command the move maps to
↓
How the Roll-inspired main workflow interface responds

The Blender cube must:

Be clearly visible.
Not be too small.
Not be outside the camera frame.
Not intersect with the main UI.
Stay in its own input zone.
Show Detected Move.
Show Mapped Action.
Show rotation hints or highlights.
Communicate that it is the input mapper for the real smart cube.
# 7. Main Visual Structure / 主视觉结构

The demo must use a clear two-zone structure.
Demo 必须使用清楚的双区域结构：

## A. Smart Cube Input Zone
## B. Roll-inspired Main Workflow Stage
## A. Smart Cube Input Zone / 智能魔方输入区

This area represents the real physical smart cube input.
该区域表示真实实体智能魔方输入。

It must include:

Title: Smart Cube Input
标题：Smart Cube Input
A clear 3x3 smart cube
一个清楚可见的 3x3 智能魔方
Detected Move
检测到的动作
Mapped Action
映射后的工作流命令
Input -> Workflow signal arrow
输入到工作流的信号箭头
Rotation highlight or arrow track
转动高亮或箭头轨迹

This area should be independent from the main workflow UI.
该区域应独立于主工作流 UI。

## B. Roll-inspired Main Workflow Stage / Roll 风格主工作流舞台

This is the main visual area.
这是画面的主视觉区域。

It must look like a complete App/game interface, not scattered Blender objects.
它必须像一个完整 App / 游戏界面，而不是散落的 Blender 物体。

It must include:

Title: RubikFlow Agent
Roll-style top navigation icons
Workflow-o-pedia panel
5 x 4 workflow tile grid
Status panel
Output Preview area
Creation Score
Combo indicator
Printability indicator
Bottom Workflow Timeline
3D Print Preview state

Visual style:

off-white / warm white background
black text and icons
rounded cards
clear tile grid
pale blue / lavender highlights
Roll-inspired minimal UI
orthographic 16:9 product demo composition

视觉风格：

奶白 / 浅灰背景
黑色文字和图标
圆角卡片
清晰格子
淡蓝 / 淡紫高亮
Roll 风格极简 UI
正交 16:9 产品展示构图
# 8. Workflow-o-pedia Tiles / 工作流图鉴格子

Workflow-o-pedia is inspired by Roll's Dice-o-pedia.
Workflow-o-pedia 灵感来自 Roll 的 Dice-o-pedia。

It must contain 20 tiles in a 5 x 4 grid.
必须包含 5 列 x 4 行，共 20 个 tile。

Fixed tile list:

+BLOCK, CLAY, VOXEL, JOINT, MIRROR,
SCALE, COLOR, SCAN, AGENT, PRINT,
EXPORT, SHELL, HOLLOW, STACK, LOCK,
LOOP, CHECK, FIX, BUILD, SAVE

Important requirements:

All 20 tiles must be visible.
The layout must be clean and regular.
The active tile must be clearly highlighted.
Text can be used instead of complex icons in the first version.
The tile grid must feel like a Roll-inspired encyclopedia or upgrade board.

重要要求：

20 个 tile 必须全部可见。
排列必须整齐规整。
当前激活 tile 必须明显高亮。
第一版可以直接使用文字，不必做复杂图标。
tile 网格要有 Roll 游戏图鉴 / 升级面板的感觉。
# 9. Cube Move to Workflow Command Mapping / 魔方动作与工作流命令映射

The first demo uses this fixed move sequence:
第一版 Demo 使用固定动作序列：

```python
MOVES = ["U", "F", "R", "F", "D", "B"]
```
## Move Mapping Table / 动作映射表
| Move | Mapped Action | 中文含义 | Required Visual Response |
| --- | --- | --- | --- |
| U | Select Module | 选择模块 | Highlight selection-related tile and timeline node |
| F | Generate Block | 生成基础方块 | Show a basic block in Output Preview |
| R | Upgrade Structure | 升级结构 | Add joints, supports, or stacked structure |
| Second F | Add Clay / Voxel Shell | 添加粘土/体素外壳 | Add clay layer, voxel shell, or soft cover |
| D | Confirm Node | 确认节点 | Show LOCKED / Confirmed state |
| B | Prepare Print | 准备打印 | Show 3D print platform, slicing lines, STL/Print state |
# 10. Step-by-Step Visual Requirements / 每一步必须显示什么
## Step 1: U

Detected Move:

U

Mapped Action:

Select Module

Required visual response:

Smart Cube Input updates to U.
Workflow-o-pedia highlights SCAN / AGENT / SELECT-related tile.
Timeline highlights SELECT MODULE.
Status panel updates to Select Module.
Output Preview stays ready but does not generate yet.

中文要求：

智能魔方输入区显示 U。
工作流图鉴高亮选择相关 tile。
时间线高亮 SELECT MODULE。
状态面板显示 Select Module。
输出区暂不生成物体，只显示准备状态。
## Step 2: F

Detected Move:

F

Mapped Action:

Generate Block

Required visual response:

Workflow-o-pedia highlights +BLOCK.
Output Preview shows a basic block.
Timeline highlights GENERATE BLOCK.
Creation Score increases.
Combo becomes x1 or x2.

中文要求：

高亮 +BLOCK。
输出区出现基础方块。
时间线高亮 GENERATE BLOCK。
创作分数增长。
Combo 开始增加。
## Step 3: R

Detected Move:

R

Mapped Action:

Upgrade Structure

Required visual response:

Workflow-o-pedia highlights JOINT or STACK.
Output Preview adds supports, joints, or layered structure.
Timeline highlights UPGRADE STRUCTURE.
Creation Score increases more.
Printability changes.

中文要求：

高亮 JOINT 或 STACK。
输出区增加支架、连接件或堆叠结构。
时间线高亮 UPGRADE STRUCTURE。
创作分数继续增加。
可打印性变化。
## Step 4: Second F

Detected Move:

F

Mapped Action:

Add Clay / Voxel Shell

Required visual response:

Workflow-o-pedia highlights CLAY or VOXEL.
Output Preview adds clay layer, voxel shell, or soft cover.
Timeline highlights ADD CLAY.
Material Mode changes to Block + Clay + Voxel.

中文要求：

高亮 CLAY 或 VOXEL。
输出区出现粘土层、体素外壳或柔性包覆层。
时间线高亮 ADD CLAY。
材料模式变为 Block + Clay + Voxel。
## Step 5: D

Detected Move:

D

Mapped Action:

Confirm Node

Required visual response:

Workflow-o-pedia highlights LOCK.
Output Preview shows LOCKED / Confirmed.
Timeline highlights CONFIRM.
Workflow State becomes Confirmed.

中文要求：

高亮 LOCK。
输出区显示 LOCKED / Confirmed。
时间线高亮 CONFIRM。
工作流状态变为 Confirmed。
## Step 6: B

Detected Move:

B

Mapped Action:

Prepare Print

Required visual response:

Workflow-o-pedia highlights PRINT or EXPORT.
Output Preview shows a 3D print platform.
Add slicing lines.
Timeline highlights PREPARE PRINT.
Status shows STL Ready / Print Ready.
Printability reaches final value.

中文要求：

高亮 PRINT 或 EXPORT。
输出区出现 3D 打印平台。
出现切片线。
时间线高亮 PREPARE PRINT。
状态面板显示 STL Ready / Print Ready。
可打印性到达最终值。
# 11. Output Preview / 输出预览区

Output Preview represents the creative result of the workflow.
Output Preview 表示工作流的创作结果。

It must change step by step:

Empty / Ready
-> Basic Block
-> Upgraded Structure
-> Clay / Voxel Shell
-> Locked
-> 3D Print Preview

中文：

空 / 准备状态
-> 基础方块
-> 升级结构
-> 粘土 / 体素外壳
-> 锁定确认
-> 3D 打印预览

The final state must clearly show:

3D print platform
slicing lines
print ready label
STL / Export implication

最终状态必须清楚显示：

3D 打印平台
切片线
打印准备标签
STL / Export 暗示
# 12. Innovation Points / 创新点
## 12.1 Cube-as-Controller / 魔方作为控制器

The smart cube becomes a physical workflow controller.
智能魔方不再只是玩具，而是空间工作流控制器。

## 12.2 Move-to-Node Mapping / 动作到节点映射

Each cube move becomes a meaningful workflow command.
每个魔方动作都变成一个可解释的工作流命令。

## 12.3 Roll-like Workflow Gamification / Roll 风格工作流游戏化

The project transforms boring modeling operations into a game-like workflow.
本项目把枯燥的建模操作变成类似游戏的工作流。

Traditional Blender:

Click menu -> adjust parameters -> edit nodes

RubikFlow:

Rotate cube -> trigger tile -> generate structure -> upgrade -> print

传统 Blender：

点菜单 -> 调参数 -> 编辑节点

RubikFlow：

转魔方 -> 触发格子 -> 生成结构 -> 升级 -> 打印
## 12.4 Physical Creation Pipeline / 实体创作管线

The workflow does not stop on screen. It connects to physical creation.
工作流不止停留在屏幕里，而是连接实体创作。

Target outputs:

blocks
clay
voxel models
modular connectors
3D printing
STL / OBJ export

目标输出：

方块
粘土
体素模型
模块化连接件
3D 打印
STL / OBJ 导出
## 12.5 Minecraft Redstone-like Logic / 类似我的世界红石的逻辑

RubikFlow is like Minecraft Redstone for physical 3D creation.
RubikFlow 像是面向实体 3D 创作的“我的世界红石”。

Why:

simple actions create complex systems
nodes connect into logic chains
each move has input and output
users can build creative workflows through action sequences

原因：

简单动作可以组合成复杂系统
节点可以连接成逻辑链
每个动作都有输入和输出
用户可以通过动作序列搭建创作流程
## 12.6 Roll-to-Physical Creation Upgrade / 从 Roll 到实体创作的升级

Roll turns dice results into game rewards.
RubikFlow turns cube moves into physical creation operations.

Roll 把骰子结果变成游戏奖励。
RubikFlow 把魔方动作变成实体创作操作。

# 13. Relation to Blocks, Clay, Voxels, and 3D Printing
与方块、粘土、体素、3D 打印的关系
中文

RubikFlow Agent 的最终目标不是只在 Blender 中做动画，而是服务于实体创作。

它应该支持：

方块结构生成
类似积木、Minecraft block、模块化方块。
粘土形态生成
表示柔性材料、手工制作、可塑形外壳。
体素结构生成
把复杂形体简化成可制作的 voxel grid。
连接件和关节
让结构不仅是静态模型，而是可装配、可扩展。
3D 打印准备
包括打印平台、切片线、STL/OBJ 导出提示。
## English

RubikFlow Agent is not only a Blender animation. Its final goal is physical creation.

It should support:

Block-based structure generation
Similar to bricks, Minecraft blocks, and modular cubes.
Clay-form generation
Representing soft material, hand crafting, and moldable surfaces.
Voxel structure generation
Simplifying complex forms into manufacturable voxel grids.
Connectors and joints
Making the structure modular, extendable, and buildable.
3D print preparation
Including print platform, slicing lines, and STL/OBJ export hints.
# 14. Camera and Visibility Rules / 相机和可见性规则
中文

运行 Blender 脚本后，进入相机视角，必须一眼看到完整系统。

相机要求：

Orthographic 正交相机
16:9
1920 x 1080
正视图或接近正视图
主工作流舞台是画面主体
智能魔方输入区清楚可见
所有核心元素都在相机框内

第 1、60、120、180、210 帧都必须看到完整系统。

禁止出现：

主界面消失
魔方消失
只有几个残缺面板
面板互相穿插
文字看不清
生成物跑出画面
相机看不到核心内容
魔方被放到画面外
Roll 工作流只剩残缺 UI
## English

After running the Blender script and entering camera view, the complete system must be visible at a glance.

Camera requirements:

Orthographic camera
16:9
1920 x 1080
Front or near-front view
Main workflow stage as the visual focus
Smart cube input zone clearly visible
All core elements inside the camera frame

Frames 1, 60, 120, 180, and 210 must all show the complete system.

Do not allow:

main interface disappearing
cube disappearing
only partial panels visible
panels intersecting each other
unreadable text
output objects outside the frame
camera missing core content
cube being pushed outside the frame
Roll workflow becoming only broken UI fragments
# 15. Animation Principles / 动画原则
中文

第一阶段优先稳定、清楚、完整、可见。

不要为了复杂动画导致 bug。

优先使用：

材质颜色变化
tile 高亮变化
时间线节点高亮
状态文字更新
生成物逐步出现
魔方面高亮
简单转动提示
分数、Combo、Printability 数值变化

不要大量使用复杂 visibility hide/unhide，避免对象消失。

主 UI 面板、标题、Workflow-o-pedia、状态面板、时间线必须始终存在。

## English

The first stage prioritizes stability, clarity, completeness, and visibility.

Do not create complex animations that cause bugs.

Prefer:

material color changes
tile highlight changes
timeline node highlights
status text updates
gradual output appearance
cube face highlights
simple rotation hints
score, combo, and printability updates

Avoid complex visibility hide/unhide systems that may make objects disappear.

The main UI panel, title, Workflow-o-pedia, status panel, and timeline must always exist.

# 16. First Stage Demo Goal / 第一阶段 Demo 目标
中文

第一阶段不需要真实接入实体智能魔方。

第一阶段只需要用固定动作序列模拟用户操作：

```python
MOVES = ["U", "F", "R", "F", "D", "B"]
```

Blender 中必须展示：

魔方同步转动
Detected Move 变化
Mapped Action 变化
Workflow-o-pedia tile 高亮
状态面板更新
时间线推进
Output Preview 逐步变化
Creation Score 增长
Combo 变化
Printability 变化
最终进入 3D 打印准备

第一阶段目标是让老师、组员、评委一眼看懂：

这是一个用实体智能魔方控制 Roll 风格工作流的 Agent 创作系统。

## English

The first stage does not need real smart cube hardware integration.

The first stage only simulates user actions with a fixed move sequence:

```python
MOVES = ["U", "F", "R", "F", "D", "B"]
```

Blender must show:

cube rotation sync
Detected Move updates
Mapped Action updates
Workflow-o-pedia tile highlights
status panel updates
timeline progression
Output Preview progression
Creation Score growth
Combo updates
Printability updates
final 3D print preparation

The goal is to make teachers, teammates, or judges immediately understand:

This is an Agent creation system where a physical smart cube controls a Roll-inspired workflow.

# 17. Future Roadmap / 后续路线图
## Phase 1: Stable Blender Demo / 稳定 Blender 演示版
fixed move sequence
Roll-inspired UI
visible smart cube input
workflow tile activation
output preview changes
print preparation visualization
## Phase 2: Keyboard Input Prototype / 键盘输入原型
U/F/R/D/B keyboard input
real-time workflow update
debug panel
move history
## Phase 3: Real Smart Cube Integration / 实体智能魔方接入
receive smart cube sensor data
convert data into cube moves
send moves to Blender
update workflow live
## Phase 4: Agent Command Layer / Agent 命令层
Agent interprets move sequences
Agent suggests next workflow step
Agent creates or modifies structures
Agent detects invalid workflow states
## Phase 5: Physical Output Pipeline / 实体输出管线
block generation
clay shell generation
voxel conversion
connector generation
STL / OBJ export
3D print preparation
## Phase 6: Redstone-like Workflow System / 红石式工作流系统
node chaining
conditional logic
repeat loops
resource bank
material upgrades
reusable workflow presets
# 18. Development Constraints / 开发约束

Codex must only modify this project:
Codex 只能修改当前项目：

D:\codex-blender\rubikflow-agent

Codex must not modify these projects:
Codex 不允许修改以下项目：

D:\codex-work\AuthentiX
D:\codex-work\miniAuthentiX
D:\codex-blender\rubik-hollow-render

The Blender script must keep these controls:
Blender 脚本必须保留：

AUTO_RENDER_STILL = False
AUTO_RENDER_ANIMATION = False
STILL_PREVIEW_FRAME = 205

Default behavior:

Do not auto-render animation.
Clear the scene safely.
Build the full scene automatically.
Set active orthographic camera.
Keep all core elements visible.
Run syntax check after modification.

默认行为：

不要自动渲染动画。
安全清空场景。
自动生成完整场景。
设置 active 正交相机。
保证所有核心元素可见。
修改后运行语法检查。

Required check:

```bash
python -m py_compile rubikflow_agent_demo.py
```
# 19. Acceptance Checklist / 验收标准

Every version must pass this checklist.
每一版都必须通过以下检查。

Visual / 视觉
 Smart cube is clearly visible.
 Cube is not removed.
 Cube is independent from the main UI.
 Main Roll-inspired interface is complete.
 20 Workflow-o-pedia tiles are visible.
 Status panel is readable.
 Timeline is visible.
 Output Preview is visible.
 Camera shows the full system.
 Nothing important is outside the frame.
 No major overlapping or intersection.
 Roll-inspired UI looks like a complete App/game interface.
 The cube does not disappear or become too small.
Logic / 逻辑
 Detected Move updates.
 Mapped Action updates.
 Tile highlight matches the move.
 Timeline highlight matches the move.
 Output Preview changes step by step.
 Creation Score changes.
 Combo changes.
 Printability changes.
 Final state shows print preparation.
 Cube movement clearly maps to workflow state.
Technical / 技术
 Script runs in Blender.
 Python syntax check passes.
 AUTO_RENDER_STILL remains False by default.
 AUTO_RENDER_ANIMATION remains False by default.
 Other projects are not modified.
# 20. Long-term Codex Rules / Codex 长期规则

Before modifying this project, Codex must:

Read this memorize.md.
Respect the project definition.
Keep the smart cube visible.
Keep Roll-inspired workflow complete.
Preserve cube-to-workflow mapping.
Prioritize clarity and stability.
Avoid overcomplicated animation that causes invisible objects.
Only modify files in this project.
Explain what changed after every update.
Run syntax check after code changes.
Never remove the Blender cube.
Never leave only broken or partial Roll UI panels.
Always ensure the camera view shows the complete system.

中文：

每次修改本项目之前，Codex 必须：

先阅读 memorize.md。
遵守项目定义。
保证智能魔方可见。
保证 Roll-inspired 工作流完整。
保留魔方动作到工作流的映射。
优先保证清楚和稳定。
不要为了复杂动画导致对象消失。
只修改当前项目文件。
每次修改后说明改了什么。
修改代码后运行语法检查。
永远不要删除 Blender 中的魔方。
永远不要只留下残缺的 Roll UI 面板。
始终保证相机视角能看到完整系统。
# 21. Final Principle / 最终原则
中文

永远记住：

魔方 = 实体输入设备
Roll-inspired UI = 工作流反馈界面
Blender = 可视化舞台
Agent = 动作理解和生成大脑
方块 / 粘土 / 体素 / 3D 打印 = 最终实体创作输出

最终目标：

RubikFlow Agent 要把智能魔方从玩具变成一个空间工作流控制器，让用户通过真实魔方转动来触发 Agent 的建模、生成、修改、确认和打印流程。

更简洁地说：

RubikFlow Agent 是一个用实体魔方控制 Roll 风格工作流，并在 Blender 中生成方块、粘土、体素和 3D 打印结果的 Agent 系统。

## English

Always remember:

Cube = physical input device
Roll-inspired UI = workflow feedback interface
Blender = visualization stage
Agent = move interpretation and generation brain
Blocks / clay / voxels / 3D printing = final physical creation output

Final goal:

RubikFlow Agent turns a smart cube from a toy into a spatial workflow controller, allowing users to trigger modeling, generation, modification, confirmation, and print preparation through real cube rotations.

In short:

RubikFlow Agent is an Agent system that uses a physical smart cube to control a Roll-inspired workflow and generate block, clay, voxel, and 3D-print outputs inside Blender.
