import pytest
import aeipathy

def test_all():
    assert aeipathy.hello("Alice") == "Hello, Alice!"
    assert aeipathy.goodbye("Bob") == "Goodbye, Bob!"
    assert aeipathy.add(1, 2) == 3