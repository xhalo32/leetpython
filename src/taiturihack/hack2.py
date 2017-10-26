#!/usr/bin/python
#   -*- coding:utf-8 -*-
'''
This hack scans the screen for sentences and types out those senteces
'''
from PIL import Image,ImageFilter
import subprocess,time
from os import system

def getcharacter(image,c):
    pixels=image.load()
    reply=[]
    for a in range(len(c)):
        w=c[a][1][0]-c[a][0][0]
        h=c[a][1][1]-c[a][0][1]
        newimage=Image.new("RGB", (w,h), "white")
        newp=newimage.load()
        for i in range(w):
            for j in range(h):
                #if pixels[c[a][0][0]+i,c[a][0][1]+j]==(255,255,255):
                pix=pixels[c[a][0][0]+i,c[a][0][1]+j]
                if pix[0]>200 and pix[1]>200 and pix[2]>200:
                    newp[i,j]=(0,0,0)

        newimage.save("chars/char%d.png"%a)
        p=subprocess.Popen(["gocr","chars/char%d.png"%a,"-a 95"],stdout=subprocess.PIPE)
        reply.append(p.communicate())
    return reply



# list of boxes to search for letters
# [636,296],
# [657,327],

'''
w=657-636
h=327-296
d=46
coords=[
    [636,296],
    [682,296],
    [728,296],
]
coords=[ [636+i*d,296] for i in range(10)]
c=[ [[i[0],i[1]],[i[0]+w,i[1]+h]] for i in coords ]
'''
## area for scanning characters
lause=[
    [379,283],
    [1184,419],
]
valitesti=[
    [383,184],
    [926,533],
]
kappaleharjoitus=[
    [389,213],
    [1151,405],
]
selection=kappaleharjoitus
valid="abcdefghijklmnopqrstuvwxyzåäö0123456789,.- "

msdelay=200;

print("Focus on window!")

lastsentence=[]
while 1:
    p=subprocess.Popen(["scrot", "shot.png"], stdout=subprocess.PIPE)
    p.communicate()

    shot=Image.open("shot.png")

    output=getcharacter(shot,[selection])[0][0].decode("utf-8")

    print(output)
    output=output.replace("J\n","{{newline}}")
    output=output.replace("\n"," ")
    output=output.replace("{{newline}}","\n")
    output=output.replace("'_","ä")
    output=output.replace("_'","ä")
    output=output.replace("_","")
    output=output.replace("' ","")
    output=output.replace("'","")
    sentlist=list(filter(None,output.split("\n")))
    for i in range(len(sentlist)):
        sentlist[i]=list(filter(None,sentlist[i].split(" ")))

    print(sentlist)
    time.sleep(1)
    if len(sentlist)==0:
        sentlist.append([[valid]])

    ## if no progress has been made smash keys
    if lastsentence==sentlist[-1]:
        print("STUCK!")
        p=subprocess.Popen(
            ["xdotool","type","--delay","%d"%msdelay,"%s"%valid],stdout=subprocess.PIPE).communicate()

    else:
        for sentence in sentlist:
            for o in range(len(sentence)):
                out=sentence[o]
                print(out)
                # p=subprocess.Popen(["xdotool","type","--delay","%d"%msdelay,"%s"%out])
                #os.system("xdotool type --delay %d '%s'"%(msdelay,out))
                subprocess.Popen("xdotool type --delay %d '%s'"%(msdelay,out),shell=1).communicate()

                ## type space after each word if there's a next word in sentence
                if o != len(sentence)-1:
                    p=subprocess.Popen(["xdotool","key","--delay","%d"%msdelay,"space"])
                    p.communicate()

            print("ENTER")
            p=subprocess.Popen(["xdotool","key","--delay","%d"%msdelay,"KP_Enter"])
            p.communicate()

    lastsentence=sentlist[-1]
