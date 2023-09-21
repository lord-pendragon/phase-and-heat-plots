import numpy as np
import matplotlib.pyplot as plt

def PoincareUltraDynamic(inf, Conjugated=True):
    def f(z):
        return np.vectorize(inf)(z)
    
    def Height(u, v):
        XX, YY = np.cos(v) * u, np.sin(v) * u
        if Conjugated:
            XX, YY = XX, -YY
        ZZ = f(XX + 1j * YY)
        ZZ = np.real(ZZ)
        return np.angle(ZZ)
    
    u = np.linspace(0, 1, 100)
    v = np.linspace(0, 2 * np.pi, 100)
    
    u, v = np.meshgrid(u, v)
    
    X = u * np.cos(v)
    Y = u * np.sin(v)
    Z = Height(u, v)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, facecolors=plt.cm.hsv(Z), rstride=10, cstride=10)
    plt.show()

def PoincareUltraDynamicTest(inf, Conjugated=True):
    def f(z):
        return np.vectorize(inf)(z)
    
    def Height(u, v):
        XX, YY = np.cos(v) * u, np.sin(v) * u
        if Conjugated:
            XX, YY = XX, -YY
        ZZ = f(XX + 1j * YY)
        ZZ = np.real(ZZ)
        return np.angle(ZZ)
    
    u = np.linspace(0, 1, 100)
    v = np.linspace(0, 2 * np.pi, 100)
    
    u, v = np.meshgrid(u, v)
    
    X = u * np.cos(v)
    Y = u * np.sin(v)
    Z = Height(u, v)
    
    return X, Y, Z
