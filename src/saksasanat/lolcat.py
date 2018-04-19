# coding: utf-8
import math
from time import sleep

def rgb2ansi(r,g,b):
    return 16+36*round(-0.5+6.*r/256.)+6*round(-0.5+6.*g/256.)+round(-0.5+6.*b/256.)

def hsv2rgb(h, s, v):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b

def printcolor(text,inc=10,phase=0,invert=False):
    s=""
    for d in range(len(text)):
        a = rgb2ansi(*hsv2rgb(inc*d+phase,1.,1.))
        s+= "\u001b[7m"*invert+"\u001b[38;5;%dm%s"%(a,text[d])
    print(s)

for i in range(360*10):
    printcolor("MOIMOIMOI AAPO!!!!",10,i)
    sleep(0.01)
