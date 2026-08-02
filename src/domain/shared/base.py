from dataclasses import InitVar, dataclass, field
from enum import auto

from domain.exceptions.shared import InvalidPriceError, InvalidStringError
from domain.shared.utils import create_uuid4
from domain.shared.value_objects import Money, OldStrEnum


class InfoCategory(OldStrEnum):
    PEN_COLOR = auto()
    PEN_TYPE = auto()
    RULER_TYPE = auto()
    SCHOOLBOOK_SUBJECT = auto()
    SCHOOLBOOK_CLASS = auto()
    BRAND = auto()


@dataclass(slots=True, kw_only=True)
class Info:
    id: str = field(default_factory=create_uuid4)
    category: InfoCategory

    init_name: InitVar[str]
    _name: str = field(init=False)

    def __post_init__(self, init_name: str):
        self.name = init_name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value or not str(value).strip():
            raise InvalidStringError(field_name="name")
        self._name = str(value).strip()


class ProductFamily(OldStrEnum):
    PENS = auto()
    RULERS = auto()
    BOOKS = auto()
    NOTEBOOKS = auto()


@dataclass(slots=True, kw_only=True)
class Brand(Info):
    supported_families: list[ProductFamily]
    category: InfoCategory = field(default=InfoCategory.BRAND, init=False)

    def supports(self, family: ProductFamily) -> bool:
        return family in self.supported_families


@dataclass(slots=True, kw_only=True)
class Product:
    id: str = field(default_factory=create_uuid4)
    type: ProductFamily
    brand_id: str

    init_sku: InitVar[str]
    init_selling_price: InitVar[Money]

    _sku: str = field(init=False)
    _selling_price: Money = field(init=False)

    def __post_init__(self, init_sku: str, init_selling_price: Money):
        self.sku = init_sku
        self.change_price(init_selling_price)

    @property
    def sku(self) -> str:
        return self._sku

    @sku.setter
    def sku(self, value: str):
        if not value or not str(value).strip():
            raise InvalidStringError(field_name="sku")
        self._sku = str(value).strip()

    @property
    def selling_price(self) -> Money:
        return self._selling_price

    def change_price(self, new_price: Money):
        if new_price.amount <= 0:
            raise InvalidPriceError(amount=float(new_price.amount))
        self._selling_price = new_price
