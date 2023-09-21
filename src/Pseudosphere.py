import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import root_scalar
import sys
sys.path.append('../src')

def pseudosphere(inf, inumax):
    def f(z):
        return np.vectorize(inf)(z)
    
    def Ans(u, v):
        return np.real(f(v + 1j * np.exp(u)))
    
    def func(umax):
        return umax - np.tanh(umax) - inumax
    
    umax = root_scalar(func, bracket=[0, 100]).root
    
    u = np.linspace(0, umax, 100)
    v = np.linspace(0, 2 * np.pi, 100)
    U, V = np.meshgrid(u, v)
    
    X = np.cosh(U) * np.cos(V)
    Y = np.cosh(U) * np.sin(V)
    Z = U - np.tanh(U)
    
    ColorFunc_H = np.vectorize(Ans)(U, V)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, facecolors=plt.cm.hsv(ColorFunc_H), rstride=10, cstride=10)
    
    plt.show()

def pseudosphereTest(inf, inumax):
    def f(z):
        return np.vectorize(inf)(z)
    
    def Ans(u, v):
        return np.real(f(v + 1j * np.exp(u)))
    
    def func(umax):
        return umax - np.tanh(umax) - inumax
    
    umax = root_scalar(func, bracket=[0, 100]).root
    
    u = np.linspace(0, umax, 100)
    v = np.linspace(0, 2 * np.pi, 100)
    U, V = np.meshgrid(u, v)
    
    X = np.cosh(U) * np.cos(V)
    Y = np.cosh(U) * np.sin(V)
    Z = U - np.tanh(U)
    
    return X, Y, Z
