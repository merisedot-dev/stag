import gi

from gi.repository import GObject


class StagProject(GObject.Object):
    """Project modelling class.
    For this application, a *project* is defined as a set of files indexed by a root
    `mdot` file. Yes, this is not a standard filetype. The indexed files cover :
    - MCD graphs
    - MLD graphs
    - SQL creation scripts
    """
    __gtype_name__ = "StagProject"

    def __init__(self, name: str = "") -> None:
        # TODO define target sgbd choices in the project.
        # TODO define index file path
        # TODO define file/path dict
        super().__init__()
        self._name = name
        self._paths: dict[str | str] = {}

    def set_name(self, name: str) -> None:
        """Change the project's name.
        This will impact the index filename, as it follows
        """
