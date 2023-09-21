import unittest
import sys
sys.path.append('../src')

from Dini import DiniTest

def mock_inf(z):
    return z * 2

class TestDiniFunctions(unittest.TestCase):
    
    def test_Dini(self):
        X, Y, Z = DiniTest(mock_inf, 10)
        self.assertEqual(X.shape, (100, 100))
        self.assertEqual(Y.shape, (100, 100))
        self.assertEqual(Z.shape, (100, 100))

if __name__ == '__main__':
    unittest.main()
