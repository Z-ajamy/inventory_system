from datetime import datetime

from domain.entities.customer import Customer
from domain.entities.invoice.invoice import Invoice
from domain.entities.settings import SystemSettings
from domain.entities.stock_batch import StockBatch
from domain.shared.base import Info, InfoCategory, Product, ProductFamily


class FakeCustomerRepository:
    def __init__(self):
        self._data: dict[str, Customer] = {}

    def save(self, customer: Customer) -> None:
        self._data[customer.id] = customer

    def get_by_id(self, customer_id: str) -> Customer | None:
        return self._data.get(customer_id)

    def get_by_name(self, name: str) -> tuple[Customer, ...]:
        return tuple(c for c in self._data.values() if c.name == name)


class FakeReferenceDataRepository:
    def __init__(self):
        self._data: dict[str, Info] = {}

    def save(self, info: Info) -> None:
        self._data[info.id] = info

    def get_by_id(self, info_id: str) -> Info | None:
        return self._data.get(info_id)

    def get_by_category(self, category: InfoCategory) -> tuple[Info, ...]:
        return tuple(i for i in self._data.values() if i.category == category)


class FakeProductRepository:
    def __init__(self):
        self._data: dict[str, Product] = {}

    def save(self, product: Product) -> None:
        self._data[product.id] = product

    def get_by_id(self, product_id: str) -> Product | None:
        return self._data.get(product_id)

    def get_by_sku(self, sku: str) -> Product | None:
        for p in self._data.values():
            if p.sku == sku:
                return p
        return None

    def get_by_type(self, type: ProductFamily) -> tuple[Product, ...]:
        return tuple(p for p in self._data.values() if p.type == type)

    def get_by_info_id(self, info_id: str) -> tuple[Product, ...]:
        # تبسيط للـ Fake
        return tuple()

    def get_by_brand_id(self, info_id: str) -> tuple[Product, ...]:
        return tuple(p for p in self._data.values() if p.brand_id == info_id)


class FakeSystemSettingsRepository:
    def __init__(self, default_settings: SystemSettings):
        self._settings = default_settings
        self._data: dict[str, SystemSettings] = {default_settings.id: default_settings}

    def save(self, settings: SystemSettings) -> None:
        self._data[settings.id] = settings
        self._settings = settings

    def get_all(self) -> tuple[SystemSettings, ...]:
        return tuple(self._data.values())

    def get_all_from_date(self, date: datetime) -> tuple[SystemSettings, ...]:
        return tuple(self._data.values())

    def get_current_setting(self) -> SystemSettings:
        return self._settings

    def get_by_id(self, settings_id: str) -> SystemSettings:
        return self._data.get(settings_id, self._settings)


class FakeStockBatchRepository:
    def __init__(self):
        self._data: dict[str, StockBatch] = {}

    def save(self, stock_batch: StockBatch) -> None:
        self._data[stock_batch.id] = stock_batch

    def get_by_id(self, stock_batch_id: str) -> StockBatch | None:
        return self._data.get(stock_batch_id)

    def get_by_product_id(self, product_id: str) -> tuple[StockBatch, ...]:
        return tuple(b for b in self._data.values() if b.product_id == product_id)

    def get_available_for_product(self, product_id: str) -> tuple[StockBatch, ...]:
        available = [
            b
            for b in self._data.values()
            if b.product_id == product_id and b.current_quantity > 0
        ]
        return tuple(sorted(available, key=lambda b: b.received_at))

    def get_total_quantity_for_product(self, product_id: str) -> int:
        return sum(
            b.current_quantity
            for b in self._data.values()
            if b.product_id == product_id
        )

    def get_low_stock(self, threshold_quantity: int) -> tuple[StockBatch, ...]:
        return tuple(
            b for b in self._data.values() if b.current_quantity < threshold_quantity
        )


class FakeInvoiceRepository:
    def __init__(self):
        self._data: dict[str, Invoice] = {}

    def save(self, invoice: Invoice) -> None:
        self._data[invoice.id] = invoice

    def get_by_id(self, invoice_id: str) -> Invoice | None:
        return self._data.get(invoice_id)

    def get_by_customer_id(self, customer_id: str) -> tuple[Invoice, ...]:
        return tuple(i for i in self._data.values() if i.customer_id == customer_id)

    def get_between_dates(
        self, start_date: datetime, end_date: datetime | None = None
    ) -> tuple[Invoice, ...]:
        return tuple(self._data.values())

    def get_by_product_id(self, product_id: str) -> tuple[Invoice, ...]:
        result = []
        for inv in self._data.values():
            for item in inv.items:
                if item.product_id == product_id:
                    result.append(inv)
                    break
        return tuple(result)
