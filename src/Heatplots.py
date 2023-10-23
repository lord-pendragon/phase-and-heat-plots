from Heatplot import Heatplot
import numpy as np
from sympy import Subs, symbols, diff, solve, exp, lambdify

x, y, lambda_ = symbols('x y lambda')
f = lambda_ * x**2 / 2 + (1 - lambda_) * exp(x)

derivative = diff(y * x - f, x)

solution = solve(derivative, x)

attainingslope = solution[0]

homotopy_expr = Subs(f, x, attainingslope).doit()

def homotopy(x, lambda_):
    return lambda_ * x ** 2 / 2 + (1 - lambda_) * np.exp(x)

Heatplot(homotopy, "x=-3..8", "y=0.1e-6..1", numpoints=2**10, axes='framed', scaling='unconstrained', view=[-3, 8, 0, 1, -1, 7], orientation=[90, 90, 180])
