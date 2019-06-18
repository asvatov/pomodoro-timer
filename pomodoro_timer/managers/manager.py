import codecs
import json
import os

from pomodoro_timer.configs.main_configs import CONFIGS_APP_DIR


class Manager:
    config_file = None
    default_params = None

    def __init__(self):
        self._params = None
        try:
            f = codecs.open(self.config_file, "r", "utf-8")
            self._params = json.loads(f.read())
        except:
            self.set_defaults()

    def set_defaults(self):
        self._params = self.default_params
        self.save()

    def get(self, key):
        return self._params[key]

    def set(self, key, value):
        self._params[key] = value
        # May be save() ?

    def reset(self):
        if os.path.exists(self.config_file):
            os.remove(self.config_file)
        self.set_defaults()

    def save(self):
        if not os.path.exists(CONFIGS_APP_DIR):
            os.makedirs(CONFIGS_APP_DIR)
        f = codecs.open(self.config_file, "w", "utf-8")
        f.write(json.dumps(self._params))
        f.close()
