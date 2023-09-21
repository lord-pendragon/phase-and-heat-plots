import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import sys
sys.path.append('../src')
from Support import sph2pln, pol2sph, sphX, sphY, sphZ

def stereographic(inf):
    def f(z):
        return np.vectorize(inf)(z)

    def Ans(u, v):
        X, Y = sph2pln(*pol2sph(u, v))
        return np.angle(f(X + 1j * Y)) / (2 * np.pi)
    
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    U, V = np.meshgrid(u, v)
    
    X = sphX(U, V)
    Y = sphY(U, V)
    Z = sphZ(U, V)
    
    ColorFunc_H = np.vectorize(Ans)(U, V)
    ColorFunc_S = np.ones_like(U)
    ColorFunc_V = np.ones_like(U)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, facecolors=plt.cm.hsv(ColorFunc_H), rstride=10, cstride=10)
    
    plt.show()


def stereographicTest(inf):
    def f(z):
        return np.vectorize(inf)(z)

    def Ans(u, v):
        X, Y = sph2pln(*pol2sph(u, v))
        return np.angle(f(X + 1j * Y)) / (2 * np.pi)
    
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    U, V = np.meshgrid(u, v)
    
    X = sphX(U, V)
    Y = sphY(U, V)
    Z = sphZ(U, V)
    
    return X, Y, Z