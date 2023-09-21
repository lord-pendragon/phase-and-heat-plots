import unittest
import sys
sys.path.append('../src')

from Klein import KleinTest

def mock_inf(p):
    return p * 2

class TestKleinFunctions(unittest.TestCase):

    def test_Klein(self):
        X, Y, Z = KleinTest(mock_inf)
        self.assertEqual(X.shape, (100, 100))
        self.assertEqual(Y.shape, (100, 100))
        self.assertEqual(Z.shape, (100, 100))

if __name__ == '__main__':
    unittest.main()
