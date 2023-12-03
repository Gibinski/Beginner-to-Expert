# ---------------------------------------------------------------------
# ---------------**## Path and Packages##**---------------------

# # ---------*******----- The Path object
import sys
print(sys.path)


# # ---------*******----- Packages 

# # ---------*******----- Important Ways
# Amproach 1
# import social_media.user_image

# social_media.user_image.img()


# Amproach 2
# from social_media.user_image import img, media

# img()
# media()


# Amproach 2
from social_media import user_image

user_image.img()
user_image.media()

