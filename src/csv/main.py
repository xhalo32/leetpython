#!/usr/bin/python

from csv import reader
import matplotlib.pyplot as plt
import numpy as np
from savitzky_golay import *

filename = 'pallon pomppiminen.csv'
with open(filename,'r') as f:
    r = reader(f, delimiter=',')
    l = np.array(list(r))

def processcsv(l):
    "Replace all empty cells with 0 for float conversion"
    for x in range(l.size):
        a = l.item(x)
        l.itemset(x, ((a=='') and '0') or a)
    return l

l = processcsv(l)

# 0 = Run #1
# bounces = 2 = Run #3
run = 2
t = l[2:,0+4*run].astype(np.float)
p = l[2:,1+4*run].astype(np.float)
v = l[2:,2+4*run].astype(np.float)
a = l[2:,3+4*run].astype(np.float)
#                   list, window size, order
ahat = savitzky_golay(a, 11, 1)

fig, axes = plt.subplots(nrows=1, ncols=1)
fig.subplots_adjust(left=0.05, bottom=0.05, right=0.98, top=0.98)
label_text = [r"%.2f$s$"%float(loc) for loc in plt.xticks()[0]]
axes.set_xticklabels(label_text)

plt.scatter(t, p, 4, 'r', label='{} {}'.format(
    l[0,1+4*run], l[1,1+4*run]))
plt.scatter(t, v, 4, 'g', label='{} {}'.format(
    l[0,2+4*run], l[1,2+4*run]))
# plt.scatter(t, a, 4, 'b', label='{} {}'.format(
#     l[0,3+4*run], l[1,3+4*run]))
plt.scatter(t, ahat, 4, 'darkblue', label='{} {}'.format(
    l[0,3+4*run], l[1,3+4*run]))

plt.legend()
plt.grid()
plt.show()
