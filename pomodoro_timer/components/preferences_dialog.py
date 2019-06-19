import gi

from pomodoro_timer.configs.app_configs import APP_NAME
from pomodoro_timer.configs.main_configs import IMG_ICON_FILE, SOUNDS_FILES_SESSION_START, \
    SOUNDS_FILES_BREAK_START, SOUNDS_PARAM_BREAK_START
from pomodoro_timer.configs.sounds_configs import SOUNDS_PARAM_SESSION_START, SOUNDS_PARAM_SOUND_ON
from pomodoro_timer.configs.strings_config import STRING_PREFERENCES, STRING_MAIN, STRING_SOUND, STRING_OTHER, STRING_PREF_1, \
    STRING_PREF_2, STRING_PREF_3, STRING_PREF_4, STRING_PREF_5, STRING_PREF_6, STRING_PREF_7, STRING_PREF_8, \
    COLON, get_bold
from pomodoro_timer.configs.timer_configs import TIMER_PARAM_NUM_POMODOROS, TIMER_PARAM_SESSION_LENGTH, TIMER_PARAM_BREAK_LENGTH, \
    TIMER_PARAM_LONG_BREAK_LENGTH
from pomodoro_timer.managers.user_manager import UserManager, USER_PARAM_AUTOSTART
from pomodoro_timer.utils.gtk_utils import get_selected_value_in_combo, select_value_in_combo

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk


