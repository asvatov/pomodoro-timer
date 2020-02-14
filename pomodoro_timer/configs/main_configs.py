import os

from pomodoro_timer import APP


def is_package():
    return os.path.abspath(os.path.dirname(__file__)).startswith('/usr')


def normalize_url(url):
    if url.startswith("http://") or url.startswith("https://"):
        return url

    return "http://" + url


# Personal and common info
WEBSITE_MAIN = normalize_url("https://github.com/asvatov/pomodoro-timer")
WEBSITE_BUG_REPORTS = normalize_url("https://github.com/asvatov/pomodoro-timer/issues")
WEBSITE_LAUNCHPAD = normalize_url("https://launchpad.net/~asvatov")

NICKNAME = "hippiest"
NAME = "Evgeniy Asvatov"
YEAR = "2020"
EMAIL = "evgeniy.asvatov@phystech.edu"

DONATE_WMZ = "Z880678669822"
DONATE_BTC = "1AgVEehDxrc4MzPU6yjUM9Fixouu4xjd1M"

LICENSE = "MIT LICENSE"
COPYRIGHT = "Copyright (c) {} {}".format(YEAR, NAME)
COMMENT = "Pomodoro Technique"

# RESOURCES_DIR = os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)), "resources")
# PROJECT_ROOT = os.path.abspath(os.path.join(os.path.abspath(__file__),
#                                             os.pardir))

# ~/.local/share

# RESOURCES_DIR = os.path.join(os.path.abspath(os.getcwd()), "resources")

DATA_DIR = os.path.join("/usr/share", APP)
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# CONFIGS_ROOT_DIR = os.path.join(RESOURCES_DIR, "configs")
CONFIGS_ROOT_DIR = os.path.join(os.path.expanduser("~/.config"), APP)
if not os.path.exists(CONFIGS_ROOT_DIR):
    os.makedirs(CONFIGS_ROOT_DIR)
CONFIGS_APP_DIR = CONFIGS_ROOT_DIR
if not os.path.exists(CONFIGS_APP_DIR):
    os.makedirs(CONFIGS_APP_DIR)

USER_CONFIG_NAME = "user_config.json"
USER_CONFIG_FILE = os.path.join(CONFIGS_APP_DIR, USER_CONFIG_NAME)

TIMER_CONFIG_NAME = "timer_config.json"
TIMER_CONFIG_FILE = os.path.join(CONFIGS_APP_DIR, TIMER_CONFIG_NAME)


# Sound files
SOUNDS_CONFIG_NAME = "sounds_config.json"
SOUNDS_CONFIG_FILE = os.path.join(CONFIGS_APP_DIR, SOUNDS_CONFIG_NAME)
SOUNDS_ROOT_DIR = os.path.join(DATA_DIR, "sounds")

SOUNDS_PARAM_SESSION_START = "session_start"
SOUNDS_PARAM_BREAK_START = "break_start"
SOUNDS_PARAM_SOUND_ON = "sound_on"

SOUNDS_DIR_SESSION_START = os.path.join(SOUNDS_ROOT_DIR, SOUNDS_PARAM_SESSION_START)
SOUNDS_FILES_SESSION_START = os.listdir(SOUNDS_DIR_SESSION_START)
SOUNDS_DIR_BREAK_START = os.path.join(SOUNDS_ROOT_DIR, SOUNDS_PARAM_BREAK_START)
SOUNDS_FILES_BREAK_START = os.listdir(SOUNDS_DIR_BREAK_START)


# Img files
IMG_ROOT_DIR = os.path.join(DATA_DIR, "img")
IMG_START_FILE = os.path.join(IMG_ROOT_DIR, "start.svg")
IMG_PAUSE_FILE = os.path.join(IMG_ROOT_DIR, "pause.svg")
IMG_ICON_FILE = os.path.join(IMG_ROOT_DIR, "test.svg")
IMG_TEMP_DIR = os.path.join(IMG_ROOT_DIR, "tmp")
if not os.path.exists(IMG_TEMP_DIR):
    os.makedirs(IMG_TEMP_DIR)
IMG_ICON_BASE = os.path.join(IMG_TEMP_DIR, "base.svg")


AUTOSTART_FILENAME = "pomodoro-timer.desktop"
AUTOSTART_DIR = os.path.join(os.path.expanduser("~/.config"), 'autostart')
AUTOSTART_ORIGINAL_FILEPATH = os.path.join(DATA_DIR, AUTOSTART_FILENAME)
AUTOSTART_FILEPATH = os.path.join(AUTOSTART_DIR, AUTOSTART_FILENAME)
