from .modules.currency.module import CurrencyParser
from .modules.datetime.module import DateTimeUtil
from .modules.enums.module import EnumModule
# from .modules.region.region_matcher import RegionMatcher
from .modules.internal.regex.module import RegexUtility
from .modules.contact.module import ContactExtractor
from .modules.internal.text.module import TextNormalizer
from .modules.internal.cast.module import TypeCaster
from .modules.internal.fuzzy.module import FuzzyMatcher


class Tweaker:
    
    def __init__(self):
        self._regex = RegexUtility()
        self._normalizer = TextNormalizer(regex=self._regex)
        self._cast = TypeCaster(regex=self._regex)
        self._fuzzy = FuzzyMatcher()

        self.contact = ContactExtractor(regex=self._regex)
        self.currency = CurrencyParser(
            normalizer=self._normalizer, 
            regex=self._regex,
            cast=self._cast,
        )
        self.datetime = DateTimeUtil(normalizer=self._normalizer)
        self.enum = EnumModule(normalizer=self._normalizer)
