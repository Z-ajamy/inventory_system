from dataclasses import dataclass

from domain.shared.base import Product
from domain.exceptions.notebook import InvalidPageCountError

@dataclass(slots=True, frozen=True, kw_only=True)
class NoteBook(Product):
    page_count: int
    type_id: str

    def __post_init__(self):
        if self.page_count <= 0:
            raise InvalidPageCountError(page_count=self.page_count)
