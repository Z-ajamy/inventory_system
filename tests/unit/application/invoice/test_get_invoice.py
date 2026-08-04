from decimal import Decimal

import pytest

from application.exceptions.get_invoice import InvoiceNotFoundError
from application.invoice.get_invoice import GetInvoiceUseCase
from domain.entities.invoice.invoice import Invoice
from domain.entities.invoice.invoice_item import InvoiceItem
from domain.shared.value_objects import Money
from tests.fakes.fake_uow import FakeUnitOfWork


def test_get_invoice_success(fake_uow: FakeUnitOfWork):
    item = InvoiceItem(
        product_id="prod-1",
        stock_batch_id="batch-1",
        num_of_items=2,
        price_of_item=Money(amount=Decimal("50.0")),
    )
    invoice = Invoice(customer_id="cust-1", items=(item,))
    fake_uow.invoices.save(invoice)

    use_case = GetInvoiceUseCase(uow=fake_uow)

    result = use_case.execute(invoice_id=invoice.id)

    assert result.id == invoice.id
    assert result.customer_id == "cust-1"
    assert result.total_price.amount == Decimal("100.0")
    assert len(result.items) == 1
    assert result.items[0].product_id == "prod-1"


def test_get_invoice_raises_not_found(fake_uow: FakeUnitOfWork):
    use_case = GetInvoiceUseCase(uow=fake_uow)

    with pytest.raises(InvoiceNotFoundError):
        use_case.execute(invoice_id="invalid-id")
