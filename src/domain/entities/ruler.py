from dataclasses import dataclass, field

from domain.exceptions.ruler import InvalidRulerLengthError
from domain.shared.base import Info, Product, ProductFamily


@dataclass(slots=True, frozen=True, kw_only=True)
class RulerType(Info):
    pass


@dataclass(slots=True, frozen=True, kw_only=True)
class RulerProduct(Product):
    type: ProductFamily = field(default=ProductFamily.RULERS, init=False)
    ruler_type_id: str
    length_cm: int

    def __post_init__(self):
        if self.length_cm <= 0:
            raise InvalidRulerLengthError(length_cm=self.length_cm)
