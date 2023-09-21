import unittest
import sys
sys.path.append('../src')

from KleinUltra import KleinUltraTest

def mock_inf(z):
    return z * 2

class TestKleinUltraFunctions(unittest.TestCase):
    
    def test_KleinUltra(self):
        X, Y, Z = KleinUltraTest(mock_inf)
        self.assertEqual(X.shape, (100, 100))
        self.assertEqual(Y.shape, (100, 100))
        self.assertEqual(Z.shape, (100, 100))

if __name__ == '__main__':
    unittest.main()
