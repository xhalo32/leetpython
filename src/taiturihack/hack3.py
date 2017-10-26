#!/usr/bin/python
#   -*- coding:utf-8 -*-
'''
This program hacks the game
'''
box=[
    [390,230],
    [1208,411],
]
certainty=00
msdelay=100
treshold=250
valid="abcdefghijklmnopqrstuvwxyzåäö0123456789 "

from PIL import Image,ImageFilter
import subprocess,time
import PIL.ImageOps

def gettext(image,box):
    p=image.load()
    
    w=box[1][0]-box[0][0]
    h=box[1][1]-box[0][1]
    nimage=Image.new("RGB",(w,h),"black")
    np=nimage.load()

    ## highpass
    for i in range(w):
        for j in range(h):
            pix=p[box[0][0]+i,box[0][1]+j]
            if pix[0]>=treshold and pix[1]>=treshold and pix[2]>=treshold:
                np[i,j]=pix

    nimage=PIL.ImageOps.invert(nimage)
    nimage.save("chars/hack3.png")
    p=subprocess.Popen(["gocr","-a","%d"%certainty,"chars/hack3.png"],stdout=subprocess.PIPE)
    return p.communicate()[0].decode("utf-8")

print("Get ready!")
time.sleep(1)

lastout=""
while 1:
    p=subprocess.Popen(["scrot","shot.png"]).communicate()
    shot=Image.open("shot.png")

    output=gettext(shot,box)
    output=output.replace("\n","")
    output=output.replace(" ","")

    _out=""
    for s in output:
        if valid.find(s)!=-1:
            _out+=s
    out=_out
    print(out)

    ## if no change has happened smash all the keys
    if out==lastout:
        p=subprocess.Popen(
            ["xdotool","type","--delay","%d"%msdelay,"%s"%valid],stdout=subprocess.PIPE).communicate()

    ## brute force
    else:
        p=subprocess.Popen(
            ["xdotool","type","--delay","%d"%msdelay,"%s"%out],stdout=subprocess.PIPE).communicate()
    
        p=subprocess.Popen(
            ["xdotool","key","--delay","%d"%msdelay,"space"],stdout=subprocess.PIPE).communicate()
    lastout=out
