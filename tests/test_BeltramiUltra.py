import unittest
import sys
sys.path.append('../src')

from BeltramiUltra import BeltramiUltraTest

def mock_inf(z):
    return z * 2

class TestBeltramiUltraFunctions(unittest.TestCase):
    
    def test_BeltramiUltra(self):
        X, Y, Z = BeltramiUltraTest(mock_inf)
        self.assertEqual(X.shape, (100, 100))
        self.assertEqual(Y.shape, (100, 100))
        self.assertEqual(Z.shape, (100, 100))

if __name__ == '__main__':
    unittest.main()
