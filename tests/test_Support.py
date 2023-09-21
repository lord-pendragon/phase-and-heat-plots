import unittest
import sys
sys.path.append('../src')

from Support import sph2pln, s2p, sphX, sphY, sphZ, pol2sph, T, arg

class TestSupportFunctions(unittest.TestCase):

    def test_sph2pln(self):
        result = sph2pln(1, 2, 3)
        expected = (-0.5, -1.0)
        for a, b in zip(result, expected):
            self.assertAlmostEqual(a, b, places=4)

    def test_s2p(self):
        result = s2p(1, 2, 3)
        expected = (-0.5, -1.0)
        for a, b in zip(result, expected):
            self.assertAlmostEqual(a, b, places=4)

    def test_sphX(self):
        self.assertAlmostEqual(sphX(1, 2), 0.4913, places=4)

    def test_sphY(self):
        self.assertAlmostEqual(sphY(1, 2), 0.7651, places=4)

    def test_sphZ(self):
        self.assertAlmostEqual(sphZ(1, 2), -0.4161, places=4)

    def test_pol2sph(self):
        result = pol2sph(1, 2)
        expected = (sphX(1, 2), sphY(1, 2), sphZ(1, 2))
        for a, b in zip(result, expected):
            self.assertAlmostEqual(a, b, places=4)

    def test_T(self):
        result = T(1, 2)
        expected = (0.2, 0.4)
        for a, b in zip(result, expected):
            self.assertAlmostEqual(a, b, places=4)

    def test_arg(self):
        self.assertAlmostEqual(arg(1 + 2j), 1.1071, places=4)

if __name__ == '__main__':
    unittest.main()
