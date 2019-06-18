from pomodoro_timer.configs.app_configs import APP, APP_VERSION
from pomodoro_timer.configs.main_configs import NICKNAME, EMAIL, COPYRIGHT, LICENSE, WEBSITE_MAIN
from pomodoro_timer.configs.strings_config import get_quoted

name = APP  # "pomodoro-timer"
__version__ = APP_VERSION
__author__ = NICKNAME + " " + get_quoted(EMAIL)
__copyright__ = COPYRIGHT
__license__ = LICENSE
__url__ = WEBSITE_MAIN
