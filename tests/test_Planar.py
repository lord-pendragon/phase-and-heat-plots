import unittest
import sys
sys.path.append('../src')

from Planar import planarTest

def mock_inf(p):
    return p * 2

class TestPlanarFunctions(unittest.TestCase):

    def test_planar(self):
        pa1 = (0, 1)
        pa2 = (0, 1)
        X, Y, Z = planarTest(mock_inf, pa1, pa2)
        self.assertEqual(X.shape, (50, 50))
        self.assertEqual(Y.shape, (50, 50))
        self.assertEqual(Z.shape, (50, 50))

if __name__ == '__main__':
    unittest.main()
