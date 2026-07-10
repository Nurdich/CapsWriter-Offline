# 更新日志

## v3.0（2026-07）

基于上游 [HaujetZhao/CapsWriter-Offline](https://github.com/HaujetZhao/CapsWriter-Offline) 的增强版本。详细开发记录见 [update_log.md](update_log.md)。

### ✨ 灵动岛

屏幕边缘常驻「正在听」药丸浮窗，全面重写：逐像素 alpha 抗锯齿渲染、60fps 弹簧动画、拖拽停靠与位置记忆、本地人声即时响应、实时冒字与完成仪式帧；每次按键自动置顶，不被其他窗口遮挡。

### 🚀 送达流光

识别完成后从灵动岛向鼠标位置发射流光弹幕——7 套内置风格，按字数连射，压轴大弹正中靶心；支持随机换色、彩虹弹幕与 `config_client.py` 完全自定义。

### ⚡ 识别管线

增量预览识别将首字延迟从约 3 秒降至约 0.6 秒；松开键后 two-pass 全量重识别消除分段接缝。录音流式实时冒字、录音时可选静音系统声音。

### 🛠 工程

UV 双包分发（`capswriter-client` / `capswriter-server`，Git + PyPI），移除 PyInstaller 集成大包；源码 `uv sync` 一键装齐依赖。模型与 `LLM/` 由用户自行放置在工作目录。

### 📦 模型获取

发行包不含模型。首次运行 `start_server` 会提示缺失的模型文件与下载页面，按提示将模型解压至 `models/` 对应目录即可。
