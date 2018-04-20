#!/usr/bin/python

from csv import reader
import matplotlib.pyplot as plt
import numpy as np
from savitzky_golay import *
from scipy.signal import butter, lfilter, freqz

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

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a
def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y
# Filter requirements.
order = 3
fs = 100.0       # sample rate, Hz
cutoff = 40.      # desired cutoff frequency of the filter, Hz
# Get the filter coefficients so we can check its frequency response.

ahat2 = butter_lowpass_filter(a, cutoff, fs, order)

fig, axes = plt.subplots(nrows=1, ncols=1)
fig.subplots_adjust(left=0.05, bottom=0.05, right=0.98, top=0.98)
#label_text = [r"%.2f$s$"%float(loc) for loc in plt.xticks()[0]]
#axes.set_xticklabels(label_text)

plt.scatter(t, p, 4, 'r', label='{} {}'.format(
    l[0,1+4*run], l[1,1+4*run]))
plt.scatter(t, v, 4, 'g', label='{} {}'.format(
    l[0,2+4*run], l[1,2+4*run]))
plt.scatter(t, a, 4, 'b', label='{} {}'.format(
    l[0,3+4*run], l[1,3+4*run]))
plt.scatter(t, ahat, 4, 'm', label='{} {}'.format(
    l[0,3+4*run], l[1,3+4*run]))

import sys
sys.path.append('matplotlib-tools/')
from matplotlib_tools.tools import Ruler
markerprops = dict(marker='o', markersize=5, markeredgecolor='red')
lineprops = dict(color='red', linewidth=2)
ruler = Ruler(ax=axes,
    useblit=True, markerprops=markerprops, lineprops=lineprops)

plt.legend()
plt.grid()
plt.show()
