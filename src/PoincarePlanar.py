import numpy as np
import matplotlib.pyplot as plt
import cmath

def PoincarePlanar(inf, pa1, pa2, Conjugated=True):
    # Define the function f
    def f(p):
        return inf(p)
    
    # Extract the x and y ranges
    if "=" in pa1:
        rngx = list(map(float, pa1.split("=")[1].split("..")))
    else:
        rngx = list(map(float, pa1.split("..")))

    if "=" in pa2:
        rngy = list(map(float, pa2.split("=")[1].split("..")))
    else:
        rngy = list(map(float, pa2.split("..")))

    # Define the transformations
    def IK(z):
        return 2 * (z + 1j) / abs(z + 1j)**2 - 1j
    
    if Conjugated:
        TP = lambda z: np.conj(IK(z))
        invTP = lambda z: IK(np.conj(z))
    else:
        TP = lambda z: IK(z)
        invTP = lambda z: IK(z)
    
    def toplot(z):
        return TP(np.real(f(invTP(z))))
    
    # Create the color function
    def color_func(x, y):
        hue = np.angle(toplot(x + 1j * y)) / (2 * np.pi)
        saturation = 1
        value = 1
        return hue, saturation, value
    
    # Generate the data for plotting
    x = np.linspace(rngx[0], rngx[1], 100)
    y = np.linspace(rngy[0], rngy[1], 100)
    X, Y = np.meshgrid(x, y)
    Z = np.ones_like(X)
    
    # Generate the color data
    hue, saturation, value = np.vectorize(color_func)(X, Y)
    color_data = np.stack([hue, saturation, value], axis=-1)
    
    # Create the 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, facecolors=plt.cm.hsv(color_data))
    
    # Draw the unit circle
    theta = np.linspace(0, 2 * np.pi, 100)
    x_circle = np.cos(theta)
    y_circle = np.sin(theta)
    ax.plot(x_circle, y_circle, 0, color='black')
    
    plt.show()


def PoincarePlanarTest():
    # Example usage
    def example_inf(p):
        return p**2

    PoincarePlanar(example_inf, "x=-1..1", "y=-1..1")
