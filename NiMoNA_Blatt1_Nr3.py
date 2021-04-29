# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 21:33:07 2021

@author: Christoph test
"""

import numpy as np
import matplotlib.pyplot as plt
#Hier werden die Analytischen Lösungen für a-c) bzw. d) ermittelt
x_ana = np.arange(0,7,0.005)
ya_ana = 0.5*np.e**(-x_ana)
yd_ana = 3*np.e**(-3*x_ana)
plt.plot(x_ana, ya_ana, color="black", label="Analytisch a-c)")
plt.plot(x_ana, yd_ana, color="blue", label="Analytisch d)")


#Hier werden die numerischen Lösungen für a-d) bestimmt
xa = np.arange(0,7.2, 0.5)
xb = np.arange(0,7.05, 0.1)
xc = np.arange(0,7.001, 0.01)

ya = np.zeros(xa.size)
yb = np.zeros(xb.size)
yc = np.zeros(xc.size)
yd = np.zeros(xa.size)

ya[0] = 0.5
yb[0] = 0.5
yc[0] = 0.5
yd[0] = 3

for i in range(1, ya.size):
    ya[i] = ya[i-1] - 0.5*ya[i-1]
    
for i in range(1, yb.size):
    yb[i] = yb[i-1] - 0.1*yb[i-1]

for i in range(1, yc.size):
    yc[i] = yc[i-1] - 0.01*yc[i-1]

for i in range(1, ya.size):
    yd[i] = yd[i-1] - 0.5*3*yd[i-1] 
    
    
plt.plot(xa, ya, color="red", label="Numerisch a)")
plt.plot(xb, yb, color="orange", label="Numerisch b)")
plt.plot(xc, yc, color="pink", label="Numerisch c)")
plt.plot(xa, yd, color="brown", label="Numerisch d)")    




plt.legend()
plt.xlabel("x Achse")
plt.ylabel("y Achse")
plt.show

