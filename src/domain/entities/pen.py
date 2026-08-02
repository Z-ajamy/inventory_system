from dataclasses import InitVar, dataclass, field

from domain.exceptions.shared import InvalidStringError
from domain.shared.base import Info, InfoCategory, Product, ProductFamily
from domain.shared.value_objects import Money


@dataclass(slots=True, kw_only=True)
class PenColor(Info):
    category: InfoCategory = field(default=InfoCategory.PEN_COLOR, init=False)


@dataclass(slots=True, kw_only=True)
class PenType(Info):
    category: InfoCategory = field(default=InfoCategory.PEN_TYPE, init=False)


@dataclass(slots=True, kw_only=True)
class PenProduct(Product):
    type: ProductFamily = field(default=ProductFamily.PENS, init=False)

    init_color_id: InitVar[str]
    init_pen_type_id: InitVar[str]

    _color_id: str = field(init=False)
    _pen_type_id: str = field(init=False)

    def __post_init__(
        self,
        init_sku: str,
        init_selling_price: Money,
        init_color_id: str,
        init_pen_type_id: str,
    ):
        Product.__post_init__(self, init_sku, init_selling_price)

        self.color_id = init_color_id
        self.pen_type_id = init_pen_type_id

    @property
    def color_id(self) -> str:
        return self._color_id

    @color_id.setter
    def color_id(self, value: str):
        if not value or not str(value).strip():
            raise InvalidStringError(field_name="color_id")
        self._color_id = str(value).strip()

    @property
    def pen_type_id(self) -> str:
        return self._pen_type_id

    @pen_type_id.setter
    def pen_type_id(self, value: str):
        if not value or not str(value).strip():
            raise InvalidStringError(field_name="pen_type_id")
        self._pen_type_id = str(value).strip()
