from dataclasses import dataclass, field

from domain.shared.base import Info, InfoCategory, Product, ProductFamily


@dataclass(slots=True, frozen=True, kw_only=True)
class PenColor(Info):
    category: InfoCategory = field(default=InfoCategory.PEN_COLOR, init=False)


@dataclass(slots=True, frozen=True, kw_only=True)
class PenType(Info):
    category: InfoCategory = field(default=InfoCategory.PEN_TYPE, init=False)


@dataclass(slots=True, frozen=True, kw_only=True)
class PenProduct(Product):
    type: ProductFamily = field(default=ProductFamily.PENS, init=False)
    color_id: str
    pen_type_id: str
