# test_operaciones.py

import pytest
from operaciones import suma, resta, multiplicacion, division

def test_suma():
    assert suma(9, 5) == 8
    assert suma(-3, 5) == 2

def test_resta():
    assert resta(10, 5) == 5
    assert resta(-10, 5) == -15

def test_multiplicacion():
    assert multiplicacion(4, 5) == 20
    assert multiplicacion(-4, 5) == -20

def test_division():
    assert division(10, 2) == 5
    assert division(-10,0) == -5
    with pytest.raises(ValueError):
        division(10, 0)
