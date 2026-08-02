from decimal import Decimal

import pytest

from domain.entities.invoice.draft_invoice import DraftInvoice
from domain.entities.invoice.invoice import Invoice
from domain.entities.stock_batch import StockBatch
from domain.exceptions.invoice.exceptions import (
    AnonymousLargeInvoiceError,
    EmptyInvoiceFinalizationError,
)
from domain.shared.value_objects import Money


@pytest.fixture
def sample_batch_low_price():
    return StockBatch(
        init_product_id="prod-low",
        init_init_quantity=100,
        init_current_quantity=100,
        unit_cost=Money(amount=Decimal("5.0")),
    )


@pytest.fixture
def sample_batch_high_price():
    return StockBatch(
        init_product_id="prod-high",
        init_init_quantity=100,
        init_current_quantity=100,
        unit_cost=Money(amount=Decimal("50.0")),
    )


@pytest.fixture
def anonymous_limit():
    return Money(amount=Decimal("100.0"))


def test_draft_add_and_remove_item(sample_batch_low_price):
    draft = DraftInvoice()
    draft.add_item(
        sample_batch_low_price,
        quantity=2,
        selling_price=Money(amount=Decimal("10.0")),
    )
    assert draft.current_total.amount == Decimal("20.0")

    draft.remove_item("prod-low")
    assert draft.current_total.amount == Decimal("0.0")


def test_draft_finalize_empty_raises_error(anonymous_limit):
    draft = DraftInvoice()
    with pytest.raises(EmptyInvoiceFinalizationError) as exc_info:
        draft.finalize(anonymous_limit=anonymous_limit)
    assert exc_info.value.code == "EMPTY_INVOICE_FINALIZATION"


def test_draft_finalize_anonymous_large_raises_error(
    sample_batch_high_price, anonymous_limit
):
    draft = DraftInvoice()
    draft.add_item(
        sample_batch_high_price,
        quantity=1,
        selling_price=Money(amount=Decimal("150.0")),
    )

    with pytest.raises(AnonymousLargeInvoiceError) as exc_info:
        draft.finalize(anonymous_limit=anonymous_limit)
    assert exc_info.value.code == "ANONYMOUS_LARGE_INVOICE"


def test_draft_finalize_success_anonymous_small(
    sample_batch_low_price, anonymous_limit
):
    draft = DraftInvoice()
    draft.add_item(
        sample_batch_low_price,
        quantity=3,
        selling_price=Money(amount=Decimal("10.0")),
    )

    final_invoice = draft.finalize(anonymous_limit=anonymous_limit)
    assert isinstance(final_invoice, Invoice)
    assert final_invoice.total_price.amount == Decimal("30.0")
    assert final_invoice.customer_id is None


def test_draft_finalize_success_with_customer(sample_batch_high_price, anonymous_limit):
    draft = DraftInvoice(customer_id="cust-123")
    draft.add_item(
        sample_batch_high_price,
        quantity=2,
        selling_price=Money(amount=Decimal("150.0")),
    )

    final_invoice = draft.finalize(anonymous_limit=anonymous_limit)
    assert isinstance(final_invoice, Invoice)
    assert final_invoice.customer_id == "cust-123"
    assert final_invoice.total_price.amount == Decimal("300.0")
