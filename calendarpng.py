#!/usr/bin/python2.7

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import calendar, os
from fractals import koch, tree
from random import random
from math import pi

def gs(val):
	return (val,val,val)

def drawtext(draw, pos, text, color, fontstring="/usr/share/fonts/TTF/DejaVuSans.ttf", fontsize=72, center=False):
	shift=draw.textsize(text,font=ImageFont.truetype(fontstring,int(fontsize)))
	if center:
		draw.text([pos[i]-shift[i]/2 for i in range(2)],text,fill=color,font=ImageFont.truetype(fontstring,int(fontsize)))
	else:
		draw.text(pos,text,fill=color,font=ImageFont.truetype(fontstring,int(fontsize)))

# 60cm * 106cm
SIZE=(1920,1080)
SIZE=(3840,2160) 
SIZE=(7680,4320)

WIDTH,HEIGHT=SIZE

def op(a,b):
	if a==b: return b
	else: return a % b

_monthrange=[8,5]
monthrange=[[_monthrange[0],_monthrange[1]] if _monthrange[0]<=_monthrange[1] else
			[_monthrange[0],_monthrange[1]+12*(1+_monthrange[0]//12)]][0]
print(monthrange)

monthranges=[ op(i,12) for i in range(monthrange[0],monthrange[1]+1) ]

print(monthranges)

weekdays=('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
weekdays_abrs=('Mon','Tue','Wed','Thu','Fri','Sat','Sun')
months=['January','February','March','April','May','June','July','August','September','October','November','December']

padding=(WIDTH/8.0,HEIGHT/8.0)
blockpadding=(WIDTH/120.0, HEIGHT/60.0)
numberpad=WIDTH/300.0

# remove old images
os.system("rm /home/potato/Desktop/calendar/*")
year=2017

for month in monthranges:
	if month==1: year+=1
	day,days=calendar.monthrange(year,month)

	img=Image.new('RGB', SIZE, "white")
	d=ImageDraw.Draw(img)

	# darken weekends
	d.rectangle([(5.5)*padding[0],(0)*padding[1],(8)*padding[0],(8)*padding[1]],fill=gs(240))

	# draw some gridlines
	for i in range(int(WIDTH/padding[0])):
		for j in range(int(HEIGHT/padding[1])):
			d.rectangle([i*padding[0],j*padding[1],(i+1)*padding[0],(j+1)*padding[1]],
					outline=gs(200))
	for i in range(int(WIDTH/padding[0])+1):
		for j in range(int(HEIGHT/padding[1])+1):
			d.rectangle([(i-0.5)*padding[0],(j-0.5)*padding[1],(i+1-0.5)*padding[0],
				(j+1-0.5)*padding[1]],outline=gs(100))

	# draw fractals
	if random() > 0.5:
		koch(d,7+int(3*random()),[0,HEIGHT-HEIGHT/8.0],WIDTH,s=int(random()*30)+110,color=gs(180))
	else:
		tree(d,10,0.5+0.3*random(),1.6*HEIGHT,[WIDTH//2,HEIGHT-padding[1]],trunk_ratio=0.1+0.1*random(),sizefactor=0.775+0.05*random(),
			balance=-0.5+random(),color=gs(180))

	for i in range(days):
		# draw the boxes
		pos=[padding[0]+(i+day)%7*padding[0]-padding[0]/2+blockpadding[0]/2,
			2*padding[1]+int(i/7.+day/7.)*padding[1]-padding[1]/2+blockpadding[1]/2]
		d.rectangle([pos[0],pos[1],
			pos[0]+2*(padding[0]/2-blockpadding[0]/2),pos[1]+2*(padding[1]/2-blockpadding[1]/2)],
			outline=gs(50))
		# double boxes
		pos=[padding[0]+(i+day)%7*padding[0]-padding[0]/2+blockpadding[0]/2-1,
			2*padding[1]+int(i/7.+day/7.)*padding[1]-padding[1]/2+blockpadding[1]/2-1]
		d.rectangle([pos[0],pos[1],
			pos[0]+2*(padding[0]/2-blockpadding[0]/2+1),pos[1]+2*(padding[1]/2-blockpadding[1]/2+1)],
			outline=gs(50))

		# draw the day index
		drawtext(d,[p+numberpad for p in pos],str(i+1),"black",
				fontstring="NimbusRoman-Regular.ttf",fontsize=18*WIDTH/1920.0)

	for i in range(len(weekdays)):
		drawtext(d, [padding[0]+i*(WIDTH-padding[0])/len(weekdays),padding[1]],
				weekdays_abrs[i], "black", fontsize=36*WIDTH/1920.0, center=True)

	drawtext(d,[WIDTH/2,padding[1]/2],months[month-1],"black",
fontstring="/usr/share/fonts/TTF/DejaVuSans-Bold.ttf",fontsize=48*WIDTH/1920.0,center=True)

	print(months[month-1],year)
	img.save("calendar/"+str(year)+"_"+str(month).zfill(2)+".png")


os.system("xdotool search --name calendar/ key r")
