import unittest
import numpy as np
import sys
sys.path.append('../src')  # Replace with the actual path

from Heatplot import heatplot  # Assuming the function is in a file named Heatplot.py

class TestHeatplotFunctions(unittest.TestCase):

    def mock_func(self, x, y):
        return x + y
    
    def test_heatplot(self):

        #TODO: Pending implementation of Heatplots

        heatplot(self.mock_func, (-10, 10), (-10, 10))
        
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
