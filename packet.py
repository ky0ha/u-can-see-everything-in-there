import os
from tkinter import filedialog, dialog
from tkinter import *

Tk().withdraw()
fpath = filedialog.askopenfilename(title=u'选择待打包的py文件', initialdir=(os.path.expanduser(os.path.abspath(os.path.dirname(__file__)))))
command_console = "pyinstaller -F -w -i test.ico " + fpath
print(command_console)

f = os.popen(command_console)
f.read()