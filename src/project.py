import gi

from gi.repository import GObject


class StagProject(GObject.Object):
    """Project modelling class.
    """
    __gtype_name__ = "StagProject"

    def __init__(self, name: str) -> None:
        super().__init__()
        self._name = name
