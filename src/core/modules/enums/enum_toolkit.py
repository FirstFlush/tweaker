from enum import Enum
from typing import Type, TypeVar
from ...base_module import BaseModule


E = TypeVar("E", bound=Enum)


class EnumToolkit(BaseModule):
    
    def match_by_normalized_value(
            self,
            enum_cls: Type[E],
            text: str
    ) -> E | None:
        normalized = self.tweaker.text.normalize(text)
        for member in enum_cls:
            if self.tweaker.text.normalize(member.value) == normalized:
                return member
            
        return None