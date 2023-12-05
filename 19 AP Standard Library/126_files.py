# ---------------------------------------------------------------------
# ---------------**## Files ##**---------------------
from pathlib import Path
from time import ctime

import shutil

source = Path("property_dealer/property.py")
new_source = Path("property_dealer/app.py")
my_directpry = Path("property_dealer/__init__.py")

# ----------------------- Useful files methods

# 1- exists() ->>>> Checking wether or not the file exists 
# print(source.exists())

# 2- rename() ->>> renaming the file
# source.rename("property_dealer/app.py")

# 3- unlink() ->>> removing the file
# new_source.unlink()

# 4- stat() ->>>>> returns info about the file
# print(my_directpry.stat())
# print(my_directpry.stat().st_atime)
# print(my_directpry.stat().st_mtime)
# print(my_directpry.stat().st_ctime)

# The following 4 methods take care of opening and closing the file *-*--*-**-*

# 5- read_bytes() ->>>> reading data from a file ->>>> return content of the fole as a bytes object for reprecenting binary data
# print(my_directpry.read_bytes())


# 6- read_text() ->>>> reading the content of the file as a string
# print(my_directpry.read_text())

# 7- write_bytes() ->>> writing to a file
# print(my_directpry.write_bytes(b'print("Hello from Jupiter")'))
# print(my_directpry.read_text())

# 8- write_text() ->>> writing to a file as a string
# print(my_directpry.write_text('print("Hello from Venus")'))
# print(my_directpry.read_text())

# 9- Copying a to another location
target_directory = Path("astronomy")
shutil.copy(my_directpry, target_directory)


