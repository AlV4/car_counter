import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

includes = []

application_title = "Car Counter"
main_python_file = "car_counter.py"


setup(
    name=application_title,
    version="0.1",
    description="Sample cx_Freeze PyQt4 script",
    options={"build_exe": {"includes": includes}},
    executables=[Executable(main_python_file, base=base)])
