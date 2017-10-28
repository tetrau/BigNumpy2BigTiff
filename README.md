# BigNumpy2BigTiff

You can calculate a huge array which can't fit in the RAM with `numpy.memmap`, but you can't just render the array to a image file for some post-processing or sharing with others or checking with some image viewer. Normally, `skimage.io.imsave` will just rasie `MemoryError` for huge numpy array. `numpy2tiff` can render array of any sizes to baseline BigTIFF image as long as there is enough space on HDD.

## install
Just copy `numpy2tiff.py` to the directory of your python script. It need no dependencies except `numpy`.

## usage
```python
from numpy2tiff import numpy2tiff
# image must be 24 bit RGB format.
# In other word, image.shape == (image_length, image_width, 3)
# image.dtype == numpy.uint8
numpy2tiff(image, 'output.tif') # image: image array, path: output image filepath
```
