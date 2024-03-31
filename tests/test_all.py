import pytest
import aeipathy

def test_all():
    assert aeipathy.hello() == "Hello, world!"
    assert aeipathy.goodbye() == "Goodbye, world!"
    assert aeipathy.add(1, 2) == 3
