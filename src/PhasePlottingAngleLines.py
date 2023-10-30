import cmath
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import zeta  # Importing the Zeta function from SciPy
from scipy.ndimage import gaussian_filter
from Support import arg, plot, sphX, sphY, sphZ, sph2pln, pol2sph

# Implementing safe Zeta function call
def safe_zeta(x):
    try:
        return zeta(x)
    except:
        return 0  # return 0 if any exception occurs

L, R, T, B = -3, 3, 3, -3
gridside = 500

# Change this line to create a 3D array for A
A = np.zeros((gridside+1, gridside+1, 3), dtype=np.float64)

def f(z):

    if z == 1 or z == 2:
        return 0 # Handle instances of division by zero
    
    else:
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

def arglines(t):
    anglemarks = 10
    return 1 if 0.50 <= np.ceil(anglemarks * t) - anglemarks * t else 1 + (-1) * 0.45 * (np.ceil(anglemarks * t) - anglemarks * t) / 0.5

# Populate A and C
for n in range(gridside + 1):
    x = n * (R - L) / gridside + L
    for m in range(gridside + 1):
        y = m * (T - B) / gridside + B
        image = f(x + y * 1j)  # 1j is the imaginary unit in Python
        A[n, m] = abs(image)
        
        ARG = arg(image)
        if ARG < 0:
            ARG += 2 * np.pi
            
        C[n, m, 0] = ARG / (2 * np.pi)
        C[n, m, 1] = 1
        C[n, m, 2] = 1 - 0.25 * (ing(abs(image)) - np.floor(ing(abs(image)))) - 0.25 * (np.ceil(10 * ARG / (2 * np.pi)) - 10 * ARG / (2 * np.pi))

plot(C,L,R,gridside,B,T,A)

# Flat Version


for n in range(gridside + 1):
    for m in range(gridside + 1):
        A[n, m] = -1

plot(C,L,R,gridside,B,T,A)
# With Rings

center = 0
r1 = 1
r2 = 2
linewidth = abs(R - L) / 100 
for n in range(gridside + 1):
    x = n * (R - L) / gridside + L
    for m in range(gridside + 1):
        y = m * (T - B) / gridside + B
        distance_to_center = abs(complex(x, y) - center)

        if (r1 - linewidth <= distance_to_center <= r1 + linewidth) or (r2 - linewidth <= distance_to_center <= r2 + linewidth):
            C[n, m, 0] = 0
            C[n, m, 1] = 0
            C[n, m, 2] = 0

plot(C,L,R,gridside,B,T,A)

gridside = int(input('Enter Gridsize for Sphere:\n'))

A = np.zeros((gridside+1, gridside+1, 3), dtype=np.float64)  
C = np.zeros((gridside+1, gridside+1, 3), dtype=np.float64)  # HSV color space


def Ans(u, v):
    try:
        X, Y = sph2pln(*pol2sph(u, v))  
        if X is np.nan or Y is np.nan:
            return 0, 0
        image = f(X + 1j * Y)  
    except ZeroDivisionError:
        return 0, 0
    return image, zeta  # Return both the image and the zeta_value


for n in range(gridside+1):
    u = 2 * np.pi * n / gridside
    for m in range(gridside+1):
        v = np.pi * m / gridside
        image, zeta = Ans(u, v)  # Retrieve both image and zeta_value

        A[n, m, 0] = sphX(u, v)
        A[n, m, 1] = sphY(u, v)
        A[n, m, 2] = sphZ(u, v)

        ARG = arg(image)
        if ARG < 0:
            ARG += 2 * np.pi

        C[n, m, 0] = ARG / (2 * np.pi)
        C[n, m, 1] = 1
        C[n, m, 2] = 1 - 0.25 * (ing(abs(image)) - np.floor(ing(abs(image)))) - 0.25 * (np.ceil(10 * ARG / (2 * np.pi)) - 10 * ARG / (2 * np.pi))

C_RGBA = colors.hsv_to_rgb(C)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = A[:,:,0]
Y = A[:,:,1]
Z = A[:,:,2]

ax.plot_surface(X, Y, Z, facecolors=C_RGBA)

plt.show()

smoothed_C = gaussian_filter(C, sigma=1)

C_RGBA = colors.hsv_to_rgb(smoothed_C)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = A[:,:,0]
Y = A[:,:,1]
Z = A[:,:,2]

ax.plot_surface(X, Y, Z, facecolors=C_RGBA)

plt.show()
