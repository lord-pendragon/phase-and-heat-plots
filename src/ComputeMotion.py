import cmath

def ComputeMotion(line1=None, line2=None, circle1=None, circle2=None):
    def f1(z):
        if line1 is not None:
            return -z + 2 * line1
        elif circle1 is not None:
            center1, radius1 = circle1
            denominator = z.conjugate() - center1
            if abs(denominator) < 1e-10:  # some small threshold to avoid division by zero
                raise ValueError("Division by zero in f1")
            return (center1 * z.conjugate() + radius1**2 - center1**2) / denominator
        else:
            raise ValueError("User error in defining geodesic 1")

    def f2(z):
        if line2 is not None:
            return -z + 2 * line2
        elif circle2 is not None:
            center2, radius2 = circle2
            denominator = z.conjugate() - center2
            if abs(denominator) < 1e-10:  # some small threshold to avoid division by zero
                raise ValueError("Division by zero in f2")
            return (center2 * z.conjugate() + radius2**2 - center2**2) / denominator
        else:
            raise ValueError("User error in defining geodesic 2")

            
    def f(z):
        return f2(f1(z))
    
    return f

def ComputeMotionTest(line1=None, line2=None, circle1=None, circle2=None):
    # Same as ComputeMotion but easier to test
    return ComputeMotion(line1, line2, circle1, circle2)
