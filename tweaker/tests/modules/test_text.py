import pytest
from tweaker import Tweaker
from .testdata.text import normalize_testdata


class TestText:
    

    @pytest.mark.parametrize("testdata", normalize_testdata)
    def test_text_normalize(self, testdata: tuple[str, str], tweaker: Tweaker):
        assert tweaker.text.normalize(testdata[0], keep_whitespace=True) == testdata[1]