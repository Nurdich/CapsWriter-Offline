# capswriter-server

CapsWriter-Offline **服务端** PyPI 包（本地 ASR 推理）。

- 命令：`capswriter-server`
- 初始化：`capswriter-server-init`（在当前目录生成 `config_server.py`、热词模板）

完整安装步骤见：[docs/UV安装说明.md](../../docs/UV安装说明.md)

```powershell
uv tool install capswriter-server
# 或 Git：
uv tool install "git+https://github.com/Nurdich/CapsWriter-Offline.git@island#subdirectory=packages/capswriter-server"
```

> 不含模型权重。将 `models/` 放在工作目录后启动。
