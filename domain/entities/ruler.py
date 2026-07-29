from dataclasses import dataclass

from domain.shared.base import Info, Product


@dataclass(slots=True, frozen=True, kw_only=True)
class RulerType(Info):
    pass


@dataclass(slots=True, frozen=True, kw_only=True)
class RulerProduct(Product):
    ruler_type_id: str
    length_cm: int


