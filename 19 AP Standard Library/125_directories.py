# ---------------------------------------------------------------------
# ---------------**## Directories ##**---------------------
from pathlib import Path
my_directory = Path("real_estate")
new_directory = Path("social")


# *-*-*-**-**-**-** Useful Directory Methods

# 1 - exists() ->>>> Checking wether or not the directory
# print(my_directory.exists())

# 2 - mkdir() ->>>> Creating the directory
# my_directory.mkdir()

# 3 - rmdir() ->>>> removing the directory
# my_directory.rmdir()

# 4 - rename() ->>>> renaming the directory
# my_directory.rename("property_dealer")

# 5 - iterdir() ->>>> getting list of files and directories at.
# print(new_directory.iterdir())

# for data in new_directory.iterdir():
#     print(data)

# LC
# social_data = [data for data in new_directory.iterdir()]
# print(social_data)

# 6 - is_file() ->>>> Getting only the files
# paths = [data for data in new_directory.iterdir() if data.is_file()]
# print(paths)

# 7 - is_dir() ->>>> Getting only the directorys
# paths = [data for data in new_directory.iterdir() if data.is_dir()]
# print(paths)

# Case 1: Searching using a patterns using asterix symvol (*)
# paths = [data for data in new_directory.iterdir() if data.is_dir()]
# python_files = [data for data in new_directory.glob("*.py")]
# print(python_files)
# print(paths)

# Case 2: Searching recusively using a rglob() method
python_files = [data for data in new_directory.glob("*.*")]
print(python_files)




