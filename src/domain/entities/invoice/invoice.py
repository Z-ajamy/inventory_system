from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal

from domain.entities.invoice.invoice_item import InvoiceItem
from domain.shared.utils import create_uuid4
from domain.shared.value_objects import Money


@dataclass(slots=True, frozen=True, kw_only=True)
class Invoice:
    id: str = field(default_factory=create_uuid4)
    customer_id: str | None  # تم التغيير إلى customer_id
    items: tuple[InvoiceItem, ...]
    date: datetime = field(default_factory=datetime.now)

    @property
    def total_price(self) -> Money:
        return sum(
            (item.price for item in self.items), start=Money(amount=Decimal("0.0"))
        )

    @property
    def items_count(self) -> int:
        return len(self.items)
