import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def PoincareDiscUltra(inf, Conjugated=True):
    def f(z):
        return np.vectorize(inf)(z)

    u = np.linspace(0, np.pi, 100)
    v = np.linspace(0.01, np.pi, 100)
    U, V = np.meshgrid(u, v)

    X, Y = np.cos(U) * np.sin(V), np.sin(U) * np.sin(V)
    Z = np.cos(V)
    
    if Conjugated:
        X, Y = X, -Y

    Z_val = f(X + 1j * Y)
    
    X_new = np.abs(Z_val)
    Y_new = np.zeros_like(X_new)

    ColorFunc_H = np.angle(1j * X_new - Y_new) / (2 * np.pi)
    ColorFunc_S = np.ones_like(U)
    ColorFunc_V = np.ones_like(U)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, facecolors=plt.cm.hsv(ColorFunc_H), rstride=10, cstride=10)
    
    plt.show()

def PoincareDiscUltraTest(inf, Conjugated=True):
    def f(z):
        return np.vectorize(inf)(z)

    u = np.linspace(0, np.pi, 100)
    v = np.linspace(0.01, np.pi, 100)
    U, V = np.meshgrid(u, v)

    X, Y = np.cos(U) * np.sin(V), np.sin(U) * np.sin(V)
    Z = np.cos(V)

    if Conjugated:
        X, Y = X, -Y

    Z_val = f(X + 1j * Y)
    
    X_new = np.abs(Z_val)
    Y_new = np.zeros_like(X_new)
    
    return X, Y, Z
