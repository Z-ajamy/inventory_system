import pytest
from decimal import Decimal
from datetime import datetime
from domain.entities.stock_batch import StockBatch
from domain.shared.value_objects import Money

@pytest.fixture
def sample_batch():
    return StockBatch(
        product_id="prod-123",
        init_quantity=100,
        current_quantity=100,
        unit_cost=Money(amount=Decimal("10.0")),
        item_price=Money(amount=Decimal("15.0"))
    )

def test_sell_items_success(sample_batch):
    sample_batch.sell_items(20)
    assert sample_batch.current_quantity == 80

def test_sell_items_insufficient_quantity(sample_batch):
    with pytest.raises(ValueError, match="Insufficient quantity"):
        sample_batch.sell_items(101)

def test_sell_items_negative_amount(sample_batch):
    with pytest.raises(ValueError, match="Amount must be positive"):
        sample_batch.sell_items(-5)

def test_stock_batch_received_at_default(sample_batch):
    assert isinstance(sample_batch.received_at, datetime)
