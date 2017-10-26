#!/usr/bin/python
from PIL import Image, ImageDraw
import math, colorsys

dimensions = (800, 800)
scale = 1.0/(dimensions[0]/3)
center = (2.2, 1.5)       # Use this for Mandelbrot set
#center = (1.5, 1.5)       # Use this for Julia set
iterate_max = 10
colors_max = 50

img = Image.new("RGB", dimensions)
d = ImageDraw.Draw(img)

# Calculate a tolerable palette
palette = [0] * colors_max
for i in range(colors_max):
    f = 1-abs((float(i)/colors_max-1)**15)
    r, g, b = colorsys.hsv_to_rgb(.66+f/3, 1-f/2, f)
    palette[i] = (int(r*255), int(g*255), int(b*255))

# Calculate the mandelbrot sequence for the point c with start value z
def iterate_mandelbrot(c, z = 0):
    for n in range(iterate_max + 1):
        z = z*z +c
        if abs(z) > 2:
            return n
    return None

# Draw our image
for y in range(dimensions[1]):
    for x in range(dimensions[0]):
        c = complex(x * scale - center[0], y * scale - center[1])

        #n = iterate_mandelbrot(c)            # Use this for Mandelbrot set
        n = iterate_mandelbrot(complex(0.3, 0.6), c)  # Use this for Julia set

        if n is None:
            v = 1
        else:
            v = n/100.0

        d.point((x, y), fill = palette[int(v * (colors_max-1))])

img.save("result.png")
