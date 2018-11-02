#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 08:45:40 2018

@author: memoherrera

Metodo numerico Bairstow

para la funcion f(x) = x**5 - 3.5*x**4 + 2.75*x**3 + 2.125*x**2 - 3.875*x + 1.25


"""

def bn(listaCoef): 
    return listaCoef[-1]

def bn1(listaCoef,b,r):
    return listaCoef[-2] + b*r

def bi(i,a,r,s,b):
    return a[i] + r*b[0] + s*b[1]

def cn(b):
    return bn(b)

def cn1(b,c,r):
    return bn1(b,c,r)

def ci(i,b,r,s,c):
    return bi(i,b,r,s,c)



listaCoef = [1.25, -3.875, 2.125, 2.75, -3.5, 1]
r = -1
s = -1
b = []
c = []
b.append(bn(listaCoef))
b.insert(0,bn1(listaCoef,b[0],r))
print(b)

for i in reversed(range(0,4)):
    b.insert(0, bi(i,listaCoef, r,s,b))

c.append(cn(b))
c.insert(0,cn1(b,c[0],r))

for i in reversed(range(0,4)):
    print(i)
    c.insert(0, ci(i,b,r,s,c))

print(b)
print(c)