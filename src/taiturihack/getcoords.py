#!/usr/bin/python
import subprocess

lastmouse=False
mouse=False
c=int(input("How many coordinates: "))

for i in range(2*c):
    while 1:
        p=subprocess.Popen(["./getclick.sh"],stdout=subprocess.PIPE)
        mouse=bool(int(str(p.communicate()[0]).split("'")[1][0]))
    
        if lastmouse!=mouse:
            if mouse:
                p=subprocess.Popen(["xdotool", "getmouselocation"],stdout=subprocess.PIPE)
                coords=str(p.communicate()[0]).split("'")[1].split("'")[0].split("screen")[0]
                x=int(coords.split(" ")[0].split(":")[1])
                y=int(coords.split(" ")[1].split(":")[1])
                print("[%d,%d],"%(x,y))
            lastmouse=mouse
            break
