from PIL import Image
import os, sys
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

path = "./data/train/"
dirs = os.listdir( path )
print(len(dirs))
i=0
for item in dirs:
	i=i+1
	print(i)
	if os.path.isfile(path+item):
		print(item)
		im = Image.open(path+item)
		f, e = os.path.splitext(path+item)
		imResize = im.resize((500,500))
		imResize.save(f + '.jpg', 'JPEG', quality=90)

path = "./data/test/"
dirs = os.listdir( path )
print(len(dirs))
i=0
for item in dirs:
	i=i+1
	print(i)
	if os.path.isfile(path+item):
		print(item)
		im = Image.open(path+item)
		f, e = os.path.splitext(path+item)
		imResize = im.resize((500,500))
		imResize.save(f + '.jpg', 'JPEG', quality=90)