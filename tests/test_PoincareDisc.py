import unittest
import sys
sys.path.append('../src')

from PoincareDisc import PoincareDiscTest

def mock_inf(p):
    return p * 2

class TestPoincareDiscFunctions(unittest.TestCase):

    def test_PoincareDisc(self):
        X, Y, Z = PoincareDiscTest(mock_inf)
        self.assertEqual(X.shape, (100, 100))
        self.assertEqual(Y.shape, (100, 100))
        self.assertEqual(Z.shape, (100, 100))

if __name__ == '__main__':
    unittest.main()
