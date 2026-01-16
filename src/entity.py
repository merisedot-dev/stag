from gi.repository import Gtk


@Gtk.Template(resource_path="/com/github/merisedotdev/stag/entity.ui")
class StagEntityEditor(Gtk.Box):
    """Entity editor interface.
    """
    __gtype_name__ = "StagEntityEditor"

    # TODO fetch kids
    stack = Gtk.Template.Child()

    def __init__(self) -> None:
        super().__init__()
