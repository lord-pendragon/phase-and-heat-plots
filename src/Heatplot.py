import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def Heatplot(inf, pa1, pa2, numpoints=100, axes=None, scaling='auto', view=None, orientation=None):
    def f(x, y):
        return inf(x, y)
        
    if "=" in pa1:
        rngx = pa1.split("=")[1]
    else:
        rngx = pa1

    if "=" in pa2:
        rngy = pa2.split("=")[1]
    else:
        rngy = pa2

    yhi, ylo = float(rngy.split("..")[1]), float(rngy.split("..")[0])
    
    def ired(z):
        return 0.5 + 4 * z if z <= 1 / 8 else 1 if 1 / 8 < z < 3 / 8 else 5 / 2 - 4 * z

    def igreen(z):
        return 0 if z <= 1 / 8 else 4 * z - 0.5 if 1 / 8 < z < 3 / 8 else 1
    
    def iblue(z):
        return 0 if z <= 3 / 8 else 4 * z - 3 / 2 if 3 / 8 < z < 5 / 8 else 1
    
    def clip_value(value):
        if value > 2:
            return 1
        elif value > 1:
            return value - 1
        elif value < -1:
            return 0
        elif value < 0:
            return value * -1
        else:
            return value

    def color_func(x, y):
        z = (y - ylo) / (yhi - ylo)
        red = clip_value(ired(z))
        green = clip_value(igreen(z))
        blue = clip_value(iblue(z))
        return [red, green, blue]


    x = np.linspace(float(rngx.split("..")[0]), float(rngx.split("..")[1]), numpoints)
    y = np.linspace(ylo, yhi, numpoints)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    
    facecolors = np.array([[color_func(x, y) for x, y in zip(row_x, row_y)] for row_x, row_y in zip(X, Y)])
    facecolors = np.array(facecolors)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, facecolors=facecolors)
    
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')

    if axes == 'framed':
        ax.grid(True, linestyle='-', linewidth=0.5, color='black')
    
    ax.auto_scale_xyz([float(rngx.split("..")[0]), float(rngx.split("..")[1])], [ylo, yhi], [Z.min(), Z.max()])
    
    if view:
        ax.view_init(elev=view[0], azim=view[1])
        
    plt.show()

# Example usage
