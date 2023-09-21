import unittest
import sys
sys.path.append('../src')

from Pseudosphere import pseudosphereTest

def mock_inf(p):
    return p * 2

class TestPseudosphereFunctions(unittest.TestCase):

    def test_pseudosphere(self):
        X, Y, Z = pseudosphereTest(mock_inf, 5)
        self.assertEqual(X.shape, (100, 100))
        self.assertEqual(Y.shape, (100, 100))
        self.assertEqual(Z.shape, (100, 100))

if __name__ == '__main__':
    unittest.main()
