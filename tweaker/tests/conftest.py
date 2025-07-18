from tweaker.core.tweaker import Tweaker
import pytest


@pytest.fixture(scope="session")
def tweaker() -> Tweaker:
    return Tweaker()