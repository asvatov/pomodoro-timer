import os


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
YEAR = "2019"
EMAIL = "evgeniy.asvatov@phystech.edu"

DONATE_WMZ = "Z880678669822"
DONATE_BTC = "1AgVEehDxrc4MzPU6yjUM9Fixouu4xjd1M"

LICENSE = "MIT LICENSE"
COPYRIGHT = "Copyright (c) {} {}".format(YEAR, NAME)
COMMENT = "Pomodoro Technique"


CONFIGS_ROOT_DIR = os.path.join(os.path.expanduser('~'), '/home/jentos/Projects/pomodoro-custom/resources/configs')
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
SOUNDS_ROOT_DIR = os.path.join(os.path.expanduser('~'), '/home/jentos/Projects/pomodoro-custom/resources/sounds')

SOUNDS_PARAM_SESSION_START = "session_start"
SOUNDS_PARAM_BREAK_START = "break_start"
SOUNDS_PARAM_SOUND_ON = "sound_on"

SOUNDS_DIR_SESSION_START = os.path.join(SOUNDS_ROOT_DIR, SOUNDS_PARAM_SESSION_START)
SOUNDS_FILES_SESSION_START = os.listdir(SOUNDS_DIR_SESSION_START)
SOUNDS_DIR_BREAK_START = os.path.join(SOUNDS_ROOT_DIR, SOUNDS_PARAM_BREAK_START)
SOUNDS_FILES_BREAK_START = os.listdir(SOUNDS_DIR_BREAK_START)


# Img files
IMG_ROOT_DIR = "/home/jentos/Projects/pomodoro-custom/resources/img"
IMG_START_FILE = os.path.join(IMG_ROOT_DIR, "start.svg")
IMG_PAUSE_FILE = os.path.join(IMG_ROOT_DIR, "pause.svg")
IMG_ICON_FILE = os.path.join(IMG_ROOT_DIR, "test.svg")
IMG_TEMP_DIR = "/home/jentos/Projects/pomodoro-custom/resources/img/tmp"
IMG_BASE_DIR = os.path.join(IMG_ROOT_DIR, "base")
IMG_ICON_BASE = os.path.join(IMG_BASE_DIR, "base.svg")


# AUTOSTART_DIR = os.path.join(CONFIGS_DIR, 'autostart')
# FILE_AUTO_START = os.path.join(AUTOSTART_DIR, APPAUTOSTART)
