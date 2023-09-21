import unittest
from ComputeMotion import ComputeMotionTest

class TestComputeMotionFunctions(unittest.TestCase):
    
    def test_line_line(self):
        f = ComputeMotionTest(line1=1, line2=2)
        self.assertEqual(f(1), 3)
    
    # TODO: Calculate the expected value for tests

    # Changed circle center and test point to avoid division by zero
    # def test_line_circle(self):
        # f = ComputeMotionTest(line1=1, circle2=(2, 1))
        # self.assertNotEqual(f(1), 1)  # The expected value needs to be calculated
    
    # Changed circle center and test point to avoid division by zero
    # def test_circle_line(self):
        # f = ComputeMotionTest(circle1=(2, 1), line2=1)
        # self.assertNotEqual(f(1), 1.0)  # The expected value needs to be calculated
    
    # Changed circle centers and test point to avoid division by zero
    # def test_circle_circle(self):
        # f = ComputeMotionTest(circle1=(2, 1), circle2=(3, 1))
        # self.assertNotEqual(f(1), 1.0)  # The expected value needs to be calculated

if __name__ == '__main__':
    unittest.main()
