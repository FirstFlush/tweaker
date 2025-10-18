from ..regex.module import RegexUtility
import unicodedata


class TextNormalizer:
    
    def __init__(self, regex: RegexUtility):
        self.regex = regex

    def normalize(self, text: str, keep_whitespace: bool = False) -> str:
        """
        Normalize a string for fuzzy matching or comparison:
        - Converts Unicode to normalized NFKC form
        - Strips punctuation
        - Converts to lowercase
        - Collapses all whitespace
        """
        delimiter = " " if keep_whitespace else ""
        return delimiter.join(self.tokenize(text))

    def tokenize(self, text: str) -> list[str]:
        unicode_normalized = self._normalize_unicode(text)
        dashes_replaced = self._replace_all_dashes(unicode_normalized)
        stripped_punctuation = self._strip_punctuation(dashes_replaced)
        return stripped_punctuation.lower().strip().split()


    def _replace_all_dashes(self, text: str, substitute: str = " ") -> str:
        """
        Replaces all dash and underscore chars with substitute value.
        """
        return text.replace("–", substitute).replace("—", substitute).replace("−", substitute)   \
        .replace("‒", substitute).replace("―", substitute).replace("‑", substitute)              \
        .replace("-", substitute).replace("_", substitute)


    def _strip_punctuation(self, text: str) -> str:
        return self.regex.sub(
            pattern=self.regex.common_patterns.PUNCTUATION, 
            repl="", 
            text=text
        ).strip()
    
    def _normalize_unicode(self, text: str) -> str:
        """
        Converts text to Unicode NFKC form.

        This flattens weird or invisible characters like:
        - Zero-width space (U+200B)
        - Non-breaking space (U+00A0)
        - Full-width characters (e.g. Ａ → A)
        - Ligatures or symbol-like characters (e.g. ① → 1)

        Useful for matching text from PDFs, web data, or user input.
        """
        return unicodedata.normalize("NFKC", text)
