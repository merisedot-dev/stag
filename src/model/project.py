from gi.repository import GObject


class MGTKProject(GObject.Object):
    """Project modelling class.
    A project is defined as a set of MCD and MLD graphs that can reference each
    other, as well as SQL scripts resulting of the user's work.
    """
    __gtype_name__ = "MGTKPRoject"

    def __init__(self, name: str, **kwargs) -> None:
        self._name = name
        # gtk constructor call
        super().__init__(**kwargs)
