# tweaker

**tweaker** is a Python toolkit for transforming messy, semi-structured text into clean, structured data.  
It’s built to power the **Transform** stage of an ETL pipeline — not fetching, not storing — just turning input into something usable.

`tweaker` helps you clean up things like currency amounts, dates, contact info, region names, and typed values.  
It’s a utility belt for wrangling messy input and transforming it into structured output.


## 🚧 Development Status

This package is in active development.  
The API is still evolving and may change frequently between versions.


## ⚙️ Usage

Instantiate once and reuse across your pipeline:

```python
from tweaker import Tweaker

t = Tweaker()
```

## 🧩 Module Overview

| Module | Description |
|---------|--------------|
| **RegexUtility** | Core regex patterns and helpers shared across modules. |
| **TextNormalizer** | Normalizes, cleans, and tokenizes text (case folding, punctuation stripping, whitespace cleanup). |
| **TypeCaster** | Converts between basic types (`"yes"` → `True`, `"42"` → `42`, etc.). |
| **FuzzyMatcher** | Lightweight fuzzy matching for approximate text similarity. |
| **ContactExtractor** | Extracts emails, phone numbers, and addresses from arbitrary text. |
| **CurrencyParser** | Detects and parses currency expressions, returning structured `{amount, currency}` data. |
| **DateTimeUtil** | Parses dates, times, and durations into Python datetime objects. |
| **EnumModule** | Tools for safely matching or instantiating Enums by normalized value. |
| **KeywordMatcher** | Flexible keyword search with token or substring matching modes. |
| **MeasurementModule** | Parses and converts weights, volumes, and lengths into consistent numeric units. |


## 📄 License

Licensed under the [MIT License](LICENSE).


## ☕ Support This Project

If this saved you time or made your life easier, feel free to [buy me a coffee](https://www.buymeacoffee.com/firstflush). Thanks for your support
