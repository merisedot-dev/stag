# window.py
#
# Copyright 2026 kheldae
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw
from gi.repository import Gtk


@Gtk.Template(resource_path='/com/github/merisedotdev/stag/window.ui')
class StagWindow(Adw.ApplicationWindow):
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

    def __init__(self, **kwargs):
        # GTK constructors like to do things
        super().__init__(**kwargs)
        # actions linking
