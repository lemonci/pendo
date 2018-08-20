


# # Import libraries

import os
import PIL
from keras.preprocessing.image import img_to_array, load_img


# # Set test folder

folder = ''


# # Walk all files

onlyfiles = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

print("Working with {0} images".format(len(onlyfiles)))
print("Image examples: ")

for i in range(0, len(onlyfiles)):
    print(onlyfiles[i])


# # Read image, convert to greyscale and convert to array


arrays = []
for i in range(0, len(onlyfiles)):
    arrays.append(img_to_array(load_img(onlyfiles[i]).convert('L')))
