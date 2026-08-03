import os
from pathlib import Path

current_dir_os = os.getcwd()
print(current_dir_os)

current_dir_pathlib = Path()
print(current_dir_pathlib.absolute())

list_dir_os = os.listdir()
print(list_dir_os)