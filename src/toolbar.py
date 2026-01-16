from gi.repository import Gtk


@Gtk.Template(resource_path="/com/github/merisedotdev/stag/toolbar.ui")
class StagToolbar(Gtk.Box):
    __gtype_name__ = "StagToolbar"

    # TODO fetch kids
    mkentity_btn = Gtk.Template.Child()
    mklink_btn = Gtk.Template.Child()

    def __init__(self) -> None:
        super().__init__()
