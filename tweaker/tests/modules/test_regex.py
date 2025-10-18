from tweaker.core.tweaker import Tweaker
import pytest
from .testdata.emails import valid_emails, invalid_emails
from .testdata.numbers import invalid_floats, two_numbers, currency
from .testdata.urls import valid_urls, valid_urls_with_params, invalid_urls
from .testdata.text import punctuation_testdata


# class TestUrl:
#     @pytest.fixture(scope="class")
#     def pattern(self, tweaker: Tweaker) -> str:
#         return tweaker._regex.common_patterns.URL
#
#     @pytest.mark.parametrize("url", valid_urls + valid_urls_with_params)
#     def test_valid_urls(self, url: str, pattern: str, tweaker: Tweaker):
#         match = tweaker._regex.search(pattern, url)
#         assert match is not None
#
#     @pytest.mark.parametrize("url", invalid_urls)
#     def test_invalid_urls(self, url: str, pattern: str, tweaker: Tweaker):
#         match = tweaker._regex.search(pattern, url)
#         assert match is None


class TestPunctuation:
    
    @pytest.fixture(scope="class")
    def pattern(self, tweaker: Tweaker) -> str:
        return tweaker._regex.common_patterns.PUNCTUATION

    @pytest.mark.parametrize("testdata", punctuation_testdata)
    def test_punctuation(self, testdata: tuple[str, str], pattern: str, tweaker: Tweaker):
        result = tweaker._regex.sub(
            pattern=pattern,
            repl="",
            text=testdata[0]
        ).strip()
        assert result == testdata[1]


class TestToFloat:

    @pytest.fixture(scope="class")
    def pattern(self, tweaker: Tweaker) -> str:
        return tweaker._regex.common_patterns.TO_FLOAT

    @pytest.mark.parametrize("s", currency + two_numbers)
    def test_valid_floats(self, s: str, pattern: str, tweaker: Tweaker):
        match = tweaker._regex.search(pattern, s)
        assert match is not None

    @pytest.mark.parametrize("s", invalid_floats)
    def test_invalid_floats(self, s: str, pattern: str, tweaker: Tweaker):
        match = tweaker._regex.search(pattern, s)
        assert match is None


class TestEmail:

    @pytest.fixture(scope="class")
    def pattern(self, tweaker: Tweaker) -> str:
        return tweaker._regex.common_patterns.EMAIL

    @pytest.mark.parametrize("email", valid_emails)
    def test_email_valid(self, email: str, pattern: str, tweaker: Tweaker):
        match = tweaker._regex.search(pattern, email)
        assert match is not None

    @pytest.mark.parametrize("email", invalid_emails)
    def test_email_invalid(self, email: str, pattern: str, tweaker: Tweaker):
        match = tweaker._regex.search(pattern, email)
        assert match is None
