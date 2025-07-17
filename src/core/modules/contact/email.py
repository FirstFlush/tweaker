from ...base_module import BaseModule
from email_validator import validate_email, EmailNotValidError
import re


class EmailSniffer(BaseModule):

    def _extract_raw(self, text: str) -> list[str]:
        return self.tweaker.regex.find_all(
            pattern=self.tweaker.regex.common_patterns.EMAIL,
            text=text,
            flags=re.IGNORECASE,
        )

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
    
    def extract_email(self, text: str) -> str | None:
        for email in self._extract_raw(text):
            try:
                v = validate_email(email, check_deliverability=False)
                return v.email
            except EmailNotValidError:
                continue
        return None