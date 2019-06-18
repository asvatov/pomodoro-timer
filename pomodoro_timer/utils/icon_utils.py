import glob
import os

from pomodoro_timer.configs.main_configs import IMG_TEMP_DIR


def remove_temp_img():
    files = glob.glob(os.path.join(IMG_TEMP_DIR, "*"))
    for f in files:
        os.remove(f)
