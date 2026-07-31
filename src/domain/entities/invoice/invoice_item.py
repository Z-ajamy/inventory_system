from dataclasses import dataclass, field

from domain.exceptions.invoice.exceptions import InvalidInvoiceItemQuantityError
from domain.shared.utils import create_uuid4
from domain.shared.value_objects import Money


@dataclass(slots=True, frozen=True, kw_only=True)
class InvoiceItem:
    id: str = field(default_factory=create_uuid4)
    product_id: str
    stock_batch_id: str
    num_of_items: int
    price_of_item: Money

    def __post_init__(self):
        if self.num_of_items <= 0:
            raise InvalidInvoiceItemQuantityError(quantity=self.num_of_items)

    @property
    def price(self) -> Money:
        return self.price_of_item * self.num_of_items
