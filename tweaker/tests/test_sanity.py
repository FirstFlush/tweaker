import pytest
from tweaker.core.tweaker import Tweaker


def test_sanity():
    t = Tweaker()
    assert isinstance(t, Tweaker)