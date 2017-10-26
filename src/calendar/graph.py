#!/usr/bin/python2.7

import numpy as np
import matplotlib.pyplot as plt

plt.ion()

x = np.arange(0, 5, 0.01);
y = np.tan(x)
plt.plot(x, y)

while 1:
    exec(raw_input())
