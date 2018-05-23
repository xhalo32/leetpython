#!/usr/bin/python

from csv import reader
import matplotlib
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
fig.subplots_adjust(left=0.07, bottom=0.07, right=0.93, top=0.98)

v2 = savitzky_golay(np.diff(p)*100.,7,1)
p2 = np.cumsum(v2)/100.
po2 = np.cumsum(v)/100.

pp = p.max() - p
v = -v

from scipy import stats
slope,intercept,r_value,p_value,std_err=stats.linregress(
    t[127:187], v[127:187])

regline = t[127:187]*slope+intercept

#label_text = [r"%.2f$s$"%float(loc) for loc in plt.xticks()[0]]
#axes.set_xticklabels(label_text)

# pos
axup=plt.subplot(211)
mins = [t[125], t[191]]
for m in mins:
    plt.axvline(x=m,c='gray',label=r'${}s$'.format(m))
axup.fill_between(t, -1, 2, where=(mins[0]<=t)^(mins[1]<t), facecolor='gray', alpha=0.2)
axup.annotate('',
    xy=(mins[0],0),
    xytext=(mins[1],0),
    arrowprops=dict(
        arrowstyle='<->',
        lw=2,
        ec='gray',
    )
)
plt.text((mins[0]+mins[1])/2,0,r'$%.2fs$'%(mins[1]-mins[0]),horizontalalignment='center',verticalalignment='bottom',fontsize=10,color='gray')

plt.scatter(t, p, 3, 'r', label=r'$f(t)$')
plt.scatter(t, pp, 3, 'm', label=r'$g(t)={}m-f(t)$'.format(p.max()))
peak = 160
axup.annotate(r'${}m$'.format(pp[peak]),
    xy=(t[peak],pp[peak]), xycoords='data',
    xytext=(t[peak]-0.2, pp[peak]+0.1), textcoords='data',
    bbox=dict(boxstyle="round", fc="w", ec='m'),
    arrowprops=dict(
        arrowstyle='->',
        lw=2,
        ec='m',
    )
)
# axup.get_xaxis().set_major_formatter(
#     matplotlib.ticker.FuncFormatter(lambda x, p: r'$%ds$'%(p)))
# axup.get_yaxis().set_major_formatter(
#     matplotlib.ticker.FuncFormatter(lambda x, p: r'$%dm$'%(p)))
plt.xlabel(r'$time\ (s)$')
plt.ylabel(r'$height\ (m)$')
plt.grid(True)
plt.axis([-0.1,5.3,-0.1,1.1])
plt.legend()

# vel
axdn=plt.subplot(212)
plt.scatter(t, v, 3, 'g', label=r'$\frac{d}{dt}g(t)$')
# acc
plt.plot(t[127:187], regline, 'b', label=
        r'$h=%.2fms^{-1}+(%.2fms^{-2})t$'%(intercept,slope))
plt.text(t[170], v[170], r'$%.2fms^{-2}$'%(slope),horizontalalignment='right',
    verticalalignment='top',fontsize=10,color='darkblue')
# axdn.get_xaxis().set_major_formatter(
#     matplotlib.ticker.FuncFormatter(lambda x, p: r'$%ds$'%(p)))
# axdn.get_yaxis().set_major_formatter(
#     matplotlib.ticker.FuncFormatter(lambda x, p: r'$%dms^{-1}$'%(p)))
plt.xlabel(r'$time\ (s)$')
plt.ylabel(r'$speed\ (ms^{-1})$')
plt.grid(True)
plt.axis([-0.1,5.3,-4,4])
plt.legend()

# plt.scatter(t, a, 4, 'b', label='{} {}'.format(
#    l[0,3+4*run], l[1,3+4*run]))
# plt.scatter(t, ahat, 4, 'm', label='{} {}'.format(
#    l[0,3+4*run], l[1,3+4*run]))
# plt.scatter(t[1:], v2, 4, 'orange')
# plt.scatter(t[1:], p2, 4, 'yellow')

# from scipy.interpolate import interp1d
# N=400
# interf = interp1d(t[:N:5], pp[:N:5], kind='cubic')
# plt.scatter(t, po2, 4, 'cyan')
# tnew = np.arange(t.min(),t[N-5],0.0001)
# plt.plot(tnew, interf(tnew), 'b')

# import sys
# sys.path.append('matplotlib-tools/')
# from matplotlib_tools.tools import Ruler
# markerprops = dict(marker='o', markersize=5, markeredgecolor='red')
# lineprops = dict(color='red', linewidth=2)
# ruler = Ruler(ax=axes,
#     useblit=True, markerprops=markerprops, lineprops=lineprops)

plt.show()
