#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 08:38:13 2018
@author: memoherrera
"""
import matplotlib.pyplot as plt

def xnew(xprev):
    return (2 * xprev ** 2 + 3)/5

x0 = 0
x1 = 0
x0Array = []
x1Array = []
iteraciones = 0

for i in range(5):
    x1 = xnew(x0)
    x0Array.append(x0)
    x1Array.append(x1)
    if (abs( x1 - x0 ) < 0.000001 ) :
        break
    else :
        x0 = x1
        iteraciones +=1 

print("La raiz es %.5f" %x1)
print("Numero de iteraciones %d" %iteraciones )

plt.plot(x0Array,x1Array)
plt.grid()
