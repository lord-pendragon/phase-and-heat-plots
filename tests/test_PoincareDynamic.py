import unittest
import sys
sys.path.append('../src')

from PoincareDynamic import PoincareDynamicTest

def mock_inf(z):
    return z * 2

class TestPoincareDynamicFunctions(unittest.TestCase):
    
    def test_PoincareDynamic(self):
        X, Y, Z = PoincareDynamicTest(mock_inf)
        self.assertEqual(X.shape, (100, 100))
        self.assertEqual(Y.shape, (100, 100))
        self.assertEqual(Z.shape, (100, 100))

if __name__ == '__main__':
    unittest.main()
