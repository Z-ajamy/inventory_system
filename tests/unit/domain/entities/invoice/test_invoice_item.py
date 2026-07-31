from decimal import Decimal

import pytest

from domain.entities.invoice.invoice_item import InvoiceItem
from domain.exceptions.invoice.exceptions import InvalidInvoiceItemQuantityError
from domain.shared.value_objects import Money


def test_invoice_item_creation_and_price_calculation():
    item = InvoiceItem(
        product_id="prod-1",
        stock_batch_id="batch-1",
        num_of_items=5,
        price_of_item=Money(amount=Decimal("10.0")),
    )
    assert item.num_of_items == 5
    assert item.price.amount == Decimal("50.0")


def test_invoice_item_zero_quantity_raises_error():
    with pytest.raises(InvalidInvoiceItemQuantityError) as exc_info:
        InvoiceItem(
            product_id="prod-1",
            stock_batch_id="batch-1",
            num_of_items=0,
            price_of_item=Money(amount=Decimal("10.0")),
        )
    assert exc_info.value.code == "INVALID_INVOICE_ITEM_QUANTITY"


def test_invoice_item_negative_quantity_raises_error():
    with pytest.raises(InvalidInvoiceItemQuantityError):
        InvoiceItem(
            product_id="prod-1",
            stock_batch_id="batch-1",
            num_of_items=-3,
            price_of_item=Money(amount=Decimal("10.0")),
        )
