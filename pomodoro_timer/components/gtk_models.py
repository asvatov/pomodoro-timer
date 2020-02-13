import gi

from pomodoro_timer.utils.utils import singleton

gi.require_version("Gtk", "3.0")
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Notify', '0.7')

from gi.repository import Gtk, Gdk
from gi.repository import GObject, Pango


@singleton
class ABoxWindow(Gtk.Window):
    def __init__(self, tickets=0):
        Gtk.Window.__init__(self, title="ListBox Demo")

        self.default_tickets = tickets

        self.set_default_size(350, 600)

        self.connect('delete-event', lambda w, e: w.hide() or True)

        self.scrollers = [None]
        self.buttons = [None]

        self.current_row = 0

        self.scroll_all = Gtk.ScrolledWindow(hexpand=True, vexpand=True)
        self.scroll_all.set_policy(
            Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.scroll_all.set_border_width(5)
        self.scroll_all.set_hexpand(True)
        self.scroll_all.set_vexpand(True)
        self.scroll_all.set_shadow_type(Gtk.ShadowType.IN)
        # scroll_all.add(self)
        self.add(self.scroll_all)

        self.grid = Gtk.Grid()
        self.generate_plus_button()
        # self.add(self.grid)

        self.scroll_all.add(self.grid)

        for x in range(self.default_tickets):
            self.generate_textview_rows(None)

    def save(self):
        for i in range(1, self.current_row):
            text = self.f(i)
            print(text)
            print("-------------------")

    def set_default_tickets(self, tickets_number):
        pass

    def get_scroller(self):
        buffer = Gtk.TextBuffer()
        text_view = Gtk.TextView(buffer=buffer)
        text_view.set_editable(True)
        text_view.set_wrap_mode(Gtk.WrapMode.WORD_CHAR)

        scroller = Gtk.ScrolledWindow()
        scroller.set_border_width(5)
        scroller.set_policy(
            Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scroller.set_hexpand(True)
        scroller.set_vexpand(True)
        scroller.set_shadow_type(Gtk.ShadowType.IN)
        scroller.add(text_view)

        return scroller

    def f(self, row_number):
        textbuffer = self.scrollers[row_number].get_child().get_buffer()
        start_iter = textbuffer.get_start_iter()
        end_iter = textbuffer.get_end_iter()
        text = textbuffer.get_text(start_iter, end_iter, True)

        return text

    def generate_plus_button(self):
        button_plus = Gtk.Button.new_with_label("+")
        button_plus.set_hexpand(True)
        button_plus.connect("clicked", self.generate_textview_rows)

        self.grid.attach(button_plus, 0, self.current_row, 1, 1)

        self.current_row += 1

    def generate_textview_rows(self, widget):

        scroller1 = self.get_scroller()
        self.scrollers.append(scroller1)

        self.grid.attach(self.scrollers[self.current_row], 0, self.current_row, 2, 1)

        button1 = Gtk.Button.new_with_label("x")
        button1.set_property("height-request", 60)
        self.buttons.append(button1)
        num = self.current_row
        self.buttons[self.current_row].connect("clicked", lambda _: print(self.current_row, self.f(num)))

        self.grid.attach(self.buttons[self.current_row], 2, self.current_row, 2, 1)

        check_button1 = Gtk.CheckButton()
        self.grid.attach(check_button1, 4, self.current_row, 2, 1)

        spin_button = Gtk.SpinButton.new_with_range(0, 100, 1)
        spin_button.set_property("width-request", 10)
        spin_button.set_property("height-request", 60)
        self.grid.attach(spin_button, 6, self.current_row, 2, 1)

        switch = Gtk.Switch()
        self.grid.attach(switch, 8, self.current_row, 2, 1)

        self.show_all()

        self.current_row += 1
