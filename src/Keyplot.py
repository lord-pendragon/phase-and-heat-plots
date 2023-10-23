import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def keyplot(inf, pa1, pa2):
    def f(x, y):
        return inf(x, y)

    if '=' in pa1:
        rngx = pa1.split('=')[1]
    else:
        rngx = pa1

    if '=' in pa2:
        rngy = pa2.split('=')[1]
    else:
        rngy = pa2

    yhi, ylo = float(rngy.split('..')[1]), float(rngy.split('..')[0])
    
    def ired(z):
        if z <= 1/8:
            return 1/2 + 4*z
        elif 1/8 < z < 3/8:
            return 1
        elif 3/8 <= z <= 5/8:
            return 5/2 - 4*z
        else:
            return 0

    def igreen(z):
        if z <= 1/8:
            return 0
        elif 1/8 < z < 3/8:
            return 4*z - 1/2
        elif 3/8 <= z <= 5/8:
            return 1
        elif 5/8 < z <= 7/8:
            return 7/2 - 4*z
        else:
            return 0

    def iblue(z):
        if z <= 3/8:
            return 0
        elif 3/8 < z <= 5/8:
            return 4*z - 3/2
        elif 5/8 < z <= 7/8:
            return 1
        else:
            return 9/2 - 4*z
            
    def color_func(x, y):
        z = (y - ylo) / (yhi - ylo)
        return [ired(z), igreen(z), iblue(z)]

    x = np.linspace(float(rngx.split('..')[0]), float(rngx.split('..')[1]), 100)
    y = np.linspace(ylo, 0.2*yhi, 100)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, facecolors=[color_func(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')

    plt.show()