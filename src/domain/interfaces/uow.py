from typing import Any, Protocol

from domain.interfaces.customer_repository import CustomerRepositoryProtocol
from domain.interfaces.invoice_repository import InvoiceRepositoryProtocol
from domain.interfaces.product_repository import ProductRepositoryProtocol
from domain.interfaces.reference_repository import ReferenceDataRepositoryProtocol
from domain.interfaces.settings_repository import SystemSettingsRepositoryProtocol
from domain.interfaces.stock_batch_repository import StockBatchRepositoryProtocol


class UnitOfWorkProtocol(Protocol):
    customers: CustomerRepositoryProtocol
    invoices: InvoiceRepositoryProtocol
    products: ProductRepositoryProtocol
    reference_data: ReferenceDataRepositoryProtocol
    settings: SystemSettingsRepositoryProtocol
    batches: StockBatchRepositoryProtocol

    def __enter__(self) -> "UnitOfWorkProtocol": ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...

    def commit(self) -> None: ...

    def rollback(self) -> None: ...
