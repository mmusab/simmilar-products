from PIL import Image
import sys
import os

def processImage(infile):
    try:
        im = Image.open(infile)
    except IOError:
        print ("Cant load", infile)
        sys.exit(1)
    i = 0
    mypalette = im.getpalette()

    try:
        while 1:
            im.putpalette(mypalette)
            new_im = Image.new("RGB", im.size)
            new_im.paste(im)
            new_im.save(infile.split('.g')[0]+'.jpg')

            i += 1
            im.seek(im.tell() + 1)

    except EOFError:
        pass # end of sequence

path = "./data/test/"
imgs = os.listdir( path )
print (imgs)
for im in imgs:
    if(im.split('.')[1]=='gif'):
        processImage(path+im)
os.system('rm ./data/test/*.gif')
