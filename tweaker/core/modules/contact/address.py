from ...base_module import BaseModule
from ..internal.regex.module import RegexUtility

class AddressExtractor(BaseModule):
    
    def __init__(self, regex: RegexUtility):
        self.regex = regex