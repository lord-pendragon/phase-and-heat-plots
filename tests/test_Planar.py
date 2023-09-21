import unittest
import sys
sys.path.append('../src')

from Planar import planar

def mock_inf(p):
    return p * 2

class TestPlanarFunctions(unittest.TestCase):

    def test_planar(self):
        pa1 = (0, 1)
        pa2 = (0, 1)
        X, Y, Z = planar(mock_inf, pa1, pa2)
        

if __name__ == '__main__':
    unittest.main()
