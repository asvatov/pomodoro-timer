from pomodoro_timer.configs.timer_configs import DEFAULT_TIMER_PARAMS
from pomodoro_timer.configs.main_configs import TIMER_CONFIG_FILE
from pomodoro_timer.managers.manager import Manager


class TimerManager(Manager):
    config_file = TIMER_CONFIG_FILE
    default_params = DEFAULT_TIMER_PARAMS