class PreferencesDialog(gtk.Dialog):
    def __init__(self, widget, timer_manager=None, sound_manager=None):
        self.timer_manager = timer_manager
        self.sound_manager = sound_manager
        self.user_manager = UserManager()

        gtk.Dialog.__init__(self, APP_NAME + ' | ' + STRING_PREFERENCES,
                            widget,
                            gtk.DialogFlags.MODAL |
                            gtk.DialogFlags.DESTROY_WITH_PARENT,
                            (gtk.STOCK_CANCEL, gtk.ResponseType.REJECT,
                             gtk.STOCK_OK, gtk.ResponseType.ACCEPT))
        self.set_position(gtk.WindowPosition.CENTER_ALWAYS)
        self.connect('close', self.close_application)
        self.set_icon_from_file(IMG_ICON_FILE)

        vbox0 = gtk.VBox(spacing=5)
        vbox0.set_border_width(5)
        self.get_content_area().add(vbox0)

        notebook = gtk.Notebook.new()
        vbox0.add(notebook)

        vbox1 = gtk.VBox(spacing=5)
        vbox1.set_border_width(5)
        notebook.append_page(vbox1, gtk.Label.new(STRING_MAIN))
        frame1 = gtk.Frame()
        vbox1.pack_start(frame1, False, True, 1)
        table1 = gtk.Table(8, 2, False)
        frame1.add(table1)

        label0 = gtk.Label(STRING_PREF_1 + COLON)
        label0.set_alignment(0, 0.5)
        table1.attach(label0, 0, 1, 0, 1, xpadding=5, ypadding=5)
        self.spinbutton0 = gtk.SpinButton()
        self.spinbutton0.set_adjustment(gtk.Adjustment(2, 1, 20, 1, 10, 0))
        table1.attach(self.spinbutton0, 1, 2, 0, 1, xpadding=5, ypadding=5)

        label1 = gtk.Label(STRING_PREF_2 + COLON)
        label1.set_alignment(0, 0.5)
        table1.attach(label1, 0, 1, 1, 2, xpadding=5, ypadding=5)
        self.spinbutton1 = gtk.SpinButton()
        self.spinbutton1.set_adjustment(gtk.Adjustment(25, 1, 1440, 1, 10, 0))
        table1.attach(self.spinbutton1, 1, 2, 1, 2, xpadding=5, ypadding=5)

        label2 = gtk.Label(STRING_PREF_3 + COLON)
        label2.set_alignment(0, 0.5)
        table1.attach(label2, 0, 1, 2, 3, xpadding=5, ypadding=5)
        self.spinbutton2 = gtk.SpinButton()
        self.spinbutton2.set_adjustment(gtk.Adjustment(25, 1, 1440, 1, 10, 0))
        table1.attach(self.spinbutton2, 1, 2, 2, 3, xpadding=5, ypadding=5)

        label_long_break = gtk.Label(STRING_PREF_4 + COLON)
        label_long_break.set_alignment(0, 0.5)
        table1.attach(label_long_break, 0, 1, 3, 4, xpadding=5, ypadding=5)
        self.spinbutton3 = gtk.SpinButton()
        self.spinbutton3.set_adjustment(gtk.Adjustment(25, 1, 1440, 1, 10, 0))
        table1.attach(self.spinbutton3, 1, 2, 3, 4, xpadding=5, ypadding=5)


        vbox2 = gtk.VBox(spacing=5)
        vbox2.set_border_width(5)
        notebook.append_page(vbox2, gtk.Label.new(STRING_SOUND))
        frame2 = gtk.Frame()
        vbox2.pack_start(frame2, False, True, 1)
        table2 = gtk.Table(8, 2, False)
        frame2.add(table2)

        label4 = gtk.Label(STRING_PREF_5 + COLON)
        label4.set_alignment(0, 0.5)
        table2.attach(label4, 0, 1, 4, 5, xpadding=5, ypadding=5)
        self.switch4 = gtk.Switch()
        table2.attach(self.switch4, 1, 2, 4, 5, xpadding=5, ypadding=5,
                      xoptions=gtk.AttachOptions.SHRINK)

        sounds_end_session = gtk.ListStore(str, str)
        for i, sound in enumerate(SOUNDS_FILES_BREAK_START):
            sound_tuple = (sound, sound)
            sounds_end_session.append(sound_tuple)
        label5 = gtk.Label(STRING_PREF_6 + COLON)
        label5.set_alignment(0, 0.5)
        table2.attach(label5, 0, 1, 5, 6, xpadding=5, ypadding=5)
        self.comboboxsound5 = gtk.ComboBox.new()
        self.comboboxsound5.set_model(sounds_end_session)
        cell1 = gtk.CellRendererText()
        self.comboboxsound5.pack_start(cell1, True)
        self.comboboxsound5.add_attribute(cell1, 'text', 0)
        table2.attach(self.comboboxsound5, 1, 2, 5, 6,
                      xoptions=gtk.AttachOptions.FILL,
                      yoptions=gtk.AttachOptions.FILL,
                      xpadding=5,
                      ypadding=5)

        sounds_end_break = gtk.ListStore(str, str)
        for i, sound in enumerate(SOUNDS_FILES_SESSION_START):
            sound_tuple = (sound, sound)  # str(i))
            sounds_end_break.append(sound_tuple)
        label6 = gtk.Label(STRING_PREF_7 + COLON)
        label6.set_alignment(0, 0.5)
        table2.attach(label6, 0, 1, 6, 7, xpadding=5, ypadding=5)
        self.comboboxsound6 = gtk.ComboBox.new()
        self.comboboxsound6.set_model(sounds_end_break)
        cell1 = gtk.CellRendererText()
        self.comboboxsound6.pack_start(cell1, True)
        self.comboboxsound6.add_attribute(cell1, 'text', 0)
        table2.attach(self.comboboxsound6, 1, 2, 6, 7,
                      xoptions=gtk.AttachOptions.FILL,
                      yoptions=gtk.AttachOptions.FILL,
                      xpadding=5,
                      ypadding=5)


        vbox3 = gtk.VBox(spacing=5)
        vbox3.set_border_width(5)
        notebook.append_page(vbox3, gtk.Label.new(STRING_OTHER))
        frame3 = gtk.Frame()
        vbox3.pack_start(frame3, False, True, 1)
        table3 = gtk.Table(8, 2, False)
        frame3.add(table3)

        label7 = gtk.Label(STRING_PREF_8 + COLON)
        label7.set_alignment(0, 0.5)
        table3.attach(label7, 0, 1, 7, 8, xpadding=5, ypadding=5)
        self.switch7 = gtk.Switch()
        table3.attach(self.switch7, 1, 2, 7, 8, xpadding=5, ypadding=5,
                      xoptions=gtk.AttachOptions.SHRINK)

        self.load_timer_preferences()
        self.load_sounds_preferences()
        self.load_user_preferences()

        self.show_all()

    def close_application(self, widget, event):
        self.hide()

    def messagedialog(self, title, message):
        dialog = gtk.MessageDialog(None,
                                   gtk.DialogFlags.MODAL,
                                   gtk.MessageType.INFO,
                                   buttons=gtk.ButtonsType.OK)
        dialog.set_markup(get_bold(title))
        dialog.format_secondary_markup(message)
        dialog.run()
        dialog.destroy()

    def close_ok(self):
        self.save_preferences()

    def load_timer_preferences(self):
        self.spinbutton0.set_value(self.timer_manager.get(TIMER_PARAM_NUM_POMODOROS))
        self.spinbutton1.set_value(self.timer_manager.get(TIMER_PARAM_SESSION_LENGTH))
        self.spinbutton2.set_value(self.timer_manager.get(TIMER_PARAM_BREAK_LENGTH))
        self.spinbutton3.set_value(self.timer_manager.get(TIMER_PARAM_LONG_BREAK_LENGTH))

    def load_sounds_preferences(self):
        self.switch4.set_active(self.sound_manager.get(SOUNDS_PARAM_SOUND_ON))
        select_value_in_combo(self.comboboxsound5,
                              self.sound_manager.get(SOUNDS_PARAM_BREAK_START))
        select_value_in_combo(self.comboboxsound6,
                              self.sound_manager.get(SOUNDS_PARAM_SESSION_START))

    def load_user_preferences(self):
        self.switch7.set_active(self.user_manager.get(USER_PARAM_AUTOSTART))

    def save_preferences(self):
        self.timer_manager.set(TIMER_PARAM_NUM_POMODOROS, self.spinbutton0.get_value())
        self.timer_manager.set(TIMER_PARAM_SESSION_LENGTH, self.spinbutton1.get_value())
        self.timer_manager.set(TIMER_PARAM_BREAK_LENGTH, self.spinbutton2.get_value())
        self.timer_manager.set(TIMER_PARAM_LONG_BREAK_LENGTH, self.spinbutton3.get_value())
        self.timer_manager.save()

        self.sound_manager.set(SOUNDS_PARAM_SOUND_ON, self.switch4.get_active())
        self.sound_manager.set(SOUNDS_PARAM_BREAK_START,
                               get_selected_value_in_combo(self.comboboxsound5))
        self.sound_manager.set(SOUNDS_PARAM_SESSION_START,
                               get_selected_value_in_combo(self.comboboxsound6))
        self.sound_manager.save()

        self.user_manager.set(USER_PARAM_AUTOSTART, self.switch7.get_active())
        self.user_manager.save()


def on_preferences_item(widget, parent, **kwargs):
    widget.set_sensitive(False)
    preferences_dialog = PreferencesDialog(parent, **kwargs)
    if preferences_dialog.run() == gtk.ResponseType.ACCEPT:
        preferences_dialog.close_ok()
    preferences_dialog.hide()
    preferences_dialog.destroy()
    widget.set_sensitive(True)
