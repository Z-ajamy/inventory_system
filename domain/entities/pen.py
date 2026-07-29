from dataclasses import dataclass, field
from domain.shared.base import Product
from domain.shared.base import Info

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
