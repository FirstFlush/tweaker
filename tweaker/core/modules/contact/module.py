from ...base_module import BaseModule
from .address import AddressExtractor
from.email import EmailExtractor
from.phone import PhoneExtractor
from ..internal.regex.module import RegexUtility


class ContactExtractor(BaseModule):
    
    def __init__(self, regex: RegexUtility):
        self.address = AddressExtractor(regex)
        self.email = EmailExtractor(regex)
        self.phone = PhoneExtractor()