# coding: utf-8

from core.runtime import ensure_workspace, setup_runtime


def init_workspace() -> None:
    """在当前目录生成客户端默认配置与热词模板。"""
    base = ensure_workspace("client")
    print(f"客户端工作目录已就绪: {base}")
    print("请编辑 config_client.py，将 models/、LLM/ 放在此目录后运行 capswriter-client")


def main() -> None:
    setup_runtime("client")
    from core.client import CapsWriterClient

    CapsWriterClient().start()
