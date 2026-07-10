# coding: utf-8
from core.runtime import setup_runtime
from core.client import CapsWriterClient

if __name__ == "__main__":
    setup_runtime("client")
    CapsWriterClient().start()