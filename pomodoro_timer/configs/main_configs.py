import os
import locale
import gettext

from pomodoro_timer.configs.strings_config import get_quoted


def is_package():
    return os.path.abspath(os.path.dirname(__file__)).startswith('/usr')


def normalize_url(url):
    # prefixes = ["http://", "https://"]

    if url.startswith("http://") or url.startswith("https://"):
        return url

    return "http://" + url


# Personal and common info
WEBSITE_MAIN = normalize_url("ya.ru")
WEBSITE_BUG_REPORTS = normalize_url("https://github.com/asvatov")
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


# CONFIG_DIR = os.path.join(os.path.expanduser('~'), '.config')
CONFIGS_ROOT_DIR = os.path.join(os.path.expanduser('~'), '/home/jentos/Projects/pomodoro-custom/resources/configs')
CONFIGS_APP_DIR = CONFIGS_ROOT_DIR  # os.path.join(CONFIGS_DIR, APP)
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
# SOUNDS_DIR_SESSION_END = os.path.join(SOUNDS_ROOT_DIR, "session_end")
# SOUNDS_FILES_SESSION_END = os.listdir(SOUNDS_DIR_SESSION_END)

# SOUNDS_PARAM_SESSION_END = "session_end"
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

# if is_package():
#     ROOTDIR = '/usr/share/'
#     if 'SNAP' in os.environ:
#         ROOTDIR = os.environ["SNAP"] + ROOTDIR
#     LANGDIR = os.path.join(ROOTDIR, 'locale-langpack')
#     APPDIR = os.path.join(ROOTDIR, APP)
#     ICONDIR = os.path.join(APPDIR, 'icons')
#     SOCIALDIR = os.path.join(APPDIR, 'social')
#     SOUNDIR = os.path.join(APPDIR, 'sounds')
#     FILE_AUTO_START_ORIG = os.path.join(APPDIR, APPAUTOSTART)
# else:
#     ROOTDIR = os.path.dirname(__file__)
#     print(ROOTDIR)
#     LANGDIR = os.path.normpath(os.path.join(ROOTDIR, '../template1'))
#     APPDIR = ROOTDIR
#     ICONDIR = os.path.normpath(os.path.join(APPDIR, '../resources/icons'))
#     SOCIALDIR = os.path.normpath(os.path.join(APPDIR, '../resources/social'))
#     SOUNDIR = os.path.normpath(os.path.join(APPDIR, '../resources/audio'))
#     FILE_AUTO_START_ORIG = os.path.join(os.path.normpath(os.path.join(APPDIR, '../../data')), APPAUTOSTART)

# pos = line.find('(')
# posf = line.find(')', pos)
# VERSION = line[pos+1:posf].strip()
# if not is_package():
#     VERSION = VERSION + '-src'
# try:
#     current_locale, encoding = locale.getdefaultlocale()
#     language = gettext.translation(APP, LANGDIR, [current_locale])
#     language.install()
#     _ = language.gettext
# except Exception as e:
#     _ = str
