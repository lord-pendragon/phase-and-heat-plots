import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar

def PseudosphereNaive(inf, inumax):
    def f(z):
        return np.vectorize(inf)(z)
    
    def find_umax():
        return root_scalar(lambda u: u - np.tanh(u) - inumax, bracket=[0, 50]).root
    
    umax = find_umax()
    
    u = np.linspace(0, umax, 100)
    v = np.linspace(0, 2 * np.pi, 100)
    
    u, v = np.meshgrid(u, v)
    
    X = np.cosh(u)**(-1) * np.cos(v)
    Y = np.cosh(u)**(-1) * np.sin(v)
    Z = u - np.tanh(u)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, facecolors=plt.cm.hsv(Z), rstride=10, cstride=10)
    plt.show()

def PseudosphereNaiveTest(inf, inumax):
    def f(z):
        return np.vectorize(inf)(z)
    
    def find_umax():
        return root_scalar(lambda u: u - np.tanh(u) - inumax, bracket=[0, 50]).root
    
    umax = find_umax()
    
    u = np.linspace(0, umax, 100)
    v = np.linspace(0, 2 * np.pi, 100)
    
    u, v = np.meshgrid(u, v)
    
    X = np.cosh(u)**(-1) * np.cos(v)
    Y = np.cosh(u)**(-1) * np.sin(v)
    Z = u - np.tanh(u)
    
    return X, Y, Z
