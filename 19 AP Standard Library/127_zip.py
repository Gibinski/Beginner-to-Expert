# ---------------------------------------------------------------------
# ---------------**## Zip ##**---------------------
from pathlib import Path
from zipfile import ZipFile


# *-*-*-*-*-**-*-* Creating Zip Files ------------------------
all_z = ZipFile("zip_dir/all.zip", "w")
py_z = ZipFile("zip_dir/py.zip", "w")

# print(all_z)
# print(type(all_z))
# *-**-*-*-*-*-*-*-*- Adding files to zip files (ziping files)
# *-**-*-*-*-* Approach one ->>>> all files
for path in Path("social").rglob("*.*"):
    all_z.write(path)
all_z.close()

# *-**-*-*-*-* Approach two ->>>> py files
with ZipFile("zip_dir/py.zip", "w") as py_files:
    for path in Path("social").rglob("*.py"):
        py_files.write(path)

# **************----------------------
# showing all filws
# with ZipFile("zip_dir/all.zip") as all_files:
#     print(all_files.namelist())

# getting single file's info
# with ZipFile("zip_dir/py.zip") as file_info:
#     info = file_info.getinfo("social/social.py")
#     print(info.file_size)
#     print(info.compress_size)
#     print(info.orig_filename)
#     print(info.__module__)

# extractiong zip files
with ZipFile("zip_dir/all.zip") as all_files_z:
    all_files_z.extractall("Extracted")