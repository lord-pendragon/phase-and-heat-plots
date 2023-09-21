import unittest
import sys
sys.path.append('../src')

from Modular import ModularTest

def mock_inf(p):
    return p * 2

class TestModularFunctions(unittest.TestCase):

    def test_Modular(self):
        X, Y, Z = ModularTest(mock_inf, (0, 1), (0, 1))
        self.assertEqual(X.shape, (100, 100))
        self.assertEqual(Y.shape, (100, 100))
        self.assertEqual(Z.shape, (100, 100))

if __name__ == '__main__':
    unittest.main()
