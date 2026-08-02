from dataclasses import dataclass


@dataclass(slots=True, frozen=True, kw_only=True)
class InvoiceItemDTO:
    product_id: str
    num_of_items: int


@dataclass(slots=True, frozen=True, kw_only=True)
class CreateInvoiceRequestDTO:
    customer_id: str | None
    invoice_items: tuple[InvoiceItemDTO, ...]
