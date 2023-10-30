import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from Support import arg, sph2pln, sphX, sphY, sphZ, pol2sph, plot, pi_2
from matplotlib import colors
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import zeta  # Importing the Zeta function from SciPy
from scipy.ndimage import gaussian_filter



# Initialization
L, R, T, B = -10, 10, 10, -10
gridside = 500
count = 0
satmarks = 10

# Initialize arrays A and C
A = np.zeros((gridside+1, gridside+1), dtype=np.float64)
C = np.zeros((gridside+1, gridside+1, 3), dtype=np.float64)

def f(z):
    try:
        f = (z - 5)**2 * (z + 5)**5
        # f = 1 / ((2 - z) * (1 - z))
        return f
    except ZeroDivisionError:
        return 0

def arglines(t):
    anglemarks = 10
    return 1 if 0.50 <= np.ceil(anglemarks * t) - anglemarks * t else 1 + (-1) * 0.45 * (np.ceil(anglemarks * t) - anglemarks * t) / 0.5

def ing(z):
    return z if z <= 1 else np.log(z + np.exp(1) - 1)

def saturation(t, satmarks):
    return 1 - 0.6 * (np.ceil(satmarks * t) - satmarks * t)**10

# Loop over the grid
for n in range(gridside + 1):
    if gridside + L == 0:
        x = 0
    else:
        # x = n * (R - L) / gridside + L
        x = ((n / gridside) * (R - L)) + L
    for m in range(gridside + 1):
        if gridside + B == 0:
            y = 0
        else:
            # y = m * (T - B) / gridside + B
            y = ((m / gridside) * (T - B)) + B
        image = f(complex(x, y))
        A[n, m] = np.abs(image)

        if np.imag(image) < 0:
            ARG = pi_2 + arg(image)
        else:
            ARG = arg(image)

        
        H = ARG / pi_2
        S = saturation(ARG / pi_2, satmarks)
        V = 1 - 0.6 * (ing(np.abs(image)) - np.floor(ing(np.abs(image))))

        while H > 1:
            H = H - 1
        if H < 0:
            H = H * -1
        else:
            C[n, m, 0] = H
        
        while S > 1:
            S = S - 1
        if S < 0:
            S = S * -1
        else:
            C[n, m, 1] = S
            
        while V > 1:
            V = V - 1
        if V < 0:
            V = V * -1
        else:
            C[n, m, 2] = V

# Plotting
plot(C, L, R, gridside, B, T, A)
# Resetting A for the next plot
A[:, :] = -1
plot(C, L, R, gridside, B, T, A)

gridside = 500
A = np.zeros((gridside+1, gridside+1), dtype=np.float64)
C = np.zeros((gridside+1, gridside+1, 3), dtype=np.float64)

for n in range(gridside + 1):
    u = 2 * np.pi * n / gridside
    for m in range(gridside + 1):
        v = np.pi * m / gridside

        x, y, z = pol2sph(u, v)
        X, Y = sph2pln(x, y, z)
        image = f(X + 1j * Y)

        A[n, m, :] = [x, y, z]

        if np.imag(image) < 0:
            ARG = pi_2 + np.angle(image)
        else:
            ARG = np.angle(image)

        H = ARG / pi_2
        S = saturation(ARG / pi_2, satmarks)
        V = 1 - 0.6 * (ing(np.abs(image)) - np.floor(ing(np.abs(image))))

        while H > 1:
            H = H - 1
        if H < 0:
            H = H * -1
        else:
            C[n, m, 0] = H
        
        while S > 1:
            S = S - 1
        if S < 0:
            S = S * -1
        else:
            C[n, m, 1] = S
            
        while V > 1:
            V = V - 1
        if V < 0:
            V = V * -1
        else:
            C[n, m, 2] = V


C_RGBA = colors.hsv_to_rgb(C)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(A[:,:,0], A[:,:,1], A[:,:,2], facecolors=C_RGBA, rstride=5, cstride=5)
plt.show()


