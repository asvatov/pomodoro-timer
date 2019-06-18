# from configs.timer_configs import DEFAULT_TIMER_PARAMS
from pomodoro_timer.configs.main_configs import USER_CONFIG_FILE
from pomodoro_timer.managers.manager import Manager


USER_PARAM_AUTOSTART = "autostart"
DEFAULT_USER_PARAMS = {
    USER_PARAM_AUTOSTART: False
}


class UserManager(Manager):
    config_file = USER_CONFIG_FILE
    default_params = DEFAULT_USER_PARAMS
