import unittest
import sys
sys.path.append('../src')

from PoincareUltraDynamic import PoincareUltraDynamicTest

def mock_inf(z):
    return z * 2

class TestPoincareUltraDynamicFunctions(unittest.TestCase):
    
    def test_PoincareUltraDynamic(self):
        X, Y, Z = PoincareUltraDynamicTest(mock_inf)
        self.assertEqual(X.shape, (100, 100))
        self.assertEqual(Y.shape, (100, 100))
        self.assertEqual(Z.shape, (100, 100))

if __name__ == '__main__':
    unittest.main()
