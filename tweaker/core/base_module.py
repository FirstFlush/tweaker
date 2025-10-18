from abc import ABC
from typing import Any


class BaseModule(ABC):
    ...
        

class BaseSubstringMapping:
    
    @staticmethod
    def get_key(text: str, mapping: dict[Any, set[str]]) -> str | None:
        for k, v in mapping.items():
            if any(s in text for s in v):
                return k

    @staticmethod
    def get_key_with_match(text: str, mapping: dict[Any, set[str]]) -> tuple[str, str] | None:
        for k, v in mapping.items():
            for time_str in v:
                if time_str in text:
                    return k, time_str