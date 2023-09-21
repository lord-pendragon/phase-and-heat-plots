import sys
sys.path.append('../src')

from Planar import planar

def mock_inf(p):
    return p * 2

def test_planar():
        pa1 = (0, 1)
        pa2 = (0, 1)
        planar(mock_inf, pa1, pa2)

test_planar()
