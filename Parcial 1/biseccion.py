#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 08:48:16 2018
@author: memoherrera
Metodo grafico de convergencia
Biseccion
Dado un rango inicial donde haya un cambio de signo, dividir el
rango por la mitad hasta encontrar la raiz
Ejemplo con la ecuacion :
*Calcular el coeficiente de arrastre con los siguientes datos*
m = 68.1 kg
v = 40 m/s
t = 10 s
g = 9.8 m/s^2
f(c) = ((g*m)/c)*(1-e^((-m*c)/10)*-v 
"""
import math
import numpy as np
import matplotlib.pyplot as plt

def fun(c):
    return (667.38/c)*(1- math.exp(-6.81*c)) -40

#Elegir valores iniciales x0 y x1 
#Donde haya un cambio de signo

xarray = np.linspace(10,25,100)
yarray = np.zeros(100)

for i in range(100):
    yarray[i] = fun(xarray[i])

plt.plot(xarray,yarray)
plt.grid()

#print(fun(14))

x0 = 10
x1 = 25

for i in range(100):
    f0 = fun(x0)
    f1 = fun(x1)
    if f0*f1 > 0 :
        print("No hay raiz en este rango: "+f0+" , "+f1)
        break
    x = (x0+x1)/2
    fx = fun(x)
    if fx*f1 < 0:
        x0 = x
    else:
        x1 = x
    
    if abs(fx) < 0.001:
        break
print("La raiz es %.5f"%x0)
