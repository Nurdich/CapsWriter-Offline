# coding: utf-8
"""UV / PyPI 安装模式下的工作目录与配置引导。"""

from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path

_CLIENT_CONFIG = "config_client.py"
_SERVER_CONFIG = "config_server.py"

_CLIENT_TEMPLATES = (
    _CLIENT_CONFIG,
    "hot.txt",
    "hot-rule.txt",
    "hot-server.txt",
)

_SERVER_TEMPLATES = (
    _SERVER_CONFIG,
    "hot-server.txt",
)


def _install_root() -> Path:
    """已安装 wheel 的根目录（含 core/ 与默认配置模板）。"""
    import core

    return Path(core.__file__).resolve().parent.parent


def get_base_dir(role: str) -> Path:
    """解析运行基目录：优先当前工作目录，其次安装目录。"""
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent

    cwd = Path.cwd()
    marker = _CLIENT_CONFIG if role == "client" else _SERVER_CONFIG
    if (cwd / marker).exists():
        return cwd

    root = _install_root()
    if (root / marker).exists():
        return root

    return cwd


def _templates_for(role: str) -> tuple[str, ...]:
    return _CLIENT_TEMPLATES if role == "client" else _SERVER_TEMPLATES


def ensure_workspace(role: str, base: Path | None = None) -> Path:
    """若工作目录缺少配置/热词模板，从安装包复制默认文件。"""
    base = base or get_base_dir(role)
    bundled = _install_root()
    for name in _templates_for(role):
        dest = base / name
        if dest.exists():
            continue
        src = bundled / name
        if not src.exists():
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
    return base


def setup_runtime(role: str) -> Path:
    """准备运行环境：工作目录、sys.path、默认配置。"""
    base = ensure_workspace(role)
    os.chdir(base)
    base_str = str(base)
    if base_str not in sys.path:
        sys.path.insert(0, base_str)
    return base
