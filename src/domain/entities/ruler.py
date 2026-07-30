from dataclasses import dataclass

from domain.shared.base import Info, Product
from domain.exceptions.ruler import InvalidRulerLengthError

@dataclass(slots=True, frozen=True, kw_only=True)
class RulerType(Info):
    pass ## لتحديد نوع المسطرة - دراسية او هندسة وهكذا

@dataclass(slots=True, frozen=True, kw_only=True)
class RulerProduct(Product):
    ruler_type_id: str
    length_cm: int
    
    def __post_init__(self):
        if self.length_cm <= 0:
            raise InvalidRulerLengthError(length_cm=self.length_cm)
    
    