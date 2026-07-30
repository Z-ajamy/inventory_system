from dataclasses import dataclass

from domain.shared.base import Info, Product


@dataclass(slots=True, frozen=True, kw_only=True)
class PenColor(Info):
    pass


@dataclass(slots=True, frozen=True, kw_only=True)
class PenType(Info):
    pass


@dataclass(slots=True, frozen=True, kw_only=True)
class PenProduct(Product):
    color_id: str
    pen_type_id: str
