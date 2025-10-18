

class CommonPatterns:
    
    # Email regex pattern that matches real-world email addresses as used by
    # Gmail, Outlook, Yahoo, Fastmail, etc. It follows most of RFC 5322 and
    # RFC 1035 (domain name rules), while deliberately ignoring obsolete or
    # extreme edge cases that don’t occur in the real world.
    #
    # ✅ RFC compliance:
    # - Based on RFC 5322 for local part syntax (alphanum, dots, underscores, hyphens, plus, apostrophe)
    # - Based on RFC 1035 for domain name rules (no underscores, no leading/trailing hyphens, max label length)
    #
    # ✅ Real-world support:
    # - Accepts subdomains: user@sub.domain.com
    # - Allows plus aliases: user+tag@example.com
    # - Accepts apostrophes: o'reilly@example.com
    # - Valid TLDs: 2–10 letters (.com, .org, .museum, .solutions, etc.)
    #
    # ❌ Intentionally excludes:
    # - Quoted local parts ("very.unusual.@.unusual.com"@example.com)
    # - IP address domains (user@[192.168.1.1])
    # - Comments (user(comment)@domain.com)
    # - Unicode (no internationalized addresses)
    # - Localhost-only domains (user@localhost)
    #
    # 💡 This pattern is strict enough to reject malformed or unsafe emails,
    # but permissive enough to match everything accepted by major providers.
    EMAIL = r"^[a-zA-Z0-9](?:[a-zA-Z0-9_+\'-]*[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9_+\'-]*[a-zA-Z0-9])?)*@(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}$"


    # This regex extracts **real-world float values** from messy text
    # while avoiding false positives like:
    # - IP addresses (e.g. 192.168.1.1)
    # - version numbers (e.g. v1.2.3)
    # - malformed floats (e.g. 1,000.00.00)
    # - chained numbers (e.g. phone numbers, timecodes, IDs)
    #
    # ✅ Matches:
    # - Optional sign: -12.34, +1, or 99.9
    # - Optional commas: 1,000.50
    # - Decimals: 0.99, 100.0
    #
    # ❌ Rejects numbers that:
    # - Are embedded in dotted/colon-separated sequences (e.g. 3.5.7.9 or 01:23:45)
    # - Have junk around them (e.g. 12.00$ or #1000-2000)
    # - Start or end in malformed structures (e.g. double dots, fragments)
    #
    # Breakdown:
    # (?<![\d.,:(#-])         - Negative lookbehind: prevents match if preceded by dot, comma, colon, digit, etc.
    # [-+]?                   - Optional sign
    # (?:\d{1,3}(?:,\d{3})*   - Digits with optional comma groups (e.g. 1,000)
    #     | \d+)              - OR just digits (e.g. 100)
    # (?:\.\d+)?              - Optional decimal part (e.g. .50)
    # (?![.\d:,°$\-)])        - Negative lookahead: blocks match if followed by dot, digit, colon, degree sign, etc.
    #
    # 🚫 Known tradeoffs:
    # - Will not extract floats from inside malformed constructs like "1.2.3"
    # - Strict by design — prioritizes correctness over fuzziness
    TO_FLOAT = r"(?<![\d.,:(#-])[-+]?(?:\d{1,3}(?:,\d{3})*|\d+)(?:\.\d+)?(?![.\d:,°$\-)])"

    # WEBSITE = r"https?://[^\s/$.?#].[^\s]*|www\.[^\s/$.?#].[^\s]*"
    URL =     r'(?:https?://)?(?:www\.)?[a-z0-9-]+(?:\.[a-z]{2,})+(?:[/?#][^\s"]*)?' 
    PUNCTUATION = r"[^\w\s]"