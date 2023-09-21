import cmath
import numpy as np

def PoincarePlanarUltra(inf, rngx, rngy, Conjugated=True):
    def f(p):
        return inf(p)

    def IK(z):
        return 2 * (z + 1j) / abs(z + 1j)**2 - 1j

    if Conjugated:
        TP = lambda z: IK(z).conjugate()
        invTP = lambda z: IK(z.conjugate())
    else:
        TP = lambda z: IK(z)
        invTP = lambda z: IK(z)

    def modulusmap(z):
        return abs(z)

    def squaremap(z):
        return z**2

    def toplot(z):
        return (1j * TP(modulusmap(f(invTP(z)))))**2

    def ColorFunc(x, y):
        return cmath.phase(toplot(x + 1j * y)) / (2 * np.pi), 1

    return ColorFunc

def PoincarePlanarUltraTest(inf, rngx, rngy, Conjugated=True):
    return PoincarePlanarUltra(inf, rngx, rngy, Conjugated)

