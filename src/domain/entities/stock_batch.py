from dataclasses import InitVar, dataclass, field
from datetime import datetime

from domain.exceptions.shared import InvalidStringError
from domain.exceptions.stock_batch import (
    InsufficientStockError,
    InvalidBatchQuantityError,
    NegativeSellAmountError,
)
from domain.shared.utils import create_uuid4
from domain.shared.value_objects import Money


@dataclass(slots=True, kw_only=True)
class StockBatch:
    id: str = field(default_factory=create_uuid4)
    unit_cost: Money
    received_at: datetime = field(default_factory=datetime.now)

    init_product_id: InitVar[str]
    init_init_quantity: InitVar[int]
    init_current_quantity: InitVar[int]

    _product_id: str = field(init=False)
    _init_quantity: int = field(init=False)
    _current_quantity: int = field(init=False)

    def __post_init__(
        self, init_product_id: str, init_init_quantity: int, init_current_quantity: int
    ):
        self.product_id = init_product_id
        self.init_quantity = init_init_quantity
        self.current_quantity = init_current_quantity

    @property
    def product_id(self) -> str:
        return self._product_id

    @product_id.setter
    def product_id(self, value: str):
        if not value or not str(value).strip():
            raise InvalidStringError(field_name="product_id")
        self._product_id = str(value).strip()

    @property
    def init_quantity(self) -> int:
        return self._init_quantity

    @init_quantity.setter
    def init_quantity(self, value: int):
        if value < 0:
            raise InvalidBatchQuantityError(quantity=value)
        self._init_quantity = value

    @property
    def current_quantity(self) -> int:
        return self._current_quantity

    @current_quantity.setter
    def current_quantity(self, value: int):
        if value < 0:
            raise InvalidBatchQuantityError(quantity=value)
        self._current_quantity = value

    def sell_items(self, amount: int) -> None:
        if amount < 0:
            raise NegativeSellAmountError(amount=amount)
        elif amount > self._current_quantity:
            raise InsufficientStockError(
                requested=amount, available=self._current_quantity
            )

        self.current_quantity = self._current_quantity - amount
