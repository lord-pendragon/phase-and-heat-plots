import numpy as np
import matplotlib.pyplot as plt
from Support import arg, sph2pln, sphX, sphY, sphZ, pol2sph, plot, pi_2
from matplotlib import colors
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import zeta  # Importing the Zeta function from SciPy
from scipy.ndimage import gaussian_filter


def visualizeFunction(visualType, f, useAngleLines = False, useSaturation = False, useRings = False, L=-3, R=3, T=3, B=-3, gridside=500,anglemarks = 10, satmarks = 10):
    
    # Identify which visualization to use
    showPhasePortrait = False
    showFlatPortrait = False
    showReimannSphere = False

    if visualType == 1:
        showPhasePortrait = True
        print("PhasePortrait Selected")
    elif visualType == 2:
        showFlatPortrait = True
        print("FlatPortrait Selected")
    elif visualType == 3:
        showReimannSphere = True
        print("ReimannSphere Selected")
    else:
        print("Invalid Visual Type")
        return
    
        # Initialize arrays similar to Maple's A and C
    A = np.zeros((gridside+1, gridside+1), dtype=np.float64)
    C = np.zeros((gridside+1, gridside+1, 3), dtype=np.float64)

    def ing(z):
        return z if z <= 1 else np.log(z + np.exp(1) - 1)

    # Define the arglines function if useAngleLines is True
    if useAngleLines:
        print("AngleLines Enabled")

        def arglines(t):
            return 1 if 0.50 <= np.ceil(anglemarks * t) - anglemarks * t else 1 + (-1) * 0.45 * (np.ceil(anglemarks * t) - anglemarks * t) / 0.5

    # Define the saturation function if useSaturation is True
    if useSaturation:
        print("Saturation Enabled")
        satmarks = 10  # Example value, set as needed

        def saturation(t):
            return 1 + (-1) * 0.6 * (np.ceil(satmarks * t) - satmarks * t) ** 10

    
    # Core Logic
    # This is where you would put the core logic for each visualization type
    if showReimannSphere:
        print("ReimannSphere Selected")
        
        # Reset A and C for 3D
        A = np.zeros((gridside+1, gridside+1, 3), dtype=np.float64)
        C = np.zeros((gridside+1, gridside+1, 3), dtype=np.float64)
        
        # Example SphX, SphY, SphZ, and Ans functions
        # Replace these with your actual functions
        def SphX(u, v): return np.sin(v) * np.cos(u)
        def SphY(u, v): return np.sin(v) * np.sin(u)
        def SphZ(u, v): return np.cos(v)
        def Ans(u, v): return np.sin(u) + np.cos(v)
        
        for n in range(gridside + 1):
            u = 2 * np.pi * n / gridside
            for m in range(gridside + 1):
                v = np.pi * m / gridside
                image = Ans(u, v)
                
                A[n, m, 0] = SphX(u, v)
                A[n, m, 1] = SphY(u, v)
                A[n, m, 2] = SphZ(u, v)
                
                if np.imag(image) < 0:
                    ARG = 2 * np.pi + np.angle(image)
                else:
                    ARG = np.angle(image)
                
                C[n, m, 0] = ARG / (2 * np.pi)
                if useSaturation:
                    C[n, m, 1] = saturation(ARG / (2 * np.pi))
                else:
                    C[n, m, 1] = 1
                
                if useAngleLines:
                    C[n, m, 2] = 1 - 0.6 * (ing(np.abs(image)) - np.floor(ing(np.abs(image))))
                else:
                    C[n, m, 2] = 1 - 0.25 * (ing(abs(image)) - np.floor(ing(abs(image)))) - 0.25 * (np.ceil(10 * ARG / (2 * np.pi)) - 10 * ARG / (2 * np.pi))

        # Plotting using Matplotlib
        C_RGBA = colors.hsv_to_rgb(C)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        X = A[:,:,0]
        Y = A[:,:,1]
        Z = A[:,:,2]

        ax.plot_surface(X, Y, Z, facecolors=C_RGBA)

        plt.show()

    if showPhasePortrait:
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

                if useSaturation:
                    C[n, m, 1] = saturation(ARG / (2 * np.pi))
                else:
                    C[n, m, 1] = 1
                
                if useAngleLines:
                    C[n, m, 2] = 1 - 0.6 * (ing(np.abs(image)) - np.floor(ing(np.abs(image))))
                else:
                    C[n, m, 2] = 1 - 0.25 * (ing(abs(image)) - np.floor(ing(abs(image)))) - 0.25 * (np.ceil(10 * ARG / (2 * np.pi)) - 10 * ARG / (2 * np.pi))

    # Logic for Flat Portrait
    elif showFlatPortrait:
        for n in range(gridside + 1):
            for m in range(gridside + 1):
                A[n, m] = -1  # Resetting A[n, m]
                x = n * (R - L) / gridside + L
                y = m * (T - B) / gridside + B
                image = f(complex(x, y))
                A[n, m] = np.abs(image)
                
                ARG = arg(image)
                C[n, m, 0] = ARG / (2 * np.pi)
                
                if useSaturation:
                    C[n, m, 1] = saturation(ARG / (2 * np.pi))
                else:
                    C[n, m, 1] = 1
                
                if useAngleLines:
                    C[n, m, 2] = 1 - 0.6 * (ing(np.abs(image)) - np.floor(ing(np.abs(image))))
                else:
                    C[n, m, 2] = 1 - 0.25 * (ing(abs(image)) - np.floor(ing(abs(image)))) - 0.25 * (np.ceil(10 * ARG / (2 * np.pi)) - 10 * ARG / (2 * np.pi))

    if useRings:
        center = 0
        r1 = 1
        r2 = 2
        linewidth = abs(R - L) / 100 
        for n in range(gridside + 1):
            x = n * (R - L) / gridside + L
            for m in range(gridside + 1):
                y = m * (T - B) / gridside + B
                distance_to_center = abs(complex(x, y) - center)

                if (r1 - linewidth <= distance_to_center <= r1 + linewidth) or (r2 - linewidth <= distance_to_center <= r2 + linewidth):
                    C[n, m, 0] = 0
                    C[n, m, 1] = 0
                    C[n, m, 2] = 0

    if showFlatPortrait:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.view_init(azim=-90, elev=0)
        
        X, Y = np.meshgrid(np.linspace(L, R, gridside + 1), np.linspace(B, T, gridside + 1))

        C_RGBA = colors.hsv_to_rgb(C)

        ax.plot_surface(X, Y, A.T, facecolors=C_RGBA)
        ax.grid(False)

    elif showPhasePortrait:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        X, Y = np.meshgrid(np.linspace(L, R, gridside + 1), np.linspace(B, T, gridside + 1))

        C_RGBA = colors.hsv_to_rgb(C)

        ax.plot_surface(X, Y, A.T, facecolors=C_RGBA)

    plt.show()



