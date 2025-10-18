from enum import Enum
from typing import Type, TypeVar
from ...base_module import BaseModule
from ..text.module import TextNormalizer

E = TypeVar("E", bound=Enum)


class EnumModule(BaseModule):

    def __init__(self, normalizer: TextNormalizer):
        self.normalizer = normalizer

    def match(self, text: str, enum_cls: Type[E]) -> E | None:
        try:
            return enum_cls(text)
        except ValueError:
            return None

    def match_by_normalized_value(
            self,
            enum_cls: Type[E],
            text: str
    ) -> E | None:
        """
        Finds the enum member whose normalized value matches the given text.
        Useful for fuzzy or format-insensitive enum lookups.
        """
        normalized = self.normalizer.normalize(text)
        for member in enum_cls:
            if self.normalizer.normalize(member.value) == normalized:
                return member
            
        return None