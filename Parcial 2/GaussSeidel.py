#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 09:15:01 2018

@author: memoherrera

Guass-Seidel

Para lad ecuaciones 

3x1 -0.2x2 -0.5x3 = 8
0.1x1 +7x2 +0.4x3 = -19.5
0.4x1 -0.1 +10x3 = 72.4
"""

def getX1(x2, x3):
    return (8+ .2*x2 +.5*x3)/(3)
    
def getX2(x1, x3):
    return (-19.5 - .1*x1 +.3*x3)/(7)
    
def getX3(x1, x2):
    return (72.4 - .4*x1 +.1*x3)/(10)
#Valores iniciales 

x1 = 0.0
x2 = 0.0    
x3 = 0.0     
   
x1a = 0.00001
x2a = 0.00001
x3a = 0.00001
error = 0.01

for i in range(100):
    x1 = getX1(x2,x3)
    x2 = getX2(x1,x3)
    x3 = getX3(x1,x2)
    print("Iteracion: "+str(i)+" con valores x1: "+str(x1)+", x2: "+str(x2)+", x3: "+str(x3))
    #Calculo de errores
    ex1 = abs((x1a - x1)/x1a)
    ex2 = abs((x2a - x2)/x2a)
    ex3 = abs((x3a - x3)/x3a)
    
    if(ex1 < error and ex2 < error and ex3 < error):
        break
    x1a = x1 
    x2a = x2 
    x3a = x3
print("\nLos valores son: X1: "+str(x1)+", X2: "+str(x2)+", X3: "+str(x3))
