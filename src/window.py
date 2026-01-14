from gi.repository import Adw
from gi.repository import Gio
from gi.repository import GObject
from gi.repository import Gtk


@Gtk.Template(resource_path='/com/github/merisedotdev/stag/window.ui')
class StagWindow(Adw.ApplicationWindow):
    """The root window.
    While other components may be defined later on, this may be the only thing
    allowed to use the `Adw.ApplicationWindow` type for the template.
    """
    __gtype_name__ = 'StagWindow'

    # headerbar kids
    header = Gtk.Template.Child()
    open_btn = Gtk.Template.Child()
    undo_btn = Gtk.Template.Child()
    redo_btn = Gtk.Template.Child()
    mainmenu_btn = Gtk.Template.Child()

    # stack kids
    stack = Gtk.Template.Child()
    stag_logo = Gtk.Template.Child()
    version_lbl = Gtk.Template.Child()

    # project creation form kids
    proj_name = Gtk.Template.Child()
    mysql_selector = Gtk.Template.Child()
    cancel_btn = Gtk.Template.Child()
    path_picker = Gtk.Template.Child()
    path_picker_lbl = Gtk.Template.Child()

    def __init__(self, **kwargs) -> None:
        # TODO define performed actions stack
        self._actions = {}  # actions dict for persistance
        # GTK constructors like to do things
        super().__init__(**kwargs)
        # stateless actions linking
        for action in [
                "add_db", "add_script", "close", "mk_proj", "open", "save"
        ]:
            gaction = Gio.SimpleAction.new(action, None)
            gaction.connect("activate", getattr(self, f"on_{action}"))
            self._actions[action] = gaction
            self.add_action(gaction)
        # TODO link other parts of the GUI

    # PROPERTIES
    # TODO

    # SPECIFIC CALLBACKS
    @Gtk.Template.Callback()
    def cancel_btn_clicked(self, button) -> None:
        pass  # TODO

    @Gtk.Template.Callback()
    def validate_btn_clicked(self, button) -> None:
        pass  # TODO

    # STATELESS ACTIONS

    def on_add_db(self, action, data) -> None:
        pass  # TODO

    def on_add_script(self, action, data) -> None:
        pass  # TODO

    def on_close(self, action, data) -> None:
        pass  # TODO

    def on_mk_proj(self, action, data) -> None:
        pass  # TODO

    def on_open(self, action, data) -> None:
        pass  # TODO

    def on_save(self, action, data) -> None:
        pass  # TODO
