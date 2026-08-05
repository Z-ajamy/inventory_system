from decimal import Decimal

import pytest

from application.exceptions.inventory import InventoryProductNotFoundError
from application.inventory.dtos import ReceiveStockBatchRequestDTO
from application.inventory.receive_stock_batch import ReceiveStockBatchUseCase
from domain.entities.pen import PenProduct
from domain.shared.value_objects import Money
from tests.fakes.fake_uow import FakeUnitOfWork


def test_receive_stock_batch_success(fake_uow: FakeUnitOfWork):
    product = PenProduct(
        brand_id="brand-1",
        init_sku="PEN-101",
        init_selling_price=Money(amount=Decimal("15.0")),
        init_color_id="c1",
        init_pen_type_id="t1",
    )
    fake_uow.products.save(product)

    request = ReceiveStockBatchRequestDTO(
        product_id=product.id, quantity=100, unit_cost=Decimal("8.50")
    )
    use_case = ReceiveStockBatchUseCase(uow=fake_uow)

    batch_id = use_case.execute(request)

    assert fake_uow.committed is True

    saved_batch = fake_uow.batches.get_by_id(batch_id)
    assert saved_batch is not None
    assert saved_batch.product_id == product.id
    assert saved_batch.init_quantity == 100
    assert saved_batch.current_quantity == 100
    assert saved_batch.unit_cost.amount == Decimal("8.50")


def test_receive_stock_batch_raises_product_not_found(fake_uow: FakeUnitOfWork):
    request = ReceiveStockBatchRequestDTO(
        product_id="invalid-product-id", quantity=50, unit_cost=Decimal("10.0")
    )
    use_case = ReceiveStockBatchUseCase(uow=fake_uow)

    with pytest.raises(InventoryProductNotFoundError):
        use_case.execute(request)
