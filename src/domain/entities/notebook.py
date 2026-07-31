from dataclasses import dataclass, field

from domain.exceptions.notebook import InvalidPageCountError
from domain.shared.base import Product, ProductFamily


@dataclass(slots=True, frozen=True, kw_only=True)
class NoteBook(Product):
    type: ProductFamily = field(default=ProductFamily.NOTEBOOKS, init=False)
    page_count: int
    type_id: str

    def __post_init__(self):
        if self.page_count <= 0:
            raise InvalidPageCountError(page_count=self.page_count)
