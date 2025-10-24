from typing import Literal, Tuple, TypeAlias
from ..internal.text.module import TextNormalizer
from ...base_module import BaseModule

KeywordMatchType: TypeAlias = Literal["token", "substring"]


class KeywordMatcher(BaseModule):
    """
    Lightweight keyword matching utility for text classification or data cleaning.

    Uses a two-step matching strategy:
    1. Token match  → "token"  (high precision)
    2. Substring match → "substring" (broader recall)

    Designed for use with Tweaker's TextNormalizer to ensure consistent text hygiene.
    """

    def __init__(self, normalizer: TextNormalizer):
        """
        Initialize with a shared TextNormalizer instance and a set of pre-normalized keywords.
        """
        self.normalizer = normalizer

    def match(self, s: str, keywords: set[str]) -> Tuple[str, KeywordMatchType] | None:
        """
        Attempt to find a keyword in text using two passes:
        1. Token match (returns "token")
        2. Substring match (returns "substring")
        Returns (matched_keyword, match_type) or None.
        """
        token_result = self.match_tokens(s, keywords)
        if token_result:
            return token_result, "token"

        substring_result = self.match_substring(s, keywords)
        if substring_result:
            return substring_result, "substring"

        return None

    def match_tokens(self, text: str, keywords: set[str]) -> str | None:
        """
        Token-level match for highest precision.
        Example:
            "Full-spectrum CBD oil 30mL" → matches "oil"
        """
        tokens = set(self.normalizer.tokenize(text))
        for kw in keywords:
            if kw in tokens:
                return kw

        return None

    def match_substring(self, text: str, keywords: set[str], keep_whitespace: bool = True) -> str | None:
        """
        Substring match for broader recall, preserving whitespace.
        Example:
            "Pre Roll 3.5g – APEX" → matches "pre roll"
        """
        normalized = self.normalizer.normalize(text, keep_whitespace=keep_whitespace)
        for kw in keywords:
            if kw in normalized:
                return kw

        return None
