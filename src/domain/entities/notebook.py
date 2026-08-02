from dataclasses import InitVar, dataclass, field

from domain.exceptions.notebook import InvalidPageCountError
from domain.exceptions.shared import InvalidStringError
from domain.shared.base import Product, ProductFamily
from domain.shared.value_objects import Money


@dataclass(slots=True, kw_only=True)
class NoteBook(Product):
    type: ProductFamily = field(default=ProductFamily.NOTEBOOKS, init=False)

    init_page_count: InitVar[int]
    init_type_id: InitVar[str]

    _page_count: int = field(init=False)
    _type_id: str = field(init=False)

    def __post_init__(
        self,
        init_sku: str,
        init_selling_price: Money,
        init_page_count: int,
        init_type_id: str,
    ):
        Product.__post_init__(self, init_sku, init_selling_price)

        self.page_count = init_page_count
        self.type_id = init_type_id

    @property
    def page_count(self) -> int:
        return self._page_count

    @page_count.setter
    def page_count(self, value: int):
        if value <= 0:
            raise InvalidPageCountError(page_count=value)
        self._page_count = value

    @property
    def type_id(self) -> str:
        return self._type_id

    @type_id.setter
    def type_id(self, value: str):
        if not value or not str(value).strip():
            raise InvalidStringError(field_name="type_id")
        self._type_id = str(value).strip()
