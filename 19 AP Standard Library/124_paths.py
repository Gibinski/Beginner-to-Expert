# ---------------------------------------------------------------------
# ---------------**## Patgs ##**---------------------
# https://docs.python.org/3/library/
# *-*-*-**-**-**-** Creating an absolute path on windows
from pathlib import Path

# path = Path("C:\\Program Files\\Python 3")
# print(path)

# *-*-*--*-*-**-** Using raw string to simplify the path craetion
# path = Path("user/__init__.pt")
# print(path)

# *-*--**-**--**-** Relative paths 
# path = Path()

# *---*-*-*-*-*-*-** a Path() object that represent the current folder
# path_2 = Path("Some_Path") / Path("user")
# print(path_2)

# *-*--*-*-**-*-*-** Combining Path() object together
# path_3 = Path("some_file") / "ecomerrce" / "__init__.py"
# print(path_3)

# *-*-*-*-*--**-*-** Getting the home directory of the current user
# print(Path.home())

# *-*-*-*-*--**-*-** 
path = Path("social/audio")
path2 = Path("social/image/__init__.py")
path3 = Path("user")

# *-*-*-*-*--**-*-** Calling the exists method to find out if this file or directory exists ir not
# print(path.exists())
# print(path2.exists())
# print(path3.exists())

# *-*-*-*-*--**-*-** To check to see if this path is a file
# print(path.is_file())
# print(path2.is_file())
# print(path3.is_file())

# *-*-*-*-*--**-*-** To check to see if this path is a directory
# print(path.is_dir())
# print(path2.is_dir())
# print(path3.is_dir())


# *-*-*-*-*--**-*-** extracting individual component in this path
# return the file name in the path
# print(path.name)
# print(path2.name)
# print(path3.name)



# *-*-*-*-*--**-*-** exstracting individual components in this path
# return the file name in the path without extention
# print(path.stem)
# print(path2.stem)
# print(path3.stem)

# return the file name extention
# print(path.suffix)
# print(path2.suffix)
# print(path3.suffix)

# return the perent of the file
# print(path.parent)
# print(path2.parent)
# print(path3.parent)

# *-*-*-*-*--**-*-** Creates a new path with the file name changed
path3 = path2.with_name("__initial__.txt")
print(path3)

# *-*-*-*-*--**-*-** Getting the absolute path for the newly created file
print(path3.absolute())

# *-*-*-*-*--**-*-** Changing the extension of a file
print(path3.with_suffix(".js"))

