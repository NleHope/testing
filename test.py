import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class SlideOver(Gtk.Window):
    def __init__(self):
        super().__init__(title="SlideOver")
        self.set_default_size(400, 600)
        self.set_decorated(False)
        self.set_keep_above(True)
        self.set_gravity(Gdk.Gravity.EAST)
        self.set_margin_end(0)
        self.set_margin_top(100)
        self.set_margin_bottom(0)

        label = Gtk.Label(label="SlideOver Window")
        self.set_child(label)

        self.connect("close-request", Gtk.main_quit)

win = SlideOver()
win.present()
Gtk.main()
