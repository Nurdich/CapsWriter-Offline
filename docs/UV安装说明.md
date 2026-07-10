# UV 安装说明

本分支 v3.0 起，**推荐通过 UV 安装两个独立包**，不再发布集成 exe 大包。

| 包名 | 作用 | 命令 |
|------|------|------|
| `capswriter-server` | 本地 ASR 推理 | `capswriter-server` |
| `capswriter-client` | 快捷键听写、灵动岛、热词、LLM | `capswriter-client` |

两个包**均不含模型权重**。模型需自行下载后放入工作目录的 `models/`。

---

## 1. 安装 UV

Windows PowerShell：

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

安装后**重启终端**，验证：

```powershell
uv --version
```

UV 会自动管理 Python 版本，无需单独安装 Python（首次运行时会下载 3.12）。

---

## 2. 准备工作目录

所有配置、热词、模型、录音归档都放在**同一个文件夹**（工作目录），与安装位置无关。

```powershell
mkdir D:\CapsWriter
cd D:\CapsWriter
```

推荐目录结构（逐步补齐即可）：

```
D:\CapsWriter\
├── config_server.py      ← capswriter-server-init 生成
├── config_client.py      ← capswriter-client-init 生成
├── hot.txt               ← 客户端热词
├── hot-rule.txt          ← 正则替换规则
├── hot-server.txt        ← 服务端热词
├── models\               ← 自行下载，见 docs/模型下载的若干问题.md
├── LLM\                  ← 从仓库复制（用 LLM 角色时需要）
├── assets\               ← 可选，托盘图标等
└── 2026\                 ← 运行后自动生成的日记/录音归档
```

---

## 3. 安装服务端 / 客户端

### 方式 A：从 Git 安装（当前推荐）

需先 `git push` 到 GitHub，他人才能安装。分支为 `island`：

```powershell
uv tool install "git+https://github.com/Nurdich/CapsWriter-Offline.git@island#subdirectory=packages/capswriter-server"
uv tool install "git+https://github.com/Nurdich/CapsWriter-Offline.git@island#subdirectory=packages/capswriter-client"
```

### 方式 B：从 PyPI 安装（维护者 `twine upload` 后可用）

```powershell
uv tool install capswriter-server
uv tool install capswriter-client
```

### 方式 C：临时试用（不写入 PATH）

在工作目录下：

```powershell
cd D:\CapsWriter
uvx --from capswriter-server capswriter-server
uvx --from capswriter-client capswriter-client
```

### 升级

```powershell
uv tool upgrade capswriter-server
uv tool upgrade capswriter-client
```

### 卸载

```powershell
uv tool uninstall capswriter-server
uv tool uninstall capswriter-client
```

---

## 4. 首次初始化

在工作目录执行（会复制默认配置，**不覆盖已有文件**）：

```powershell
cd D:\CapsWriter
capswriter-server-init
capswriter-client-init
```

然后按需编辑 `config_server.py`、`config_client.py`。

---

## 5. 准备模型

1. 打开 [模型下载说明](模型下载的若干问题.md)，按 `config_server.py` 里 `model_type` 选择引擎
2. 将模型文件解压到 `D:\CapsWriter\models\<引擎名>\`
3. 首次运行 `capswriter-server` 时，若缺模型会在控制台打印缺失列表与下载页链接

---

## 6. 启动

**两个终端**，均先 `cd` 到工作目录：

```powershell
# 终端 1 — 服务端（加载模型，托盘图标）
cd D:\CapsWriter
capswriter-server

# 终端 2 — 客户端（听写、灵动岛）
cd D:\CapsWriter
capswriter-client
```

按住 `CapsLock` 或鼠标侧键 `X2` 说话，松开即上屏。

> 客户端黑窗口/托盘需保持运行。若要在管理员权限程序中输入，客户端也需管理员运行。

---

## 7. 源码开发（可选）

克隆仓库后，在根目录：

```powershell
git clone https://github.com/Nurdich/CapsWriter-Offline.git
cd CapsWriter-Offline
uv sync   # 安装 client + server 全部运行时依赖

# 终端 1
uv run start_server.py

# 终端 2
uv run start_client.py
```

---

## 8. 维护者：构建并发布 PyPI

```powershell
pip install build twine
python build_uv.py
# 检查 dist/uv/*.whl
twine upload dist/uv/*.whl
```

---

## 常见问题

**Q: 命令找不到？**  
A: `uv tool install` 后需重启终端；或执行 `uv tool update-shell` 将 `~/.local/bin` 加入 PATH。

**Q: 配置改了不生效？**  
A: 确认是在**工作目录**下的 `config_*.py` 修改，且启动前已 `cd` 到该目录。

**Q: 服务端报缺 DLL / VC++？**  
A: 安装 [VC++ 运行库](https://learn.microsoft.com/zh-cn/cpp/windows/latest-supported-vc-redist)。文件转录还需 [ffmpeg](https://ffmpeg.org/download.html) 在 PATH 中。

**Q: 和旧版 exe 包有什么区别？**  
A: UV 包只有 Python 代码 + pip 依赖（几十 MB 级），模型、LLM 角色、热词均由用户放在工作目录，升级包体小、配置可改。
