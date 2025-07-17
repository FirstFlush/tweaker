
from ...base_module import BaseModule
from .municipalities import MunicipalityBC
from .provinces import ProvinceAbbreviation, ProvinceName


class RegionMatcher(BaseModule):
    
    municipalities = MunicipalityBC
    provinces = ProvinceName
    provinces_abbreviated = ProvinceAbbreviation
    
    def get_municipality(self, text: str) -> MunicipalityBC | None:
        normalized = self.tweaker.text.normalize(text)
        return self.tweaker.enum.match_by_normalized_value(
            enum_cls=self.municipalities,
            text=normalized,
        )
    
    def get_province(self, text: str, abbreviation: bool = False) -> ProvinceName | ProvinceAbbreviation | None:
        normalized = self.tweaker.text.normalize(text)
        enum_cls = ProvinceAbbreviation if abbreviation else ProvinceName
        return self.tweaker.enum.match_by_normalized_value(
            enum_cls=enum_cls,
            text=normalized,
        )