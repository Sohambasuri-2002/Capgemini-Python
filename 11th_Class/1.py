# FILE OPERATIONS
# File -> container which helps us to store some data or instructions (.docx, .html, jpg, .txt, .java, .py)
# By looking into extensions, users can identify what type of data present in the file.
# Path ---> is basically allocation where file is present in the system.
# \ --> backslash
# Windows accept '\' as path separator while linux or mac accepts '/'

# Backslash Escape Sequence problem :
# in python '\' is a Escape Sequence char

# var = 'c:\users\kiit\dektop'
# to get rid of '\' we   -- import os
# so we do , path = os.path.join('c:','users','kiit','desktop') which takes care of everyrhing like running in winsdows or linux
# print(os.sep) -> gives '\' in case of windows 



