import cmath
import math

# Math and complex math related libraries

# Constants for pi
pi_1 = math.pi  # Equivalent to `1*Pi` in Maple
pi_2 = 2 * math.pi  # Equivalent to `2*Pi` in Maple
pi_half = math.pi / 2  # Equivalent to `Pi/2` in Maple

# Cartesian unit sphere to Cartesian plane transformation
def sph2pln(x, y, z):

    # Transforms Cartesian unit sphere coordinates to Cartesian plane coordinates.
    # Parameters are X,Y and Z coordinates on the unit sphere
    # returns a tuple containing the transformed coordinates (X, Y)
    
    return x / (1 - z), y / (1 - z)

# Alias for sph2pln
s2p = sph2pln

# Parameterization of the unit sphere in terms of polar coordinates
# Calculates the X-coordinate of a point on the unit sphere given its polar coordinates.
# Parameters are Polar coordinates u and v
# returns X,Y and Z coordinate of the point on the unit sphere respectively
    
def sphX(u, v):

    return math.sqrt(1 - math.cos(v) ** 2) * math.cos(u)

def sphY(u, v):

    return math.sqrt(1 - math.cos(v) ** 2) * math.sin(u)

def sphZ(u, v):
    return math.cos(v)

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