def f(z):

    if z == 1 or z == 2:
        return 0 # Handle instances of division by zero
    
    else:
        return 1 / ((2 - z) * (1 - z))

option = input("Choose type of visualization, 1 = Phase Portrait, 2 = Flat, 3 = Reimann Sphere\n")
visualType = option
option = input("Angle Lines? 1 = Yes, 2 = No\n")
useAngleLines = False
if int(option) == 1:
    useAngleLines = True
option = input("Saturation? 1 = Yes, 2 = No\n")
useSaturation = False
if int(option) == 1:
    useSaturation = True
option = input("Rings? 1 = Yes, 2 = No\n")
useRings = False
if int(option) == 1:
    useRings = True
option = input("Custom or Default inputs? 1 = Custom, 2 = Default \n")
if int(option) == 1:
    L = input("Enter L\n")
    R = input("Enter R\n")
    T = input("Enter T\n")
    B = input("Enter B\n")
    gridside = input("Enter gridsize\n")

    if useAngleLines:
        anglemarks = input("Enter anglemarks\n")
    elif useSaturation:
        satmarks = input("Enter satmarks\n")

    visualizeFunction(int(visualType), f, useAngleLines, useSaturation, useRings, L, R, T, B, gridside,anglemarks,satmarks)
else:
    visualizeFunction(int(visualType), f, useAngleLines, useSaturation, useRings)



# visualizeFunction(visualType, f, useAngleLines = False, useSaturation = False, useRings = False, L=-3, R=3, T=3, B=-3, gridside=500,anglemarks = 10, satmarks = 10):
    