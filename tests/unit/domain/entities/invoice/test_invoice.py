from decimal import Decimal

from domain.entities.invoice.invoice import Invoice
from domain.entities.invoice.invoice_item import InvoiceItem
from domain.shared.value_objects import Money


def test_immutable_invoice_properties():
    item1 = InvoiceItem(
        product_id="p1",
        stock_batch_id="b1",
        num_of_items=2,
        price_of_item=Money(amount=Decimal("10.0")),
    )
    item2 = InvoiceItem(
        product_id="p2",
        stock_batch_id="b2",
        num_of_items=1,
        price_of_item=Money(amount=Decimal("50.0")),
    )

    invoice = Invoice(customer_id="cust-1", items=(item1, item2))

    assert invoice.items_count == 2
    assert invoice.total_price.amount == Decimal("70.0")
    assert isinstance(invoice.items, tuple)
