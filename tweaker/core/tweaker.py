import warnings
from .modules.contact.module import ContactExtractor
from .modules.currency.module import CurrencyParser
from .modules.datetime.module import DateTimeUtil
from .modules.enums.module import EnumModule
from .modules.keyword.module import KeywordMatcher
from .modules.measure.module import MeasurementModule

from .modules.internal.cast.module import TypeCaster
from .modules.internal.fuzzy.module import FuzzyMatcher
from .modules.internal.text.module import TextNormalizer
from .modules.internal.regex.module import RegexUtility


class Tweaker:
    
    def __init__(self):
        self._regex = RegexUtility()
        self._normalizer = TextNormalizer(regex=self._regex)    # deprecated
        warnings.warn(
            "Tweaker._normalizer is deprecated. Use Tweaker.text instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        self._cast = TypeCaster(regex=self._regex)
        self.text = TextNormalizer(regex=self._regex)
        self._fuzzy = FuzzyMatcher()
        self.contact = ContactExtractor(regex=self._regex)
        self.currency = CurrencyParser(
            normalizer=self._normalizer, 
            regex=self._regex,
            cast=self._cast,
        )
        self.datetime = DateTimeUtil(normalizer=self._normalizer)
        self.enum = EnumModule(normalizer=self._normalizer)
        self.keyword = KeywordMatcher(normalizer=self._normalizer)
        self.measure = MeasurementModule()