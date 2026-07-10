# coding: utf-8
from multiprocessing import freeze_support

from core.runtime import setup_runtime
from core.server.app import CapsWriterServer

if __name__ == '__main__':
    freeze_support()
    setup_runtime("server")
    CapsWriterServer().start()