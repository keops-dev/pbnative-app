from . import setup as stp
from . import messenger


def setup():
    return stp.start()


def start():
    return messenger.start()
