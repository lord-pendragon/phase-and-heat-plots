import unittest
import sys
sys.path.append('../src')

from Stereographic import stereographicTest

def mock_inf(p):
    return p * 2

class TestStereographicFunctions(unittest.TestCase):

    def test_stereographic(self):
        X, Y, Z = stereographicTest(mock_inf)
        self.assertEqual(X.shape, (100, 100))
        self.assertEqual(Y.shape, (100, 100))
        self.assertEqual(Z.shape, (100, 100))

if __name__ == '__main__':
    unittest.main()
