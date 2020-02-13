import os
import subprocess
from itertools import cycle
from tempfile import NamedTemporaryFile
from threading import Thread

from pydub.utils import get_player_name


def singleton(cls):
    instances = {}

    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance


def start_thread(func, is_deamon=True):
    thread = Thread(target=func)
    thread.setDaemon(is_deamon)
    thread.start()


def _play_with_ffplay_suppress(seg):
    # seg = seg - 10

    PLAYER = get_player_name()

    with NamedTemporaryFile("w+b", suffix=".wav") as f:
        seg.export(f.name, "wav")
        devnull = open(os.devnull, 'w')
        subprocess.call([PLAYER, "-nodisp", "-autoexit", "-hide_banner", f.name], stdout=devnull, stderr=devnull)


def play_sound(seg):
    def play_sound_function():
        _play_with_ffplay_suppress(seg)

    start_thread(play_sound_function, is_deamon=False)


def get_random_string(length=5):
    tbl = bytes.maketrans(bytearray(range(256)),
                          bytearray([ord(b'a') + b % 26 for b in range(256)]))
    random_string = os.urandom(length).translate(tbl).decode('utf-8')

    return random_string


def get_random_filename():
    EXT = ".svg"

    return get_random_string() + EXT


class Toggler:
    def __init__(self, toggle_list):
        self.pool = cycle(toggle_list)

    def get_pool(self):
        return self.pool

    def toggle(self):
        return next(self.pool)
