import phonenumbers
from phonenumbers import PhoneNumberFormat, PhoneNumberMatcher
from ...base_module import BaseModule


class PhoneSniffer(BaseModule):

    def extract_number(self, text: str, region: str = "US", **kwargs) -> str | None:
        _matches = PhoneNumberMatcher(text, region, **kwargs)
        for _match in _matches:
            number = _match.number
            if phonenumbers.is_valid_number(number):
                return phonenumbers.format_number(number, PhoneNumberFormat.E164)
        return None

    def extract_numbers(self, text: str, region: str = "US", **kwargs) -> list[str]:
        results = []
        _matches = PhoneNumberMatcher(text, region, **kwargs)
        for _match in _matches:
            number = _match.number
            if phonenumbers.is_valid_number(number):
                formatted = phonenumbers.format_number(number, PhoneNumberFormat.E164)
                results.append(formatted)

        return results
    
