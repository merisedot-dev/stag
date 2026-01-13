# some extra commands to handle the project.

mktext: # define a pot file from source
    xgettext --files-from=po/POTFILES.in --output=po/stag.pot

mkmsg: # define a po file from pot
    msginit -i po/stag.pot -o po/$1 -l $1.UTF-8
