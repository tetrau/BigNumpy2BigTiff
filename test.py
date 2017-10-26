import numpy as np
import skimage.io
import os
from numpy2tiff import numpy2tiff

array = np.random.randint(0, 256, size=(1000, 1000, 3), dtype=np.uint8)
TEMP_FILE = 'temp.tiff'

numpy2tiff(array, TEMP_FILE)
image = skimage.io.imread(TEMP_FILE)

print(np.array_equal(array, image))

os.remove(TEMP_FILE)
