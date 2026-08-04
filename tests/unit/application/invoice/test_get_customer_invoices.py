from decimal import Decimal

from application.invoice.get_customer_invoices import GetCustomerInvoicesUseCase
from domain.entities.invoice.invoice import Invoice
from domain.entities.invoice.invoice_item import InvoiceItem
from domain.shared.value_objects import Money
from tests.fakes.fake_uow import FakeUnitOfWork


def test_get_customer_invoices_success(fake_uow: FakeUnitOfWork):
    item = InvoiceItem(
        product_id="prod-1",
        stock_batch_id="batch-1",
        num_of_items=1,
        price_of_item=Money(amount=Decimal("10.0")),
    )

    invoice_1 = Invoice(customer_id="target-customer", items=(item,))
    invoice_2 = Invoice(customer_id="target-customer", items=(item,))

    invoice_3 = Invoice(customer_id="other-customer", items=(item,))

    fake_uow.invoices.save(invoice_1)
    fake_uow.invoices.save(invoice_2)
    fake_uow.invoices.save(invoice_3)

    use_case = GetCustomerInvoicesUseCase(uow=fake_uow)

    results = use_case.execute(customer_id="target-customer")

    assert len(results) == 2

    returned_ids = [inv.id for inv in results]
    assert invoice_1.id in returned_ids
    assert invoice_2.id in returned_ids
    assert invoice_3.id not in returned_ids
