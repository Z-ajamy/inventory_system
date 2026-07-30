from dataclasses import dataclass, field
from datetime import datetime

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
    product_id: str
    init_quantity: int
    current_quantity: int
    unit_cost: Money
    item_price: Money
    received_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        if self.init_quantity < 0 or self.current_quantity < 0:
            raise InvalidBatchQuantityError(
                quantity=min(self.init_quantity, self.current_quantity)
            )

    def sell_items(self, amount: int) -> None:
        if amount < 0:
            raise NegativeSellAmountError(amount=amount)
        elif amount > self.current_quantity:
            raise InsufficientStockError(
                requested=amount, available=self.current_quantity
            )

        self.current_quantity -= amount

    def change_price(self, price: Money):
        self.item_price = price
