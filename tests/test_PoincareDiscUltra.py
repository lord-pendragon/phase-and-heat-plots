import unittest
import sys
sys.path.append('../src')

from PoincareDiscUltra import PoincareDiscUltraTest

def mock_inf(z):
    return z * 2

class TestPoincareDiscUltraFunctions(unittest.TestCase):
    
    def test_PoincareDiscUltra(self):
        X, Y, Z = PoincareDiscUltraTest(mock_inf)
        self.assertEqual(X.shape, (100, 100))
        self.assertEqual(Y.shape, (100, 100))
        self.assertEqual(Z.shape, (100, 100))

if __name__ == '__main__':
    unittest.main()
