from dataclasses import dataclass, field
from decimal import Decimal

from domain.entities.invoice.item import InvoiceItem

from domain.entities.invoice.invoice import Invoice
from domain.entities.stock_batch import StockBatch
from domain.exceptions.invoice.exceptions import (
    AnonymousLargeInvoiceError,
    EmptyInvoiceFinalizationError,
)
from domain.shared.value_objects import Money


@dataclass(slots=True, kw_only=True)
class DraftInvoice:
    customer_name: str | None = None
    _items: list[InvoiceItem] = field(default_factory=list, init=False)

    def add_item(self, batch: StockBatch, quantity: int) -> None:
        item = InvoiceItem(
            product_id=batch.product_id,
            stock_batch_id=batch.id,
            num_of_items=quantity,
            price_of_item=batch.item_price,
        )
        self._items.append(item)

    def remove_item(self, product_id: str) -> None:
        self._items = [item for item in self._items if item.product_id != product_id]

    @property
    def current_total(self) -> Money:
        return sum(
            (item.price for item in self._items), start=Money(amount=Decimal("0.0"))
        )

    def finalize(self, anonymous_limit: Money) -> Invoice:
        if not self._items:
            raise EmptyInvoiceFinalizationError()

        if (
            self.customer_id is None
            and self.current_total.amount >= anonymous_limit.amount
        ):
            raise AnonymousLargeInvoiceError(
                limit=float(anonymous_limit.amount),
                actual_total=float(self.current_total.amount),
            )

        return Invoice(customer_id=self.customer_id, items=tuple(self._items))
