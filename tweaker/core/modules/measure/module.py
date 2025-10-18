from decimal import Decimal
from ...base_module import BaseModule


class MeasurementModule(BaseModule):
    """
    Converts numeric values between compatible measurement units.
    Supports weight, volume, and distance conversions.
    """

    # Each category defines its base reference unit.
    CATEGORIES = {
        "weight": {
            "g": Decimal("1"),
            "mg": Decimal("0.001"),
            "kg": Decimal("1000"),
            "oz": Decimal("28.3495"),
            "lb": Decimal("453.592"),
        },
        "volume": {
            "ml": Decimal("1"),
            "l": Decimal("1000"),
            "fl_oz": Decimal("29.5735"),
            "tsp": Decimal("4.92892"),
            "tbsp": Decimal("14.7868"),
            "cup": Decimal("236.588"),
            "pt": Decimal("473.176"),
            "qt": Decimal("946.353"),
            "gal": Decimal("3785.41"),
        },
        "distance": {
            "mm": Decimal("1"),
            "cm": Decimal("10"),
            "m": Decimal("1000"),
            "km": Decimal("1000000"),
            "in": Decimal("25.4"),
            "ft": Decimal("304.8"),
            "yd": Decimal("914.4"),
            "mi": Decimal("1609344"),
        },
    }

    def convert(
        self,
        value: Decimal | float | int,
        from_unit: str,
        to_unit: str,
    ) -> Decimal | None:
        """
        Convert a numeric value from one unit to another.
        Returns a Decimal representing the converted value.
        Returns None if units are incompatible or unsupported.
        """
        if value is None or not from_unit or not to_unit:
            return None

        from_unit = from_unit.lower().strip()
        to_unit = to_unit.lower().strip()

        category = self._find_category(from_unit)
        if not category or to_unit not in self.CATEGORIES[category]:
            return None  # incompatible or unsupported conversion

        base_table = self.CATEGORIES[category]
        base_value = Decimal(value) * base_table[from_unit]  # to base unit
        converted = base_value / base_table[to_unit]
        return converted

    def _find_category(self, unit: str) -> str | None:
        """Determine which category (weight, volume, distance) a unit belongs to."""
        for category, table in self.CATEGORIES.items():
            if unit in table:
                return category
        return None
