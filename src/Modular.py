import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
sys.path.append('../src')

def Modular(inf, pa1, pa2):
    def f(z):
        return np.vectorize(inf)(z)
    
    if isinstance(pa1, tuple):
        rngx = np.linspace(pa1[0], pa1[1], 100)
    else:
        rngx = np.full(100, pa1)

    if isinstance(pa2, tuple):
        rngy = np.linspace(pa2[0], pa2[1], 100)
    else:
        rngy = np.full(100, pa2)

    X, Y = np.meshgrid(rngx, rngy)
    Z = np.abs(f(X + 1j * Y))

    ColorFunc_H = np.angle(f(X + 1j * Y)) / (2 * np.pi)
    ColorFunc_S = np.ones_like(X)
    ColorFunc_V = np.ones_like(X)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, facecolors=plt.cm.hsv(ColorFunc_H), rstride=10, cstride=10)
    
    plt.show()

def ModularTest(inf, pa1, pa2):
    def f(z):
        return np.vectorize(inf)(z)
    
    if isinstance(pa1, tuple):
        rngx = np.linspace(pa1[0], pa1[1], 100)
    else:
        rngx = np.full(100, pa1)

    if isinstance(pa2, tuple):
        rngy = np.linspace(pa2[0], pa2[1], 100)
    else:
        rngy = np.full(100, pa2)

    X, Y = np.meshgrid(rngx, rngy)
    Z = np.abs(f(X + 1j * Y))
    
    return X, Y, Z
