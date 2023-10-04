import cmath
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from mpl_toolkits.mplot3d import Axes3D
from Support import plot


L, R, T, B = -3, 3, 3, -3
gridside = 500
A = np.zeros((gridside+1, gridside+1), dtype=np.float64)

def f(z):
    # TODO: Implement support for Laurent function
    # TODO: Implement Maple Sum function here
    return 1 / ((2 - z) * (1 - z))
    # laurent(1/((2 - z)*(1 - z)), z = 1);
    # f := z -> Sum((1 - (1/2)^(k + 1))*z^k, k = 0 .. 40);
    # f := z -> Sum(-z^(-k), k = 1 .. 40) + Sum(-z^k/2^(k + 1), k = 0 .. 40);
    # f := z -> Sum((2^(k - 1) - 1)*z^(-k), k = 1 .. 40);
    # f := z -> 1/((2 - z)*(1 - z));

# COLORING

C = np.zeros((gridside + 1, gridside + 1, 3), dtype=np.float64)

def ing(z):
    return z if z <= 1 else np.log(z + np.exp(1) - 1)
    # ing := z->z;

def arglines(t):
    anglemarks = 10
    return 1 if 0.50 <= np.ceil(anglemarks * t) - anglemarks * t else 1 + (-1) * 0.45 * (np.ceil(anglemarks * t) - anglemarks * t) / 0.5
    # arglines := t -> 1:
    # arglines := t -> 1- 0.6*`(ceil(anglemarks*t) - anglemarks*t)^10

# TODO: NumericEventHanlders need to be implemented here

inp = input("Please select type of Visualization:\n1 = Normal\n2 = Flat\n3 = With Rings\n4 = Zeta\n5 = All\nO = Exit\n")

if inp != '0':
# Populate A and C
    for n in range(gridside + 1):
        x = n * (R - L) / gridside + L
        for m in range(gridside + 1):
            y = m * (T - B) / gridside + B
            image = f(x + y * 1j)  # 1j is the imaginary unit in Python
            A[n, m] = abs(image)
            
            ARG = cmath.phase(image)
            if ARG < 0:
                ARG += 2 * np.pi
                
            C[n, m, 0] = ARG / (2 * np.pi)
            C[n, m, 1] = 1
            C[n, m, 2] = 1 - 0.25 * (ing(abs(image)) - np.floor(ing(abs(image)))) - 0.25 * (np.ceil(10 * ARG / (2 * np.pi)) - 10 * ARG / (2 * np.pi))

# Flat Version

if inp == '2' or inp == '5':
    for n in range(gridside + 1):
        for m in range(gridside + 1):
            A[n, m] = -1

# With Rings

elif inp == '3' or inp == '5':
    center = 0
    r1 = 1
    r2 = 2
    linewidth = abs(R - L) / 100  # You had a syntax error in your Maple code for this
    for n in range(gridside + 1):
        x = n * (R - L) / gridside + L
        for m in range(gridside + 1):
            y = m * (T - B) / gridside + B
            distance_to_center = abs(complex(x, y) - center)

            if (r1 - linewidth <= distance_to_center <= r1 + linewidth) or (r2 - linewidth <= distance_to_center <= r2 + linewidth):
                C[n, m, 0] = 0
                C[n, m, 1] = 0
                C[n, m, 2] = 0


elif inp == '4' or inp == '5':
    print('Plotting Zeta')
    # TODO: Implement the Zeta Plotting, gridside = 500

if inp != '0':
    plot(C,L,R,gridside,B,T,A)