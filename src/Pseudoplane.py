import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def Pseudoplane(inf, xmin, xmax, ymin, ymax, logscale=False, outside="Black"):
    def f(p):
        return np.vectorize(inf)(p)
        
    if ymin < 0:
        print("WARNING: Negative y<0 not plotted")
        
    X = np.linspace(xmin, xmax, 100)
    Y = np.linspace(max(0, ymin), ymax, 100)
    X, Y = np.meshgrid(X, Y)
    Z = f(X + 1j * Y)
    
    Z_real = np.real(Z) / (2 * np.pi)
    
    ColorFunc_H = np.where((Z_real > 1) | (Z_real < 0), 0, Z_real)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, np.ones_like(X), facecolors=plt.cm.hsv(ColorFunc_H), rstride=10, cstride=10)
    
    if logscale:
        plt.yscale('log')
    
    plt.show()

def PseudoplaneTest(inf, xmin, xmax, ymin, ymax):
    def f(p):
        return np.vectorize(inf)(p)
        
    X = np.linspace(xmin, xmax, 100)
    Y = np.linspace(max(0, ymin), ymax, 100)
    X, Y = np.meshgrid(X, Y)
    Z = f(X + 1j * Y)
    
    return X, Y, Z
