import numpy as np
from scipy.optimize import curve_fit
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

import sys
if len(sys.argv) == 4:
    fn=(sys.argv[1])
    fn1=(sys.argv[2])
    fn2=(sys.argv[3])

data=np.loadtxt(fn,unpack=True)

xx=data[0]
yy=data[1]
dx=np.array(0)
dy=data[4]
dx1=data[2]
dx2=data[3]
plt.errorbar(xx,yy,xerr=[dx2,dx1],yerr=dy,color='b', marker='o', markerfacecolor='red', ls='None', elinewidth=1.4, capsize=4.0, label='volatile atoms at $z<4.5$')

#dyy=np.array(0)

#- perform the fit on data
#fitdata(xx,yy,dx=dxx,dy=dyy)


data1=np.loadtxt(fn1,unpack=True)
xx1=data1[0]
yy1=data1[1]
dy1=data1[2]
lolims = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], dtype=bool)
#dx2=data[3]
#ax.errorbar(xx1,yy1,yerr=dy1,color='b',marker='o',ls='None',label='data1')
plt.errorbar(xx1,yy1, yerr=dy1, lolims=lolims, color='g', marker='v', markerfacecolor='blue',ls='None', elinewidth=1.4, capsize=4.0, markersize=4,label='volatile atoms at $z>4.5$')


data2=np.loadtxt(fn2,unpack=True)
xx2=data2[0]
yy2=data2[1]
dx3=data2[2]
dx4=data2[3]
dy3=data2[4]
lolims = np.array([1], dtype=bool)
plt.errorbar(xx2,yy2, yerr=dy3, xerr=[dx4,dx3], lolims=lolims, fmt='rp', elinewidth=1.4, capsize=4.0, markersize=9, label='N$_{HI}$-weighted mean metallicity for median z=4.844')
#plt.legend(loc=3, fontsize=10)

x = np.arange(10)
y = -0.177*x - 0.674

# fit with np.polyfit
m, b = np.polyfit(x, y, 1)

plt.plot(x, y)
plt.plot(x, m*x + b, 'b--', label='linear fit to $z<4.5$ systems')

#plt.abline(slope=-0.177, intercept=-0.674)
plt.legend(loc=3, fontsize=10)
plt.xlabel('Redshift', fontsize=14)
plt.ylabel('log (Z/Z${_\odot}$)', fontsize=14)
plt.title('Metallicity evolution', fontsize=16)
plt.xlim(-0.25, 6.5)
plt.ylim(-4.0, 0.5)

plt.savefig('metallicity_evolution_1.eps', format='eps', dpi=1000)
plt.show()


