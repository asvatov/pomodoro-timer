import os

import gi
gi.require_version("Gtk", "3.0")
gi.require_version('Notify', '0.7')

from gi.repository import Gtk as gtk
from gi.repository import Notify as notify


def get_selected_value_in_combo(combo):
    model = combo.get_model()

    return model.get_value(combo.get_active_iter(), 1)


def select_value_in_combo(combo, value):
    model = combo.get_model()
    for i, item in enumerate(model):
        if value == item[1]:
            combo.set_active(i)

            return

    combo.set_active(0)


class Notification:
    def __init__(self, header, notification_content, notification_icon_filepath=None):
        self.header = header
        self.notification_content = notification_content
        self.notification_icon_filepath = self.format_notification_icon(notification_icon_filepath)
        self.notification = self.create_notification()

    def format_notification_icon(self, notification_icon_filepath):
        try:
            return os.path.abspath(notification_icon_filepath)
        except Exception:
            pass

        return None

    def create_notification(self):
        notification = notify.Notification.new(self.header, self.notification_content, self.notification_icon_filepath)
        # notification.set_timeout(notify.EXPIRES_NEVER)
        notification.set_urgency(notify.Urgency.CRITICAL)

        return notification

    def get(self, notification_content=None):
        if notification_content is None:
            return self.notification
        self.notification_content = notification_content
        self.notification = self.create_notification()

        return self.notification


def set_menu_text(item, text):
    item.get_child().set_text(text)


class ChangeableMenuItem:
    def __init__(self, text=""):
        self.text = text
        self.menu_item = gtk.MenuItem(self.text)

    def set_text(self, text):
        self.menu_item.get_child().set_text(text)

    def set_item_data(self, text):
        self.set_text(text)

    def get(self):
        return self.menu_item


class ChangeableImageMenuItem:
    def __init__(self, text="", image_filepath=""):
        self.text = text
        self.image_filepath = image_filepath

        self.image_menu_item = gtk.ImageMenuItem(self.text)
        self.img = gtk.Image()
        self.img.set_from_file(self.image_filepath)
        self.image_menu_item.set_image(self.img)
        self.image_menu_item.set_always_show_image(True)

    def set_img(self, image_filepath):
        self.image_filepath = image_filepath
        self.img.set_from_file(self.image_filepath)

    def set_text(self, text):
        self.image_menu_item.get_child().set_text(text)

    def set_item_data(self, text, image_filepath):
        self.set_text(text)
        self.set_img(image_filepath)

    def get(self):
        return self.image_menu_item
