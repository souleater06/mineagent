\# RubikFlow Agent Project Submit



本压缩包包含两个部分：



\## 1. RubikFlow Blender / Web Mock



路径：

01\_RubikFlow\_Blender\_WebMock/



主要打开文件：

01\_RubikFlow\_Blender\_WebMock/web/rubikflow\_web\_mock.html



用途：

展示 RubikFlow Agent 的前端草稿，包括 Smart Cube Input、Workflow-o-pedia、Agent State、Agent Function Pipeline、Output Preview 和 Workflow Timeline。



说明：

这是用于 Blender / WebGL / 前端视觉参考的 RubikFlow Agent 原型。



\## 2. csTimer RubikFlow Plugin MVP



路径：

02\_csTimer\_RubikFlow\_Plugin/



主要打开文件：

02\_csTimer\_RubikFlow\_Plugin/experiment/rubikflow-overlay-demo.html



用途：

展示 csTimer 插件 MVP。左侧是 csTimer mock 页面，右侧是 RubikFlow Agent Overlay。



测试方式：

按键盘 U / F / R / F / D / B，或者点击 Run Sequence，可模拟智能魔方动作触发工作流。



\## 当前阶段



目前项目仍是 Demo / MVP 阶段：



\- RubikFlow Web Mock 用于展示界面和工作流概念。

\- csTimer 插件 MVP 用于模拟智能魔方动作输入。

\- 暂未接入真实蓝牙智能魔方。

\- 暂未正式集成到 csTimer 核心源码。

\- Blender Python Demo 仍有布局和视觉问题，当前优先参考 Web Mock。



\## 后续方向



1\. 继续修复 Web Mock 视觉细节。

2\. 抽象 csTimer 插件事件接口。

3\. 接入真实 csTimer move event / smart cube event。

4\. 联动 Blender / WebGL 进行可视化展示。

