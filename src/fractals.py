#!/usr/bin/python2.7

from PIL import Image
from PIL import ImageDraw
from math import cos,sin,pi
import os

def koch(d,order,pos,size,angle=0,s=120,linewidth=1,color=(0,0,0)):
	if order==0:
		newpos=[pos[0]+size*cos(pi/180.0*angle),pos[1]+size*sin(pi/180.0*angle)]
		d.line([pos[0],pos[1],newpos[0],newpos[1]],fill=color,width=linewidth)
		return newpos
	else:
		alist=[0,-180+s,360-2*s,-180+s]
		for a in alist:
			angle+=a
			pos=koch(d,order-1,pos,size/(2+2*cos(pi/180.0*-alist[1])),angle,s,linewidth,color)
		return pos
 
def tree(d,order,theta,size,posn,heading=-pi/2,trunk_ratio=0.3,sizefactor=0.9,balance=0,linewidth=1,color=(0,0,0)):
	trunk=size*trunk_ratio
	delta_x=trunk*cos(heading);delta_y=trunk*sin(heading)
	newpos=(posn[0]+delta_x,posn[1]+delta_y)
	d.line([posn[0],posn[1],newpos[0],newpos[1]],fill=color,width=linewidth)
	if order > 0:
		newsize=size*(sizefactor-trunk_ratio)
		for i in [-1,1]:
			tree(d,order-1,theta,newsize,newpos,heading+(i+balance)*theta,trunk_ratio,sizefactor,balance,
					linewidth,color)

if __name__=='__main__':
	#SIZE=[1920,1080]
	SIZE=[3840,2160]
	WIDTH,HEIGHT=SIZE

	img=Image.new('RGB',SIZE,"white")
	d=ImageDraw.Draw(img)

	tree(d,9,0.5,HEIGHT*0.5,(WIDTH//2,HEIGHT-50),-pi/2)

	koch(d,7,[0,HEIGHT-HEIGHT/8.0],WIDTH)

	img.save("frac.png")
	os.system("xdotool search --name frac.png key r")
