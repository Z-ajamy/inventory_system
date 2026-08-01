from datetime import datetime
from typing import Protocol

from domain.entities.invoice.invoice import Invoice


class InvoiceRepositoryProtocol(Protocol):
    def save(self, invoice: Invoice) -> None: ...

    def get_by_id(self, invoice_id: str) -> Invoice | None: ...

    def get_by_customer_id(self, customer_id: str) -> tuple[Invoice, ...]: ...

    def get_between_dates(
        self, start_date: datetime, end_date: datetime | None = None
    ) -> tuple[Invoice, ...]: ...

    def get_by_product_id(self, product_id: str) -> tuple[Invoice, ...]: ...
