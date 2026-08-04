from dataclasses import dataclass
from datetime import datetime

from domain.shared.value_objects import Money


@dataclass(slots=True, frozen=True, kw_only=True)
class InvoiceItemDTO:
    product_id: str
    num_of_items: int


@dataclass(slots=True, frozen=True, kw_only=True)
class CreateInvoiceRequestDTO:
    customer_id: str | None
    invoice_items: tuple[InvoiceItemDTO, ...]


@dataclass(slots=True, frozen=True, kw_only=True)
class InvoiceItemResponseDTO:
    product_id: str
    num_of_items: int
    total_price: Money


@dataclass(slots=True, frozen=True, kw_only=True)
class InvoiceResponseDTO:
    id: str
    customer_id: str | None
    items: tuple[InvoiceItemResponseDTO, ...]
    date: datetime
    total_price: Money
    items_count: int
