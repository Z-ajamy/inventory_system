from dataclasses import dataclass, field
from domain.shared.base import Product, Brand
from domain.shared.base import Info


@dataclass(slots=True, frozen=True, kw_only=True)
class NoteBookType(Info):
    pass

@dataclass(slots=True, frozen=True, kw_only=True)
class NoteBook(Product):
    page_numbers: int
    type_id: str
    #Publisher is the Brand
