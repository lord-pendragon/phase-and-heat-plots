import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def BeltramiUltra(inf, Conjugated=False):
    def f(z):
        return np.vectorize(inf)(z)
        
    theta = np.linspace(0, 2 * np.pi, 100)
    phi = np.linspace(-np.pi / 2, 0, 100)
    theta, phi = np.meshgrid(theta, phi)
    
    X = np.sin(phi) * np.cos(theta)
    Y = np.sin(phi) * np.sin(theta)
    Z = np.cos(phi)
    
    if Conjugated:
        Y = -Y
    
    T_X, T_Y = X, Y  # Transformation function T can be applied here
    Z_value = f(T_X + 1j * T_Y)
    
    Z_real = np.abs(Z_value)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, facecolors=plt.cm.hsv(Z_real), rstride=10, cstride=10)
    
    plt.show()

def BeltramiUltraTest(inf, Conjugated=False):
    def f(z):
        return np.vectorize(inf)(z)
        
    theta = np.linspace(0, 2 * np.pi, 100)
    phi = np.linspace(-np.pi / 2, 0, 100)
    theta, phi = np.meshgrid(theta, phi)
    
    X = np.sin(phi) * np.cos(theta)
    Y = np.sin(phi) * np.sin(theta)
    Z = np.cos(phi)
    
    return X, Y, Z
