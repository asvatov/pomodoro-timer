# coding: utf-8

# import dbus

from pomodoro_timer.components.help_menu import get_dropdown_help_menu
from pomodoro_timer.configs.app_configs import APP_INDICATOR_ID, APP_DBUS_NAME
from pomodoro_timer.configs.strings_config import STRING_RESET, STRING_STATS, \
    STRING_HELP, STRING_QUIT, STRING_PREFERENCES, STRING_STATE_IDLE, STRING_STATE_WORK, STRING_STATE_BREAK, \
    STRING_STATE_LONG_BREAK
from pomodoro_timer.configs.timer_configs import SECOND
from pomodoro_timer.managers.session_manager import SessionManager, SESSION_START_PAUSE_TEXT_DEFAULT, SESSION_START_PAUSE_IMG_DEFAULT
from pomodoro_timer.managers.sound_manager import SoundManager
from pomodoro_timer.managers.time_manager import TimerManager
from pomodoro_timer.components.preferences_dialog import on_preferences_item
from pomodoro_timer.fsm import TimerFSM, ContinueEvent, StartEvent, PauseEvent, ResetEvent, FSM_STATE_RUN, FSM_STATE_IDLE, \
    FSM_STATE_PAUSED, FSM_STATE_BREAK, StartBreakEvent
from pomodoro_timer.utils.gtk_utils import ChangeableImageMenuItem, ChangeableMenuItem
from pomodoro_timer.utils.icon_utils import remove_temp_img

import os
import signal
import warnings

import gi

from pomodoro_timer.utils.svg_utils import get_icon
from pomodoro_timer.utils.utils import get_random_filename

gi.require_version("Gtk", "3.0")
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Notify', '0.7')

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify
from gi.repository import GObject


warnings.filterwarnings("ignore")


def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


@singleton
class Indicator(GObject.Object):

    def init(self):
        self.timer_manager = TimerManager()
        self.sound_manager = SoundManager()

        self.session = SessionManager(timer_manager=self.timer_manager,
                                      sound_manager=self.sound_manager)

        self.fsm = TimerFSM(self.session)

        notify.init(APP_INDICATOR_ID)

        self.changeable_item = ChangeableImageMenuItem(SESSION_START_PAUSE_TEXT_DEFAULT,
                                                       SESSION_START_PAUSE_IMG_DEFAULT)

        self.changeable_item2 = ChangeableMenuItem(STRING_STATE_IDLE)

        self.indicator = appindicator.Indicator.new(APP_INDICATOR_ID, os.path.abspath(self.session.icon_filepath),
                                                    appindicator.IndicatorCategory.SYSTEM_SERVICES)
        self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.build_menu())

        self.ticking = False
        self.prev_state_state = None

    def change_icon(self, arc):
        icon = get_icon(arc)
        buff_filepath = os.path.join(os.path.dirname(self.session.icon_filepath), get_random_filename())
        os.rename(self.session.icon_filepath, buff_filepath)
        self.session.icon_filepath = buff_filepath

        with open(self.session.icon_filepath, "w") as fp:
            fp.write(icon)

        self.indicator.set_icon_full(os.path.abspath(self.session.icon_filepath), "0")

    def do_tick(self):
        current_state_code = self.fsm.get_state_code()

        if current_state_code == FSM_STATE_RUN:
            self.ticking = True
            if current_state_code != self.prev_state_state:
                self.changeable_item2.set_item_data(STRING_STATE_WORK)

        elif current_state_code == FSM_STATE_BREAK:
            self.ticking = True
            if current_state_code != self.prev_state_state:
                if self.session.is_it_long_break():
                    self.changeable_item2.set_item_data(STRING_STATE_LONG_BREAK)
                else:
                    self.changeable_item2.set_item_data(STRING_STATE_BREAK)

        else:
            self.ticking = False

            if current_state_code == FSM_STATE_IDLE:
                self.change_icon(0)
                self.changeable_item2.set_item_data(STRING_STATE_IDLE)

            self.prev_state_state = current_state_code

            return self.ticking

        self.prev_state_state = current_state_code

        self.session.timer += 1
        self.change_icon(self.session.timer / self.session.duration)
        if self.session.timer == self.session.duration:
            if self.fsm.get_state_code() == FSM_STATE_RUN:
                self.fsm.on_event(StartBreakEvent())
            elif self.fsm.get_state_code() == FSM_STATE_BREAK:
                self.fsm.on_event(StartEvent())

        return self.ticking

    def set_ticker(self):
        GObject.timeout_add(SECOND, self.do_tick)

    def press_start_pause(self, x):
        if self.fsm.get_state_code() == FSM_STATE_PAUSED:
            self.fsm.on_event(ContinueEvent())
        elif self.fsm.get_state_code() == FSM_STATE_IDLE:
            self.fsm.on_event(StartEvent())
        else:
            self.fsm.on_event(PauseEvent())

        self.changeable_item.set_item_data(self.session.start_pause_text, self.session.start_pause_img_filepath)

        if not self.ticking:
            self.ticking = True
            self.set_ticker()

    def press_reset(self, x):
        self.fsm.on_event(ResetEvent())
        self.changeable_item.set_item_data(SESSION_START_PAUSE_TEXT_DEFAULT, SESSION_START_PAUSE_IMG_DEFAULT)

    def build_menu(self):
        menu = gtk.Menu()

        menu_state_info = self.changeable_item2.get()
        menu_state_info.set_sensitive(False)
        menu_state_info.show()
        menu.append(menu_state_info)

        menu_sep = gtk.SeparatorMenuItem()
        menu.append(menu_sep)

        menu_start_pause_item = self.changeable_item.get()
        menu_start_pause_item.connect('activate', self.press_start_pause)
        menu.append(menu_start_pause_item)

        menu_reset_item = gtk.MenuItem(STRING_RESET)
        menu_reset_item.connect('activate', self.press_reset)
        menu.append(menu_reset_item)

        menu_sep = gtk.SeparatorMenuItem()
        menu.append(menu_sep)

        menu_stats = gtk.MenuItem(STRING_STATS)
        menu_stats.set_sensitive(False)
        menu_stats.show()
        menu.append(menu_stats)

        menu_sep = gtk.SeparatorMenuItem()
        menu.append(menu_sep)

        menu_preferences = gtk.MenuItem(STRING_PREFERENCES)
        menu_preferences.connect('activate',
                                 lambda x: on_preferences_item(x, menu.get_parent(),
                                                               timer_manager=self.timer_manager,
                                                               sound_manager=self.sound_manager))
        menu_preferences.show()
        menu.append(menu_preferences)

        menu_help = gtk.MenuItem(STRING_HELP)
        menu_help.set_submenu(get_dropdown_help_menu())
        menu_help.show()
        menu.append(menu_help)

        menu_sep = gtk.SeparatorMenuItem()
        menu.append(menu_sep)

        item_quit = gtk.MenuItem(STRING_QUIT)
        item_quit.connect('activate', self.quit)
        menu.append(item_quit)

        menu.show_all()

        return menu

    def quit(self, source):
        notify.uninit()
        remove_temp_img()
        gtk.main_quit()


def main():
    # dbus_response = dbus.SessionBus().request_name(APP_DBUS_NAME)
    # if dbus_response != dbus.bus.REQUEST_NAME_REPLY_PRIMARY_OWNER:
    #     exit(1)
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    indicator = Indicator()
    indicator.init()
    GObject.threads_init()
    gtk.main()


if __name__ == "__main__":
    main()
