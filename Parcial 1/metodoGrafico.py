#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 09:11:14 2018
@author: memoherrera
"""

##Metodo grafico de representar graficas
import numpy as np
import matplotlib.pyplot as plt

xarray = np.linspace(0,2,100)
yarray = np.zeros(100)

#print (xarray)

for i in range (len(xarray)): 
    yarray[i] = y(xarray[i])
    
#print(yarray)
    
plt.plot(xarray,yarray)
plt.grid()
plt.show()
