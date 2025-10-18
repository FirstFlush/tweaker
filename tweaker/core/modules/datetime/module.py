import dateparser
from datetime import datetime
from ...base_module import BaseModule
from .time_mapping import TimeMapping
from ..text.module import TextNormalizer


class DateTimeUtil(BaseModule):
    """
    Parses datetimes from natural language text.
    Uses dateparser first, then falls back to contextual clues like
    clock times, AM/PM markers, or time-of-day keywords (e.g. 'noon', 'evening').
    """

    time_mapping = TimeMapping

    def __init__(self, normalizer: TextNormalizer):
        self.normalizer = normalizer

    def parse(self, text: str) -> datetime | None:
        """
        Attempt to parse a datetime from text.
        Falls back to contextual inference if dateparser fails.
        """
        dt = dateparser.parse(text)
        if dt:
            return dt

        normalized = self.normalizer.normalize(text)
        return self.dt_from_context(normalized)

    def dt_from_context(self, text: str) -> datetime | None:
        """
        Infer a datetime from fuzzy or incomplete text using mapping rules.
        Handles cases like '5 tonight', 'at noon', or 'tomorrow morning'.
        """
        # Try to match an explicit clock time (e.g. "5", "7:30", "five o’clock")
        match = self._match_clock_time(text)
        if match:
            base_time, match_string = match
            meridian = self._resolve_meridian(text, match_string)
            time_str = f"{base_time} {meridian}" if meridian else base_time
        else:
            # Otherwise look for keyword-only times like "noon" or "evening"
            normalized = self.normalizer.normalize(text, keep_whitespace=True)
            time_str = self._match_time_keyword(normalized)

        return dateparser.parse(time_str) if time_str else None

    def _resolve_meridian(self, text: str, time_str: str) -> str | None:
        """Determine AM/PM either from suffix ('5pm') or context ('tonight')."""
        meridian = self._extract_meridian_suffix(text, time_str)
        if not meridian:
            meridian = self._infer_meridian_from_context(text)
        return meridian

    def _match_clock_time(self, text: str) -> tuple[str, str] | None:
        """Check if text contains a recognized clock time."""
        return self.time_mapping.get_key_with_match(
            text=text,
            mapping=self.time_mapping.CLOCK_TIMES,
        )

    def _match_time_keyword(self, text: str) -> str | None:
        """Match time-related keywords like 'noon', 'midnight', 'morning'."""
        return self.time_mapping.get_key(
            text=text,
            mapping=self.time_mapping.KEYWORDS,
        )

    def _extract_meridian_suffix(self, text: str, time_str: str) -> str | None:
        """Check if the time substring is followed by an explicit AM/PM suffix."""
        idx = text.find(time_str)
        if idx == -1:
            return None
        suffix = text[idx + len(time_str):].strip().lower()
        if suffix.startswith("am"):
            return "am"
        if suffix.startswith("pm"):
            return "pm"
        return None

    def _infer_meridian_from_context(self, text: str) -> str | None:
        """Infer AM/PM from words like 'morning', 'evening', or 'tonight'."""
        return self.time_mapping.get_key(
            text=text,
            mapping=self.time_mapping.TIME_CONTEXTS,
        )
