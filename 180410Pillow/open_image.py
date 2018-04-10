from PIL import Image, ImageFilter
# #include <numpy> + using numpy = np
import numpy as np
img = Image.open('original.jpg')
#GET size 
width, height = img.size
print (img.size)
#
print (img.getextrema())
# gray scale , 90 rotation, gaussian filter
img2 = img.convert('L').rotate(90).filter(ImageFilter.GaussianBlur())
#open
img.show()
img2.show()
