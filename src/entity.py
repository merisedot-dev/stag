from gi.repository import Gtk


@Gtk.Template(resourcepath="/com/github/merisedotdev/stag/entity.ui")
class StagEntityEditor(Gtk.Box):
    """Entity editor interface.
    """
    __gtype_name__ = "StagEntityEditor"

    def __init__(self) -> None:
        super().__init__()
