#!/usr/bin/python2.7

from PIL import Image
from PIL import ImageDraw
from math import cos,sin,tan,pi
import os, colorsys, random

def gs(val):
	return val,val,val

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

def kochsnowflake(d,order,center,size,s=120,linewidth=1,color=(0,0,0)):
	pos=[center[0]-(size/2.0),center[1]-(size/2.0)*tan(pi/180.0*60)]
	for i in range(6):
		pos=koch(d,order,pos,size,i*60,s,linewidth,color)

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

def dragon(d,order,pos,size,polarity=1,angle=45,s=120,linewidth=1,color=(0,0,0),gene=[(0,0),(0,0)]):
	if order==0:
		newpos=[pos[0]+size*cos(pi/180.0*angle),pos[1]+size*sin(pi/180.0*angle)]
		d.line([pos[0],pos[1],newpos[0],newpos[1]],fill=127+127*polarity,width=linewidth)
		return newpos
	else:
		angle+=45*polarity*gene[0][0]
		pos=dragon(d,order-1,pos,size/2**0.5,polarity*gene[1][0],angle,s,linewidth,color,gene)
		angle+=45*polarity*gene[0][1]
		pos=dragon(d,order-1,pos,size/2**0.5,polarity*gene[1][1],angle,s,linewidth,color,gene)
		return pos

def dragon2(d,order,pos,size,angle,direction=45,n=0):
	if order<=0:
		c=tuple([int(255*i) for i in colorsys.hsv_to_rgb(((pos[0]-WIDTH/2.0)**2.0+(pos[1]-HEIGHT/2.0)**2.0)**0.5/1024.0,1,1)])
		newpos=[pos[0]+size*cos(pi/180.0*angle),pos[1]+size*sin(pi/180.0*angle)]
		d.line([pos[0],pos[1],newpos[0],newpos[1]],fill=c,width=2)
		return newpos, n+1
	else:
		angle+=direction
		pos,n=dragon2(d,order-1,pos,size/2**.5,angle,45,n)
		angle-=2*direction
		pos,n=dragon2(d,order-1,pos,size/2**.5,angle,-45,n)
		angle+=direction
		return pos, n

def rangeindex(i,l):
	for r in range(len(l)-1):
		if l[r]<=i<=l[r+1]:	return r
	return -1

def barnsley(d,iterations,w,h,ranges,genes,r=0,color=gs(0)):
	x,y=0,0
	for i in range(iterations):
		rand=random.uniform(0,100)
		i=rangeindex(rand,ranges)
		x,y=[genes[i][j][0]*float(x)+genes[i][j][1]*float(y)+genes[i][j][2] for j in range(2)]
		vx,vy=(w/2.0+x*w/10.5,h-y*h/10.5)
		d.ellipse((vx-r,vy-r,vx+r,vy+r),fill=color)
		#d.point((w/2+x*w/10.0,h-y*h/10.0),fill="black")


if __name__=='__main__':
	#SIZE=[1920,1080]
	SIZE=[3840,2160]
	WIDTH,HEIGHT=SIZE

	img=Image.new('RGB',SIZE,"white")
	d=ImageDraw.Draw(img)

	#tree(d,9,0.5,HEIGHT*0.5,(WIDTH//2,HEIGHT-50),-pi/2)

	#koch(d,7,[0,HEIGHT-HEIGHT/8.0],WIDTH)
	#gene=(1,-2),(1,-1) semi dragon
	#depth=2
	#gene=(0,-2),(-1,1)
	#dragon(d,depth,[WIDTH/2.0-0*HEIGHT/4.0,HEIGHT/2.0],HEIGHT/3.0,1,-90,linewidth=2,gene=gene)
	#dragon2(d,18,[WIDTH/2.0,HEIGHT/2.0],HEIGHT/3.0,90)
	'''ranges=[0,1,86,93,100] classic fern
	genes=[	
			[(0,0,0),(0,0.16,0)],
			[(0.85,0.04,0),(-0.04,0.85,1.6)],
			[(0.2,-0.26,0),(0.23,0.22,1.6)],
			[(-0.15,0.28,0),(0.26,0.24,0.44)],
	]
	'''
	r=random.random
	s=lambda: 0
	s=lambda: random.getrandbits(1)
	s1=s()		# 1 0
	s1c=-s1+1	# 0 1
	s1b=2*s1-1	# 1 -1
	s1cb=2*s1c-1# -1 1
	r1=r()*0.5+0.5
	ranges=[0,1,86,93,100]
	genes=[	
			[(0,0,0),						(0,0.16,0)],
			[(0.8+0.1*r(),s1b*0.05*r1,0),	(-(0.03+0.04*r())*s1b,0.82,1.6)],
			[(0.1+0.1*r(),-0.17-.06*r(),0),	(s1b*(0.2+.06*r()+s1c*0.2),0.18*s1+.08*r(),1+1*r())],
			[(-0.1+0.1*r(),+0.17+.06*r(),0),(s1b*(0.2+.06*r()+s1c*0.2),0.18*s1+.08*r(),1+1*r())],
	]
	print(genes)
	'''
	genes=[	
			[(0,0,0),(0,0.16,0)],
			[(0.85,-0.04,0),(0.04,0.85,1.6)],
			[(0.2,-0.26,0),(-0.63,0.05,1.6)],
			[(-0.15,0.28,0),(-0.66,0.05,0.44)],
	]'''
	'''
	genes=[
		[(0, 0, 0), (0, 0.16, 0)],
		[(0.8833068402737843, 0.04742500298752205, 0), (0.06529136783350334, 0.85, 1.6)],
		[(0.10316138818140216, -0.2574602481056263, 0), (-0.6481695471089404, 0.04000019437502212, 1.2083408128802138)],
		[(-0.15, 0.28, 0), (-0.6106014745187465, 0.015418060495432737, 1.0535796172952783)]
	]'''
	'''
	genes=[
		[(0, 0, 0), (0, 0.16, 0)],
		[(0.8283960172899405, -0.010609301587963787, 0), (0.05841956194407307, 0.85, 1.6)],
		[(0.15917342105736967, -0.20688655337704424, 0), (-0.6142165791056544, 0.0517021904725546, 2.0650989460512363)],
		[(-0.15, 0.20, 0), (-0.6202680341099683, 0.06656000730740115, 1.93375432155726)]]
	'''
	

	barnsley(d,10**5,WIDTH,HEIGHT,ranges,genes)

	img.save("frac.png")
	os.system("xdotool search --name frac.png key r")
