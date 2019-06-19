from pydub import AudioSegment

from pomodoro_timer.configs.main_configs import IMG_START_FILE, IMG_PAUSE_FILE, \
    SOUNDS_DIR_SESSION_START, SOUNDS_PARAM_SESSION_START, SOUNDS_PARAM_BREAK_START, SOUNDS_DIR_BREAK_START, \
    IMG_ICON_FILE, SOUNDS_PARAM_SOUND_ON
from pomodoro_timer.configs.strings_config import STRING_START, STRING_PAUSE, get_bold, STRING_NOTIFY_START, \
    STRING_NOTIFY_END
from pomodoro_timer.configs.timer_configs import TIMER_PARAM_NUM_POMODOROS, TIMER_PARAM_SESSION_LENGTH, \
    TIMER_PARAM_LONG_BREAK_LENGTH, TIMER_PARAM_BREAK_LENGTH, MINUTE
from pomodoro_timer.managers.sound_manager import SoundManager
from pomodoro_timer.managers.time_manager import TimerManager
from pomodoro_timer.utils.gtk_utils import Notification
from pomodoro_timer.utils.svg_utils import init_icon
from pomodoro_timer.utils.utils import play_sound

SESSION_START_PAUSE_TEXT_DEFAULT = STRING_START
SESSION_START_PAUSE_IMG_DEFAULT = IMG_START_FILE


def get_notification_start(duration):
    return "Stay focused for {} minutes {} seconds".format(int(duration / MINUTE), int(duration % MINUTE))


def get_notification_break(duration):
    return "Break for {} minutes {} seconds".format(int(duration / MINUTE), int(duration % MINUTE))


class SessionManager:
    def __init__(self, timer_manager=None, sound_manager=None):
        self.sound_manager = sound_manager or SoundManager()
        self.timer_manager = timer_manager or TimerManager()

    def set_default_session_params(self):
        self.timer = 0
        self.duration = 0
        self.pomodoros = 0
        self.icon_filepath = init_icon()

        self.start_pause_text = SESSION_START_PAUSE_TEXT_DEFAULT
        self.start_pause_img_filepath = SESSION_START_PAUSE_IMG_DEFAULT

    def play_sound_work_session_started(self):
        if not self.sound_manager.get(SOUNDS_PARAM_SOUND_ON):
            return
        sound = AudioSegment.from_wav(self.sound_manager.get(SOUNDS_PARAM_SESSION_START,
                                                             directory=SOUNDS_DIR_SESSION_START))
        play_sound(sound)

    def play_sound_break_session_started(self):
        if not self.sound_manager.get(SOUNDS_PARAM_SOUND_ON):
            return
        sound = AudioSegment.from_wav(self.sound_manager.get(SOUNDS_PARAM_BREAK_START,
                                                             directory=SOUNDS_DIR_BREAK_START))
        play_sound(sound)

    def get_notification_work_session_started(self):
        notification = Notification(get_bold(STRING_NOTIFY_START),
                                             get_notification_start(
                                                self.duration - self.timer),
                                             IMG_START_FILE).get()

        return notification

    def get_notification_break_session_started(self):
        notification = Notification(get_bold(STRING_NOTIFY_END),
                                             get_notification_break(
                                                self.duration - self.timer),
                                             IMG_ICON_FILE).get()

        return notification

    def start_work_session(self):
        if self.timer == self.duration:
            self.timer = 0

        self.duration = self.timer_manager.get(TIMER_PARAM_SESSION_LENGTH) * MINUTE

        self.start_pause_text = STRING_PAUSE
        self.start_pause_img_filepath = IMG_PAUSE_FILE

        if self.timer == 0:
            self.play_sound_work_session_started()
            self.get_notification_work_session_started().show()

    def start_break_session(self):
        if self.timer == self.duration:
            self.timer = 0
            self.pomodoros += 1

        if self.pomodoros % self.timer_manager.get(TIMER_PARAM_NUM_POMODOROS) == 0:
            self.duration = self.timer_manager.get(TIMER_PARAM_LONG_BREAK_LENGTH) * MINUTE
        else:
            self.duration = self.timer_manager.get(TIMER_PARAM_BREAK_LENGTH) * MINUTE

        self.start_pause_text = STRING_PAUSE
        self.start_pause_img_filepath = IMG_PAUSE_FILE

        if self.timer == 0:
            self.play_sound_break_session_started()
            self.get_notification_break_session_started().show()

    def pause_session(self):
        self.start_pause_text = STRING_START
        self.start_pause_img_filepath = IMG_START_FILE
