import pytest
from datetime import datetime
from decimal import Decimal
from domain.entities.stock_batch import StockBatch
from domain.shared.value_objects import Money
from domain.exceptions.stock_batch import NegativeSellAmountError, InsufficientStockError

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

def test_sell_items_insufficient_quantity_raises_error(sample_batch):
    with pytest.raises(InsufficientStockError) as exc_info:
        sample_batch.sell_items(101)
    
    assert exc_info.value.code == "INSUFFICIENT_STOCK"

def test_sell_items_negative_amount_raises_error(sample_batch):
    with pytest.raises(NegativeSellAmountError) as exc_info:
        sample_batch.sell_items(-5)
        
    assert exc_info.value.code == "NEGATIVE_SELL_AMOUNT"

def test_stock_batch_change_price(sample_batch):
    new_price = Money(amount=Decimal("20.0"))
    sample_batch.change_price(new_price)
    assert sample_batch.item_price.amount == Decimal("20.0")

def test_stock_batch_received_at_default(sample_batch):
    assert isinstance(sample_batch.received_at, datetime)
