import unittest
import sys
sys.path.append('../src')

from PseudosphereNaive import PseudosphereNaiveTest

def mock_inf(z):
    return z * 2

class TestPseudosphereNaiveFunctions(unittest.TestCase):
    
    def test_PseudosphereNaive(self):
        X, Y, Z = PseudosphereNaiveTest(mock_inf, 10)
        self.assertEqual(X.shape, (100, 100))
        self.assertEqual(Y.shape, (100, 100))
        self.assertEqual(Z.shape, (100, 100))

if __name__ == '__main__':
    unittest.main()
