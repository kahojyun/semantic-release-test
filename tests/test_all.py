import pytest
import aeipathy

def test_all():
    assert aeipathy.hello("Alice") == "Hello, Alice!"
    assert aeipathy.add(1, 2) == 3
    assert aeipathy.multiply(2, 3) == 6
    assert aeipathy.subtract(5, 3) == 2
    assert aeipathy.divide(10, 2) == 5
