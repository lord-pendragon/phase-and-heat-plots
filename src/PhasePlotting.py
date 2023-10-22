import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from Support import arg, sph2pln, sphX, sphY, sphZ, pol2sph, plot, pi_2, pi_1

# Initialization
L, R, T, B = -10, 10, 10, -10
gridside = 500
count = 0
satmarks = 10

# Initialize arrays A and C
A = np.zeros((gridside+1, gridside+1), dtype=np.float64)
C = np.zeros((gridside+1, gridside+1, 3), dtype=np.float64)

# Function definition
def f(z):
    return (z - 5)**2 * (z + 5)**5

def ing(z):
    if z <= 1:
        return z
    else:
        return np.log(z + np.exp(1) - 1)

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
A = np.zeros((gridside+1, gridside+1, 3))
C = np.zeros((gridside+1, gridside+1, 3))

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

        C[n, m, 0] = ARG / pi_2
        C[n, m, 1] = 1
        C[n, m, 2] = 1 - 0.6 * (ing(np.abs(image)) - np.floor(ing(np.abs(image))))


C_RGBA = colors.hsv_to_rgb(C)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(A[:,:,0], A[:,:,1], A[:,:,2], facecolors=C_RGBA, rstride=5, cstride=5)
plt.show()
