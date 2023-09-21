import numpy as np
import matplotlib.pyplot as plt

def PoincareDynamic(inf, Conjugated=True):
    def f(z):
        return np.vectorize(inf)(z)
    
    def Height(u, v):
        if Conjugated:
            XX, YY = np.cos(v) * u, -np.sin(v) * u
        else:
            XX, YY = np.cos(v) * u, np.sin(v) * u
        ZZ = f(XX + 1j * YY)
        ZZ = np.abs(ZZ)
        return np.angle(1j * ZZ)
    
    u = np.linspace(0, 1, 100)
    v = np.linspace(0, 2 * np.pi, 100)
    
    u, v = np.meshgrid(u, v)
    
    X = u * np.cos(v)
    Y = u * np.sin(v)
    Z = np.pi - Height(u, v)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, facecolors=plt.cm.hsv(Z), rstride=10, cstride=10)
    plt.show()

def PoincareDynamicTest(inf, Conjugated=True):
    def f(z):
        return np.vectorize(inf)(z)
    
    def Height(u, v):
        if Conjugated:
            XX, YY = np.cos(v) * u, -np.sin(v) * u
        else:
            XX, YY = np.cos(v) * u, np.sin(v) * u
        ZZ = f(XX + 1j * YY)
        ZZ = np.abs(ZZ)
        return np.angle(1j * ZZ)
    
    u = np.linspace(0, 1, 100)
    v = np.linspace(0, 2 * np.pi, 100)
    
    u, v = np.meshgrid(u, v)
    
    X = u * np.cos(v)
    Y = u * np.sin(v)
    Z = np.pi - Height(u, v)
    
    return X, Y, Z
