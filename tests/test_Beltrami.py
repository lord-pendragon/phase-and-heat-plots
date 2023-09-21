import unittest
import sys
sys.path.append('../src')

from Beltrami import BeltramiTest

def mock_inf(p):
    return p * 2

class TestBeltramiFunctions(unittest.TestCase):

    def test_Beltrami(self):
        X, Y, Z = BeltramiTest(mock_inf)
        self.assertEqual(X.shape, (100, 100))
        self.assertEqual(Y.shape, (100, 100))
        self.assertEqual(Z.shape, (100, 100))

if __name__ == '__main__':
    unittest.main()
