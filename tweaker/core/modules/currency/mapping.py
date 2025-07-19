from ...base_module import BaseSubstringMapping
from .enums import Currency

class CurrencyMapping(BaseSubstringMapping):
        
    FREE = {
        0.0 : {"free", "nocost", "gratis", "complimentary"}
    }
    
    CURRENCY_TYPES = {
        Currency.CAD: {
            "cad", "canadian", "canadien", "cdn", "c$", "ca$", "cadollar", "cadollars"
        },
        Currency.USD: {
            "usd", "usdollars", "us$", "u$", "american", "unitedstates", "uscurrency", "usfunds", "dollar", "dollars"
        },
        Currency.GBP: {
            "gbp", "pound", "pounds", "britishpound", "britishpounds", "£", "gb£", "ukpound", "sterling", "quid"
        },
        Currency.EUR: {
            "eur", "euro", "euros", "€", "eu", "eucurrency", "eufunds"
        },
        Currency.BTC: {
            "btc", "bitcoin", "₿", "bit", "satoshi", "sat", "sats"
        },
        Currency.ETH: {
            "eth", "ethereum", "ether",
        },
        Currency.JPY: {
            "jpy", "yen", "¥", "jp¥", "japanese", "japaneseyen"
        },
        Currency.CNY: {
            "cny", "yuan", "renminbi", "rmb", "cn¥", "chineseyuan", "chinesermb"
        },
        Currency.INR: {
            "inr", "rupee", "rupees", "₹", "rs", "indianrupee", "indianrupees"
        },
        Currency.AUD: {
            "aud", "australian", "australiandollar", "aussiedollar", "a$"
        },
        Currency.NZD: {
            "nzd", "kiwidollar", "kiwi", "nz$", "newzealand", "newzealanddollar"
        },
        Currency.CHF: {
            "chf", "swiss", "swissfranc", "fr", "sfr", "swissmoney"
        },
        Currency.ILS: {
            "ils", "shekel", "shekels", "₪", "israelishekel", "nis", "newisraelishekel"
        },
        Currency.MXN: {
            "mxn", "peso", "pesos", "mexicanpeso", "mexicanpesos", "m$", "mx$", "mex$"
        },
        Currency.BRL: {
            "brl", "real", "reais", "brazilianreal", "r$", "br$"
        },
        Currency.ZAR: {
            "zar", "rand", "southafricanrand", "r"
        },
    }
