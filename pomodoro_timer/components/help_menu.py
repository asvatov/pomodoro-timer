import webbrowser

import gi

from pomodoro_timer.components.about_dialog import on_about_item
from pomodoro_timer.configs.main_configs import WEBSITE_BUG_REPORTS
from pomodoro_timer.configs.strings_config import STRING_ABOUT, STRING_BUGS

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk


def get_dropdown_help_menu():
    help_menu = gtk.Menu()

    item_about = gtk.MenuItem(STRING_ABOUT)
    item_about.connect('activate', lambda x: on_about_item(x))
    item_about.show()
    help_menu.append(item_about)

    bug_item = gtk.MenuItem(STRING_BUGS)
    bug_item.connect('activate', lambda x: webbrowser.open(WEBSITE_BUG_REPORTS))
    bug_item.show()
    help_menu.append(bug_item)

    help_menu.show()

    return help_menu
