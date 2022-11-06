import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\vkale\AppData\Local\Programs\Python\Python310\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\vkale\AppData\Local\Programs\Python\Python310\tcl\tk8.6"

executables = [cx_Freeze.Executable("fdafr.py", base=base, icon="face.ico")]


cx_Freeze.setup(
    name = "fdafr",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["face.ico",'tcl86t.dll','tk86t.dll', 'photo','data','database','attendance_report']}},
    version = "3.0",
    description = "fdafr | Developed By Vaibhav",
    executables = executables
    )
