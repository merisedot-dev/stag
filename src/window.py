from gi.repository import Adw, Gio, Gtk, GObject

from .project import StagProject

# screen-related constants
DEFAULT_SCREEN_NAME: str = "welcome"
WORKSPACE_SCREEN_NAME: str = "workspace"
PROJECT_FORM_SCREEN_NAME: str = "project_form"


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
    newproj_btn = Gtk.Template.Child()

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

    # editor kids
    editor_stack = Gtk.Template.Child()
    entity_editor = Gtk.Template.Child()

    # toolbar kids
    # TODO write that part of the interface first

    def __init__(self, **kwargs) -> None:
        self._project: StagProject = None
        self._tmp_project: StagProject = None
        # GTK tools
        self._actions = {}  # actions dict for persistance
        # GTK constructors like to do things
        super().__init__(**kwargs)
        # stateless actions linking
        for action in [
                "add_db", "add_script", "cancel", "close", "mk_proj", "open",
                "save", "validate"
        ]:
            gaction = Gio.SimpleAction.new(action, None)
            gaction.connect("activate", getattr(self, f"on_{action}"))
            self._actions[action] = gaction
            self.add_action(gaction)
        # TODO link other parts of the GUI

    # PROPERTIES
    @GObject.Property(type=StagProject)
    def project(self) -> StagProject:
        return self._project

    # INTERMEDIATES
    def _set_page(self, page_name: str) -> None:
        """Change displayed screen.
        :param page_name: the name of the page to display
        """
        self.stack.set_visible_child_name(page_name)

    # STATELESS ACTIONS

    def on_add_db(self, action, data) -> None:
        pass  # TODO

    def on_add_script(self, action, data) -> None:
        pass  # TODO

    def on_cancel(self, action, data) -> None:
        self._tmp_project = None
        self._set_page(DEFAULT_SCREEN_NAME
                       if not self._project else WORKSPACE_SCREEN_NAME)

    def on_close(self, action, data) -> None:
        self._project = None
        self._set_page(DEFAULT_SCREEN_NAME)

    def on_mk_proj(self, action, data) -> None:
        self._tmp_project = StagProject()  # empty project for now
        self._set_page(PROJECT_FORM_SCREEN_NAME)

    def on_open(self, action, data) -> None:
        pass  # TODO

    def on_save(self, action, data) -> None:
        pass  # TODO

    def on_validate(self, action, data) -> None:
        if not self._project:
            self._project = self._tmp_project
            self._tmp_project = None
            self._set_page(WORKSPACE_SCREEN_NAME)
        else:  # TODO find a way to build a popup
            self._set_page(DEFAULT_SCREEN_NAME)
