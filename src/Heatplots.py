from Heatplot import Heatplot
import numpy as np
from sympy import Subs, symbols, diff, solve, exp, lambdify

# Define the functions
x, y, lambda_ = symbols('x y lambda')
f = lambda_ * x**2 / 2 + (1 - lambda_) * exp(x)

# Take the derivative
derivative = diff(y * x - f, x)
# Solve for x
solution = solve(derivative, x)
# Store the solution for the attaining slope
attainingslope = solution[0]
# Substitute the value of attainingslope into f
homotopy_expr = Subs(f, x, attainingslope).doit()

def homotopy(x, lambda_):
    return lambda_ * x ** 2 / 2 + (1 - lambda_) * np.exp(x)

Heatplot(homotopy, "x=-3..8", "y=0.1e-6..1", numpoints=2**10, axes='framed', scaling='unconstrained', view=[-3, 8, 0, 1, -1, 7], orientation=[90, 90, 180])
