import os

from pomodoro_timer.configs.main_configs import SOUNDS_CONFIG_FILE
from pomodoro_timer.configs.sounds_configs import DEFAULT_SOUNDS_PARAMS
from pomodoro_timer.managers.manager import Manager


class SoundManager(Manager):
    config_file = SOUNDS_CONFIG_FILE
    default_params = DEFAULT_SOUNDS_PARAMS

    def get(self, key, directory=""):
        try:
            res = os.path.join(directory, self._params[key])
        except TypeError:
            res = self._params[key]

        return res