############ With Angle Lines ###############

L, R, T, B = -3, 3, 3, -3
gridside = 500
A = np.zeros((gridside+1, gridside+1), dtype=np.float64)

# Populate A and C
for n in range(gridside + 1):
    x = n * (R - L) / gridside + L
    for m in range(gridside + 1):
        y = m * (T - B) / gridside + B
        image = f(x + y * 1j)  # 1j is the imaginary unit in Python
        A[n, m] = abs(image)
        
        ARG = arg(image)
        if ARG < 0:
            ARG += 2 * np.pi
            
        C[n, m, 0] = ARG / (2 * np.pi)
        C[n, m, 1] = 1
        C[n, m, 2] = 1 - 0.25 * (ing(abs(image)) - np.floor(ing(abs(image)))) - 0.25 * (np.ceil(10 * ARG / (2 * np.pi)) - 10 * ARG / (2 * np.pi))

plot(C,L,R,gridside,B,T,A)

# Flat Version


for n in range(gridside + 1):
    for m in range(gridside + 1):
        A[n, m] = -1

plot(C,L,R,gridside,B,T,A)
# With Rings

# elif inp == '3' or inp == '5':
center = 0
r1 = 1
r2 = 2
linewidth = abs(R - L) / 100  # You had a syntax error in your Maple code for this
for n in range(gridside + 1):
    x = n * (R - L) / gridside + L
    for m in range(gridside + 1):
        y = m * (T - B) / gridside + B
        distance_to_center = abs(complex(x, y) - center)

        if (r1 - linewidth <= distance_to_center <= r1 + linewidth) or (r2 - linewidth <= distance_to_center <= r2 + linewidth):
            C[n, m, 0] = 0
            C[n, m, 1] = 0
            C[n, m, 2] = 0

plot(C,L,R,gridside,B,T,A)

gridside = 500
A = np.zeros((gridside+1, gridside+1, 3), dtype=np.float64)  # Similar to your A definition, but now with an extra dimension for the 3 values
C = np.zeros((gridside+1, gridside+1, 3), dtype=np.float64)  # HSV color space


def Ans(u, v):
    try:
        X, Y = sph2pln(*pol2sph(u, v))  
        if X is np.nan or Y is np.nan:
            return 0, 0
        image = f(X + 1j * Y)  
    except ZeroDivisionError:
        return 0, 0
    return image, zeta  # Return both the image and the zeta_value


for n in range(gridside+1):
    u = 2 * np.pi * n / gridside
    for m in range(gridside+1):
        v = np.pi * m / gridside
        image, zeta = Ans(u, v)  # Retrieve both image and zeta_value

        A[n, m, 0] = sphX(u, v)
        A[n, m, 1] = sphY(u, v)
        A[n, m, 2] = sphZ(u, v)

        ARG = arg(image)
        if ARG < 0:
            ARG += 2 * np.pi

        C[n, m, 0] = ARG / (2 * np.pi)
        C[n, m, 1] = 1
        C[n, m, 2] = 1 - 0.25 * (ing(abs(image)) - np.floor(ing(abs(image)))) - 0.25 * (np.ceil(10 * ARG / (2 * np.pi)) - 10 * ARG / (2 * np.pi))

C_RGBA = colors.hsv_to_rgb(C)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Use the slices of A as the X, Y, Z values
X = A[:,:,0]
Y = A[:,:,1]
Z = A[:,:,2]

# Plotting the surface plot
ax.plot_surface(X, Y, Z, facecolors=C_RGBA)

plt.show()

smoothed_C = gaussian_filter(C, sigma=1)

C_RGBA = colors.hsv_to_rgb(smoothed_C)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Use the slices of A as the X, Y, Z values
X = A[:,:,0]
Y = A[:,:,1]
Z = A[:,:,2]

# Plotting the surface plot
ax.plot_surface(X, Y, Z, facecolors=C_RGBA)

plt.show()


