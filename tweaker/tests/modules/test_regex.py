from tweaker.core.tweaker import Tweaker
import pytest
from .testdata.emails import valid_emails, invalid_emails
from .testdata.numbers import invalid_floats, two_numbers, currency



@pytest.mark.parametrize("s", currency + two_numbers)
def test_valid_floats(s: str):
    t = Tweaker()
    pattern = t.regex.common_patterns.TO_FLOAT
    match = t.regex.search(pattern, s)
    assert match is not None
    
    
@pytest.mark.parametrize("s", invalid_floats)
def test_invalid_floats(s: str):
    t = Tweaker()
    pattern = t.regex.common_patterns.TO_FLOAT
    match = t.regex.search(pattern, s)
    assert match is None
    
    
    
    

@pytest.mark.parametrize("email", valid_emails)
def test_email_valid(email: str):
    
    t = Tweaker()
    pattern = t.regex.common_patterns.EMAIL
    match = t.regex.search(pattern, email)
    
    assert match is not None
    # assert isinstance(match, str)


@pytest.mark.parametrize("email", invalid_emails)
def test_email_invalid(email: str):
    
    t = Tweaker()
    match = t.regex.search(t.regex.common_patterns.EMAIL, email)
    assert match == None
