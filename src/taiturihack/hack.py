#!/usr/bin/python

## import bash commandline interpreter
import subprocess

## take screenshot
p=subprocess.Popen(["scrot", "shot.png"], stdout=subprocess.PIPE)
p.communicate()

## import python image processing libraries
from PIL import Image
from PIL import ImageFilter

shot=Image.open("shot.png")
pixels=shot.load()

size=(600,270),(960,400)
newshot=Image.new("RGB", (size[1][0]-size[0][0],size[1][1]-size[0][1]), "white")
newpixels=newshot.load()

debug=False
for i in range(size[1][0]-size[0][0]):
    for j in range(size[1][1]-size[0][1]):
        if debug: 
            newpixels[i,j]=pixels[size[0][0]+i,size[0][1]+j]
        else: 
            if (pixels[size[0][0]+i,size[0][1]+j]==(255,255,255)):
                newpixels[i,j]=(0,0,0)

##newshot=newshot.filter(ImageFilter.MinFilter(3))
##newshot=newshot.filter(ImageFilter.BLUR)
##newshot=newshot.filter(ImageFilter.GaussianBlur(radius=2))
##newshot=newshot.filter(ImageFilter.UnsharpMask(radius=10, percent=250, threshold=10))

##Horiz = ImageFilter.Kernel((3, 3), (-1,-2,-1,0,0,0,1,2,1), scale=None, offset=0)
##newshot=newshot.filter(Horiz)

##newshot=newshot.filter(ImageFilter.MaxFilter(size=3))
##newshot=newshot.filter(ImageFilter.CONTOUR)

newshot=newshot.filter(ImageFilter.ModeFilter(size=3)) ## very good



newshot.save("newshot.png")

## call for gocr
p=subprocess.Popen(["gocr", "newshot.png"], stdout=subprocess.PIPE)
text=p.communicate()[0]
print(text)

found=""
for i in range(len(text)-2):
    if text[i]=="l" and text[i+2]=="l":
        print(text[i+1])
        found=text[i+1]
