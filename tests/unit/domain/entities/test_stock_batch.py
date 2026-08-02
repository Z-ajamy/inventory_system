from datetime import datetime
from decimal import Decimal

import pytest

from domain.entities.stock_batch import StockBatch
from domain.exceptions.stock_batch import (
    InsufficientStockError,
    NegativeSellAmountError,
)
from domain.shared.value_objects import Money


@pytest.fixture
def sample_batch():
    return StockBatch(
        init_product_id="prod-123",
        init_init_quantity=100,
        init_current_quantity=100,
        unit_cost=Money(amount=Decimal("10.0")),
    )


def test_sell_items_success(sample_batch):
    sample_batch.sell_items(20)
    assert sample_batch.current_quantity == 80


def test_sell_items_insufficient_quantity_raises_error(sample_batch):
    with pytest.raises(InsufficientStockError) as exc_info:
        sample_batch.sell_items(101)

    assert exc_info.value.code == "INSUFFICIENT_STOCK"


def test_sell_items_negative_amount_raises_error(sample_batch):
    with pytest.raises(NegativeSellAmountError) as exc_info:
        sample_batch.sell_items(-5)

    assert exc_info.value.code == "NEGATIVE_SELL_AMOUNT"


def test_stock_batch_received_at_default(sample_batch):
    assert isinstance(sample_batch.received_at, datetime)
