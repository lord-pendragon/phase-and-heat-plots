import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
sys.path.append('../src')
from Support import sph2pln, pol2sph, sphX, sphY, sphZ

def Beltrami(inf, Conjugated=True):
    def f(z):
        return np.vectorize(inf)(z)
    
    def Ans(u, v):
        X, Y = sph2pln(*pol2sph(u, v))
        
        if Conjugated:
            X, Y = X, -Y
        else:
            X, Y = X, Y
        
        Z = f(X + 1j * Y)
        
        X = np.real(Z)
        Y = 0
        
        return np.angle(X - 1j * Y)
    
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(-np.pi / 2, 0, 100)
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

def BeltramiTest(inf, Conjugated=True):
    def f(z):
        return np.vectorize(inf)(z)
    
    def Ans(u, v):
        X, Y = sph2pln(*pol2sph(u, v))
        
        if Conjugated:
            X, Y = X, -Y
        else:
            X, Y = X, Y
        
        Z = f(X + 1j * Y)
        
        X = np.real(Z)
        Y = 0
        
        return np.angle(X - 1j * Y)
    
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(-np.pi / 2, 0, 100)
    U, V = np.meshgrid(u, v)
    
    X = sphX(U, V)
    Y = sphY(U, V)
    Z = sphZ(U, V)
    
    return X, Y, Z
