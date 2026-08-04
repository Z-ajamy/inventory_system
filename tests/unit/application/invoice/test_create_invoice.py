from decimal import Decimal

import pytest

from application.exceptions.create_invoice import (
    ProductNotFoundError,
    QuantityIsLessThanOrderError,
)
from application.invoice.create_invoice import CreateInvoiceUseCase
from application.invoice.dtos import CreateInvoiceRequestDTO, InvoiceItemDTO
from domain.entities.stock_batch import StockBatch
from domain.shared.base import Product, ProductFamily
from domain.shared.value_objects import Money
from tests.fakes.fake_uow import FakeUnitOfWork


def test_create_invoice_success_fifo_logic(fake_uow: FakeUnitOfWork):
    product = Product(
        type=ProductFamily.PENS,
        brand_id="brand-1",
        init_sku="PEN-01",
        init_selling_price=Money(amount=Decimal("15.0")),
    )
    fake_uow.products.save(product)

    batch_old = StockBatch(
        init_product_id=product.id,
        init_init_quantity=2,
        init_current_quantity=2,
        unit_cost=Money(amount=Decimal("10.0")),
    )
    batch_old.received_at = batch_old.received_at.replace(year=2020)  # نجعله قديماً

    batch_new = StockBatch(
        init_product_id=product.id,
        init_init_quantity=10,
        init_current_quantity=10,
        unit_cost=Money(amount=Decimal("12.0")),
    )

    fake_uow.batches.save(batch_old)
    fake_uow.batches.save(batch_new)

    request = CreateInvoiceRequestDTO(
        customer_id="cust-1",
        invoice_items=(InvoiceItemDTO(product_id=product.id, num_of_items=5),),
    )

    use_case = CreateInvoiceUseCase(uow=fake_uow)
    invoice_id = use_case.execute(request)

    assert fake_uow.committed is True

    saved_invoice = fake_uow.invoices.get_by_id(invoice_id)
    assert saved_invoice is not None
    assert saved_invoice.items_count == 2

    assert batch_old.current_quantity == 0
    assert batch_new.current_quantity == 7


def test_create_invoice_raises_product_not_found(fake_uow: FakeUnitOfWork):
    request = CreateInvoiceRequestDTO(
        customer_id="cust-1",
        invoice_items=(InvoiceItemDTO(product_id="invalid-id", num_of_items=1),),
    )
    use_case = CreateInvoiceUseCase(uow=fake_uow)

    with pytest.raises(ProductNotFoundError):
        use_case.execute(request)


def test_create_invoice_raises_insufficient_quantity(fake_uow: FakeUnitOfWork):
    product = Product(
        type=ProductFamily.PENS,
        brand_id="brand-1",
        init_sku="PEN-01",
        init_selling_price=Money(amount=Decimal("15.0")),
    )
    fake_uow.products.save(product)

    batch = StockBatch(
        init_product_id=product.id,
        init_init_quantity=1,
        init_current_quantity=1,
        unit_cost=Money(amount=Decimal("10.0")),
    )
    fake_uow.batches.save(batch)

    request = CreateInvoiceRequestDTO(
        customer_id="cust-1",
        invoice_items=(InvoiceItemDTO(product_id=product.id, num_of_items=10),),
    )
    use_case = CreateInvoiceUseCase(uow=fake_uow)

    with pytest.raises(QuantityIsLessThanOrderError):
        use_case.execute(request)
