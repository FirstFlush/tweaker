from .modules.currency.currency_parser import CurrencyParser
from .modules.datetime_util.datetime_util import DateTimeUtil
from .modules.enums.enum_toolkit import EnumToolkit 
from .modules.region.region_matcher import RegionMatcher
from .modules.regex.regex import RegexTool
from .modules.contact.contact import ContactSniffer
from .modules.text.text_module import TextModule
from .modules.types_util.types import TypeTransformer


class Tweaker:
    
    def __init__(self):
        self.contact = ContactSniffer(self)
        self.currency = CurrencyParser(self)
        self.date = DateTimeUtil(self)
        self.enum = EnumToolkit(self)
        self.regex = RegexTool(self)
        self.region = RegionMatcher(self)
        self.text = TextModule(self)
        self.types = TypeTransformer(self)
