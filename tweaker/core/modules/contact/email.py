from ...base_module import BaseModule
from ..regex.module import RegexUtility
from email_validator import validate_email, EmailNotValidError
import re


class EmailExtractor(BaseModule):
    """
    Extracts and validates email addresses from arbitrary text using regex and email-validator.
    Filters out invalid patterns and returns normalized addresses from full paragraphs or mixed content.
    """

    def __init__(self, regex: RegexUtility):
        self.regex = regex
    
    def extract_email(self, text: str) -> str | None:
        for email in self._extract_raw(text):
            try:
                v = validate_email(email, check_deliverability=False)
                return v.email
            except EmailNotValidError:
                continue
        return None

    def extract_emails(self, text: str) -> list[str]:
        raw = self._extract_raw(text)
        valid = []

        for email in raw:
            try:
                v = validate_email(email, check_deliverability=False)
                valid.append(v.email)
            except EmailNotValidError:
                continue

        return valid

    def _extract_raw(self, text: str) -> list[str]:
        return self.regex.find_all(
            pattern=self.regex.common_patterns.EMAIL,
            text=text,
            flags=re.IGNORECASE,
        )