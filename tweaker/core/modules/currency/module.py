from decimal import Decimal, InvalidOperation
from ...base_module import BaseModule
from ..internal.text.module import TextNormalizer
from .mapping import CurrencyMapping
from ..internal.regex.module import RegexUtility
from ..internal.cast.module import TypeCaster

class CurrencyParser(BaseModule):
    
    currency_mapping = CurrencyMapping
    
    def __init__(self, normalizer: TextNormalizer, regex: RegexUtility, cast: TypeCaster):
        self.normalizer = normalizer
        self.regex = regex
        self.cast = cast

    def extract_amount(self, text: str) -> Decimal | None:
        """
        Extracts the first numeric amount from a text string (e.g. "$42.40 CAD after tax").
        Handles commas, decimals, and sign prefixes.
        Returns a Decimal for precision, or None if no valid number is found.
        """
        return self.cast.to_decimal(text)

    def resolve_currency_type(self, text: str) -> str | None:
        
        normalized = self.normalizer.normalize(text)
        currency_type = self.currency_mapping.get_key(
            text=normalized,
            mapping=self.currency_mapping.CURRENCY_TYPES
        )
        return currency_type if currency_type else None
    
    def _decimalize(self, num: str) -> Decimal | None:
        try:
            return Decimal(num)
        except InvalidOperation:
            return None
