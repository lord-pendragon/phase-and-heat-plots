import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def planar(inf, pa1, pa2):
    def f(p):
        return np.vectorize(inf)(p)
    
    # Extracting the parameter ranges
    if isinstance(pa1, tuple):
        rngx = pa1
    else:
        rngx = (pa1, pa1)
        
    if isinstance(pa2, tuple):
        rngy = pa2
    else:
        rngy = (pa2, pa2)
    
    # Generate 3D data
    x = np.linspace(rngx[0], rngx[1], 50)
    y = np.linspace(rngy[0], rngy[1], 50)
    X, Y = np.meshgrid(x, y)
    Z = np.ones_like(X)  # Since Z is always 1 in this case
    
    # Color function
    def color_func(x, y):
        return np.angle(f(x + 1j * y)) / (2 * np.pi)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot surface
    ax.plot_surface(X, Y, Z, facecolors=plt.cm.hsv(color_func(X, Y)))
    
    plt.show()
