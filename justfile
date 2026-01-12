# some extra commands to handle the project.

mktext: # define a pot file from source
    xgettext --files-from=po/POTFILES.in --output=po/stag.pot
