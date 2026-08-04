from typing import Any

from domain.entities.settings import SystemSettings
from tests.fakes.fake_repositories import (
    FakeCustomerRepository,
    FakeInvoiceRepository,
    FakeProductRepository,
    FakeReferenceDataRepository,
    FakeStockBatchRepository,
    FakeSystemSettingsRepository,
)


class FakeUnitOfWork:
    def __init__(self, default_settings: SystemSettings):
        self.customers = FakeCustomerRepository()
        self.invoices = FakeInvoiceRepository()
        self.products = FakeProductRepository()
        self.reference_data = FakeReferenceDataRepository()
        self.settings = FakeSystemSettingsRepository(default_settings)
        self.batches = FakeStockBatchRepository()

        self.committed = False
        self.rolled_back = False

    def __enter__(self) -> "FakeUnitOfWork":
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if exc_type is not None:
            self.rollback()

    def commit(self) -> None:
        self.committed = True

    def rollback(self) -> None:
        self.rolled_back = True
