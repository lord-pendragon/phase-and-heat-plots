import cmath
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


# Math and complex math related libraries

# Constants for pi
pi_1 = np.pi  # Equivalent to `1*Pi` in Maple
pi_2 = 2 * np.pi  # Equivalent to `2*Pi` in Maple
pi_half = np.pi / 2  # Equivalent to `Pi/2` in Maple

# Cartesian unit sphere to Cartesian plane transformation
def sph2pln(x, y, z):

    # Transforms Cartesian unit sphere coordinates to Cartesian plane coordinates.
    # Parameters are X,Y and Z coordinates on the unit sphere
    # returns a tuple containing the transformed coordinates (X, Y)
    if z == 1:
        return 0, 0 # Check if results in division by zero, in which case return 0
    
    else:
        return x / (1 - z), y / (1 - z)

# Alias for sph2pln
s2p = sph2pln

# Parameterization of the unit sphere in terms of polar coordinates
# Calculates the X-coordinate of a point on the unit sphere given its polar coordinates.
# Parameters are Polar coordinates u and v
# returns X,Y and Z coordinate of the point on the unit sphere respectively
    
def sphX(u, v):
    return np.sqrt(1 - np.cos(v) ** 2) * np.cos(u)

def sphY(u, v):
    return np.sqrt(1 - np.cos(v) ** 2) * np.sin(u)

def sphZ(u, v):
    return np.cos(v)

# Polar to spherical transformation
def pol2sph(u, v):

    # Transforms polar coordinates to spherical coordinates
    # Parameters are again Polar coordinates u and v
    # returns a tuple containing the transformed coordinates (X, Y, Z)
    
    return sphX(u, v), sphY(u, v), sphZ(u, v)

# Upper half plane in Cartesian to interior of unit disc
def T(X, Y):
    
    # Transforms the upper half plane in Cartesian to the interior of the unit disc.
    # Parameters are X and Y Cartesian coordinates
    # returns a tuple containing the transformed coordinates (x, y) 
    
    return (2 * X / (X ** 2 + Y ** 2 + 2 * Y + 1), 
            1 - 2 / (X ** 2 + Y ** 2 + 2 * Y + 1) * Y - 2 / (X ** 2 + Y ** 2 + 2 * Y + 1))

# Compute the argument of a complex number
def arg(Z):
    
    # Computes the argument of a complex number.
    # Parameter is a complex number
    # Returns the argument of the complex number
    
    ans = cmath.phase(Z)
    if ans < 0:
        ans += pi_2
    return ans


def plot(C, L, R, gridside, B, T, A):
    
    C_RGBA = colors.hsv_to_rgb(C)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Convert A and C to suitable formats for Matplotlib
    X, Y = np.meshgrid(np.linspace(L, R, gridside + 1), np.linspace(B, T, gridside + 1))

    # Plotting the surface plot
    ax.plot_surface(X, Y, A.T, facecolors=C_RGBA)

    plt.show()
