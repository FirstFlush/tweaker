from ...base_module import BaseSubstringMapping


class CurrencyMapping(BaseSubstringMapping):
        
    FREE_WORDS = {
        0.0 : {"free", "nocost", "gratis", "complimentary"}
    }
    
    CURRENCY_TYPES = {
        "cad": {
            "cad", "canadian", "canadien", "cdn", "c$", "ca$", "cadollar", "cadollars"
        },
        "usd": {
            "usd", "usdollars", "us$", "u$", "american", "unitedstates", "uscurrency", "usfunds", "dollar", "dollars"
        },
        "gbp": {
            "gbp", "pound", "pounds", "britishpound", "britishpounds", "£", "gb£", "ukpound", "sterling", "quid"
        },
        "eur": {
            "eur", "euro", "euros", "€", "eu", "eucurrency", "eufunds"
        },
        "btc": {
            "btc", "bitcoin", "₿", "bit", "satoshi", "sat", "sats"
        },
        "eth": {
            "eth", "ethereum", "ether",
        },
        "jpy": {
            "jpy", "yen", "¥", "jp¥", "japanese", "japaneseyen"
        },
        "cny": {
            "cny", "yuan", "renminbi", "rmb", "cn¥", "chineseyuan", "chinesermb"
        },
        "inr": {
            "inr", "rupee", "rupees", "₹", "rs", "indianrupee", "indianrupees"
        },
        "aud": {
            "aud", "australian", "australiandollar", "aussiedollar", "a$"
        },
        "nzd": {
            "nzd", "kiwidollar", "kiwi", "nz$", "newzealand", "newzealanddollar"
        },
        "chf": {
            "chf", "swiss", "swissfranc", "fr", "sfr", "swissmoney"
        },
        "ils": {
            "ils", "shekel", "shekels", "₪", "israelishekel", "nis", "newisraelishekel"
        },
        "mxn": {
            "mxn", "peso", "pesos", "mexicanpeso", "mexicanpesos", "m$", "mx$", "mex$"
        },
        "brl": {
            "brl", "real", "reais", "brazilianreal", "r$", "br$"
        },
        "zar": {
            "zar", "rand", "southafricanrand", "r"
        },
    }
