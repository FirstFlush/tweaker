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
        text = self._normalize_unicode(text)
        text = self.normalize_whitespace(text)
        text = self._normalize_symbols(text)
        text = self._normalize_dashes(text)
        text = self._strip_punctuation(text)
        return text.lower().strip().split()

    def normalize_text(self, text: str) -> str:
        """
        Normalize human-readable text (e.g. paragraphs, product descriptions).

        - Normalizes Unicode to NFKC (fixes full-width, ligatures, etc.)
        - Removes invisible or non-breaking space characters
        - Collapses multiple whitespace/newlines into single spaces
        - Standardizes typographic symbols (quotes, ellipses, bullets)
        - Replaces all dash variants with a standard ASCII hyphen ("-")
        - Preserves punctuation, case, and overall readability
        """        
        text = self._normalize_unicode(text)
        text = self.normalize_whitespace(text, keep_space=True)
        text = self._normalize_symbols(text)
        text = self._normalize_dashes(text, substitute="-")
        return text.strip()

    def normalize_whitespace(self, text: str, keep_space: bool = True) -> str:
        """
        collapse all whitespace (space, tab, newline, etc.) to a single space
        """
        text = self._remove_invisible_chars(text)
        if keep_space:
            text = self.regex.sub(r'\s+', " ", text)
        else:
            text = self.regex.sub(r'\s+', "", text)
        return text.strip()

    def _normalize_dashes(self, text: str, substitute: str = "-") -> str:
        """
        Replaces all dash and underscore chars with substitute value.
        """
        dash_chars = "‐-‒–—―−_"
        return self.regex.sub(f"[{dash_chars}]", substitute, text)

    def _remove_invisible_chars(self, text: str) -> str:
        return self.regex.sub(r"[\u00A0\u2000-\u200D\u2028\u2029\u2060\uFEFF]+", " ", text)

    def _normalize_symbols(self, text: str) -> str:
        """Normalizes symbols, except hyphen/dash type symbols are handled in _normalize_dashes"""
        replacements = {
            "“": '"', "”": '"', "„": '"',
            "‘": "'", "’": "'", "‚": "'",
            "′": "'", "″": '"',
            "…": "...",
            "•": "-",
        }
        for k, v in replacements.items():
            text = text.replace(k, v)
        text = self.regex.sub(r"[\x00-\x08\x0B\x0C\x0E-\x1F]", "", text)
        return text

    def _strip_punctuation(self, text: str) -> str:
        return self.regex.sub(
            pattern=self.regex.common_patterns.PUNCTUATION, 
            repl="", 
            text=text
        ).strip()
    
    def _normalize_unicode(self, text: str) -> str:
        """
        Converts text to Unicode NFKC form.

        This standardizes visually identical characters:
        - Full-width → ASCII (ｅ → e)
        - Ligatures and symbols → decomposed forms (ﬁ → fi, ① → 1)
        - Normalizes diacritics and compatibility forms

        Does NOT remove invisible or space-like characters
        (those are handled by _remove_invisible_chars).
        """
        return unicodedata.normalize("NFKC", text)
