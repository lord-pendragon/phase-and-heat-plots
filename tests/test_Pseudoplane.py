import unittest
import sys
sys.path.append('../src')

from Pseudoplane import PseudoplaneTest

def mock_inf(z):
    return z * 2

class TestPseudoplaneFunctions(unittest.TestCase):
    
    def test_Pseudoplane(self):
        X, Y, Z = PseudoplaneTest(mock_inf, -1, 1, -1, 1)
        self.assertEqual(X.shape, (100, 100))
        self.assertEqual(Y.shape, (100, 100))
        self.assertEqual(Z.shape, (100, 100))

if __name__ == '__main__':
    unittest.main()
