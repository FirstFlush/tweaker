currency = [
    "$19.99",                          # simple USD
    "CAD 1,234.56",                    # currency with comma
    "EUR 999",                         # no decimal
    "€1.50",                           # symbol before number
    "Price: $2,499.00",               # text prefix
    "Only 3.14 left in stock!",        # float in text
    "RRP: £79.95",                     # British pound
    "Special deal: 100",              # plain number
    "₩50000",                          # Korean won (no decimal)
    "Amount: 0.99",                    # leading zero
    "$0",                              # zero with currency
    "USD -12.34",                      # negative currency
    "Total: $1,000.00 CAD",           # currency before & after
    "$12.3",                           # single decimal digit
    "Approx. $50",                     # word prefix
    "about 2.5 dollars",              # word suffix
    "1,000,000.00",                    # large number with commas
    "9.8765",                          # >2 decimal places
    "2.00",                            # normalized float
    "-$1,234.56",                      # negative with currency and comma
]

two_numbers = [
    "20 socks for $10.00",
    "Price dropped from $19.99 to $14.99",
    "Bought 2.5kg for 4.75 dollars",
    "Discount: 30% off when you spend 50.00",
    "Earn 3.00 points per $1.00 spent",
    "Was $5.00, now only $3.50",
    "Package weighs 1.25kg and costs $9.99",
    "You saved $12.00 on a $40.00 purchase",
    "Item 1: $7.49, Item 2: $8.99",
    "Between 3.00 and 4.00 liters recommended",
    "Rent: $950.00 + $50.00 utilities",
    "Exchange rate: 1.10 USD = 1.00 EUR",
    "From 0.00 to 100.00 scale",
    "Only 5.5 miles away, ETA: 12.3 minutes",
    "Invoice: subtotal $83.21, tax $4.12",
    "Flight leaves at 14.50, lands at 17.25",
    "Speed ranged between 55.0 and 70.5 mph",
    "Used 1.5GB of 3.0GB data",
    "Refund of $22.00 issued, original $30.00",
    "2.99 each or 2 for 5.00",
]

invalid_floats = [
    "The IP is 192.168.1.1",
    "Running version 3.10.6 now",
    "Paid 20.42.2 dollars",                # too many decimals
    "Just one: 12.34.56",                  # same deal
    "Error code: 404.500.600",
    "Use regex101.com",                    # domain
    "Balance: 1,000.00.00",                # malformed number
    "v2.0.0 released yesterday",
    "Decimal overload: .12.34",
    "That's a 1..5 ratio",                 # double dots
    "Range: 10,000..20,000",               # double dot again
    "Cost: 12.00$",                        # trailing $ is nonstandard
    "Input: ..50",                         # leading double dot
    "Timecode: 01:23:45.67",               # timestamp
    "Coordinates: 49.2827° N, 123.1207° W", # lat/lon
    "Phone: (123) 456-7890",
    "Order #: 1000-2000-3000",
    "Build: r1.0.0-beta",                 # semver again
    "Mix: 3.5.7.9 for best results",
    "Weird: 0..1"
]