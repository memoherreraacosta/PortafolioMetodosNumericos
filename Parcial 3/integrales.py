# Integral 1/x**2, sin(x**2) 
# h = 1, h = 0.5  h= 0.25
# Intervalo de 1 a 2
import numpy as np
import math
a = 1
b = 2
h = .25
n = int((b -a) / h)
x = np.linspace(1,2, n + 1)
def fun(x):
    return math.sin(x**2)

y = [fun(xi) for xi in x]


def trapecio(y,h):
    I = sum([2*yi for yi in y[1:-1]])
    I += y[0]
    I += y[-1]
    I *= h/2
    return I


def simpson13(y,h):
    I = 0
    I += y[0]
    I += y[-1]
    for i in range(1,len(y)-1):
        if  i % 2 != 0:
            I += 4*y[i]
        else:
            I += 2*y[i]
    I *= h/3
    return I
    
def simpson18(y,h):
    I = 0
    I += y[0]
    I += y[-1]
    for i in range(1,len(y)-1):
        if  i % 3 != 0:
            I += 3*y[i]
        else:
            I += 2*y[i]
    I *= 3*h/8
    return I
print("Trapecio", trapecio(y,h))
print("Simpson 1/3", simpson13(y,h))
print("Simpson 1/8", simpson18(y,h))
