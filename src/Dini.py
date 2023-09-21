import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar

def Dini(inf, inumax, wraps=2, twist=0.5):
    def f(z):
        return np.vectorize(inf)(z)

    def umax_eq(u):
        return np.exp(u) ** 2 * u - np.exp(u) ** 2 * inumax - np.exp(u) ** 2 + u - inumax + 1
    
    umax = root_scalar(umax_eq, bracket=[0, 50], method='brentq').root
    u = np.linspace(0, umax, 100)
    v = np.linspace(0, wraps * 2 * np.pi, 100)
    
    u, v = np.meshgrid(u, v)
    
    X = np.cosh(u)**(-1) * np.cos(v)
    Y = np.cosh(u)**(-1) * np.sin(v)
    Z = u - np.tanh(u) - twist * v
    
    Z_value = f(v + 1j * np.exp(u))
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, facecolors=plt.cm.hsv(Z_value), rstride=10, cstride=10)
    plt.show()

def DiniTest(inf, inumax, wraps=2, twist=0.5):
    def f(z):
        return np.vectorize(inf)(z)

    def umax_eq(u):
        return np.exp(u) ** 2 * u - np.exp(u) ** 2 * inumax - np.exp(u) ** 2 + u - inumax + 1
    
    umax = root_scalar(umax_eq, bracket=[0, 50], method='brentq').root
    u = np.linspace(0, umax, 100)
    v = np.linspace(0, wraps * 2 * np.pi, 100)
    
    u, v = np.meshgrid(u, v)
    
    X = np.cosh(u)**(-1) * np.cos(v)
    Y = np.cosh(u)**(-1) * np.sin(v)
    Z = u - np.tanh(u) - twist * v
    
    return X, Y, Z
