# coding: utf-8
"""
系统音频静音模块

提供控制系统主音量的功能，使用 pycaw + comtypes + Windows Core Audio API。
在录音开始时静音，录音结束后恢复原音量。
"""

from __future__ import annotations

from . import logger


class SystemAudioMute:
    """
    系统音频静音管理器

    通过 Windows Core Audio API 控制主音量静音状态。
    记录静音前的音量大小，以便恢复。
    """

    _volume = None
    _saved_volume: float = 0.0

    @classmethod
    def mute(cls) -> None:
        """静音系统声音输出"""
        if not cls._init():
            return

        try:
            if cls._volume.GetMute():
                return  # 已经静音

            # 保存当前音量
            cls._saved_volume = cls._volume.GetMasterVolumeLevelScalar()

            # 静音
            cls._volume.SetMute(True, None)
            logger.debug("系统声音已静音")
        except Exception as e:
            logger.warning(f"静音系统声音失败: {e}")

    @classmethod
    def unmute(cls) -> None:
        """恢复系统声音"""
        if not cls._init():
            return

        try:
            if not cls._volume.GetMute():
                return  # 已经非静音

            # 取消静音
            cls._volume.SetMute(False, None)
            # 恢复原音量
            if cls._saved_volume > 0.0:
                cls._volume.SetMasterVolumeLevelScalar(cls._saved_volume, None)
            logger.debug("系统声音已恢复")
        except Exception as e:
            logger.warning(f"恢复系统声音失败: {e}")

    @classmethod
    def _init(cls) -> bool:
        """初始化音频端点音量控制接口"""
        if cls._volume is not None:
            return True

        try:
            from pycaw.pycaw import AudioUtilities

            devices = AudioUtilities.GetSpeakers()
            cls._volume = devices.EndpointVolume
            return True
        except Exception as e:
            logger.warning(f"初始化音频设备失败: {e}")
            return False
