from dataclasses import InitVar, dataclass, field

from domain.exceptions.ruler import InvalidRulerLengthError
from domain.exceptions.shared import InvalidStringError
from domain.shared.base import Info, InfoCategory, Product, ProductFamily
from domain.shared.value_objects import Money


@dataclass(slots=True, kw_only=True)
class RulerType(Info):
    category: InfoCategory = field(default=InfoCategory.RULER_TYPE, init=False)


@dataclass(slots=True, kw_only=True)
class RulerProduct(Product):
    type: ProductFamily = field(default=ProductFamily.RULERS, init=False)

    init_ruler_type_id: InitVar[str]
    init_length_cm: InitVar[int]

    _ruler_type_id: str = field(init=False)
    _length_cm: int = field(init=False)

    def __post_init__(
        self,
        init_sku: str,
        init_selling_price: Money,
        init_ruler_type_id: str,
        init_length_cm: int,
    ):
        Product.__post_init__(self, init_sku, init_selling_price)

        self.ruler_type_id = init_ruler_type_id
        self.length_cm = init_length_cm

    @property
    def ruler_type_id(self) -> str:
        return self._ruler_type_id

    @ruler_type_id.setter
    def ruler_type_id(self, value: str):
        if not value or not str(value).strip():
            raise InvalidStringError(field_name="ruler_type_id")
        self._ruler_type_id = str(value).strip()

    @property
    def length_cm(self) -> int:
        return self._length_cm

    @length_cm.setter
    def length_cm(self, value: int):
        if value <= 0:
            raise InvalidRulerLengthError(length_cm=value)
        self._length_cm = value
