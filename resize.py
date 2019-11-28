
import os
from PIL import Image

def imgResize(path):

	items = os.listdir(path)

	for img in items:
		if os.path.isfile(path+img):

			readimg	= Image.open(path+img)

			filename, ext = os.path.splitext(path+img)
			resize = readimg.resize((350,200), Image.ANTIALIAS)

			resize.save(filename+"_resize.jpg", "JPEG", quality=100)

	print("\n All images have been resized successfuly")


if __name__ == '__main__':
	path = "/root/Documents/instagram/"
	imgResize(path)