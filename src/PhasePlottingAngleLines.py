import cmath
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from mpl_toolkits.mplot3d import Axes3D

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

# Convert HSV to RGBA
C_RGBA = colors.hsv_to_rgb(C)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Convert A and C to suitable formats for Matplotlib
X, Y = np.meshgrid(np.linspace(L, R, gridside + 1), np.linspace(B, T, gridside + 1))

# Plotting the surface plot
ax.plot_surface(X, Y, A.T, facecolors=C_RGBA)

plt.show()


# TODO: Implement Flat version below this line

# TODO: Put rings

# TODO: Implement the Zeta Plotting, gridside = 500