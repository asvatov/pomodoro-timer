from pomodoro_timer.configs.app_configs import APP_NAME, APP_VERSION
from pomodoro_timer.configs.main_configs import WEBSITE_MAIN, NAME, WEBSITE_LAUNCHPAD, IMG_ICON_FILE, COPYRIGHT, LICENSE, COMMENT
from pomodoro_timer.configs.strings_config import STRING_VERSION, STRING_ABOUT, get_quoted

import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk
from gi.repository import GdkPixbuf


def get_about_dialog(window):
    """Create and populate the about dialog."""
    about_dialog = gtk.AboutDialog(STRING_ABOUT, window, 0, ())

    about_dialog.set_name(APP_NAME)
    about_dialog.set_version(STRING_VERSION + " " + str(APP_VERSION))
    about_dialog.set_copyright(COPYRIGHT)
    about_dialog.set_comments(COMMENT)
    about_dialog.set_license(LICENSE)
    about_dialog.set_website(WEBSITE_MAIN)
    about_dialog.set_website_label(WEBSITE_MAIN)
    about_dialog.set_authors([NAME + ' ' + get_quoted(WEBSITE_LAUNCHPAD)])
    about_dialog.set_documenters([NAME + ' ' + get_quoted(WEBSITE_LAUNCHPAD)])
    about_dialog.set_translator_credits(NAME + ' ' + get_quoted(WEBSITE_LAUNCHPAD))
    about_dialog.set_icon(GdkPixbuf.Pixbuf.new_from_file(IMG_ICON_FILE))
    about_dialog.set_logo(GdkPixbuf.Pixbuf.new_from_file(IMG_ICON_FILE))
    about_dialog.set_program_name(APP_NAME)

    return about_dialog


def on_about_item(widget, data=None):
    about_dialog = get_about_dialog(widget.get_toplevel())
    about_dialog.run()
    about_dialog.destroy()
