from dataclasses import dataclass, field
from datetime import datetime

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

    def sell_items(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Amount must be positive")
        elif amount > self.current_quantity:
            raise ValueError("Insufficient quantity in this batch")

        self.current_quantity -= amount


