# coding: utf-8

from multiprocessing import freeze_support

from core.runtime import ensure_workspace, setup_runtime


def init_workspace() -> None:
    """在当前目录生成服务端默认配置与热词模板。"""
    base = ensure_workspace("server")
    print(f"服务端工作目录已就绪: {base}")
    print("请编辑 config_server.py，将 models/ 放在此目录后运行 capswriter-server")


def main() -> None:
    freeze_support()
    setup_runtime("server")
    from core.server.app import CapsWriterServer

    CapsWriterServer().start()
