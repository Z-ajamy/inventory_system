from decimal import Decimal

import pytest

from application.catalog.get_product import GetProductUseCase
from application.exceptions.catalog import ProductNotFoundError
from domain.entities.notebook import NoteBook
from domain.entities.stock_batch import StockBatch
from domain.shared.value_objects import Money
from tests.fakes.fake_uow import FakeUnitOfWork


def test_get_product_success_with_inventory(fake_uow: FakeUnitOfWork):
    notebook = NoteBook(
        brand_id="b1",
        init_sku="NB-100",
        init_selling_price=Money(amount=Decimal("30.0")),
        init_page_count=100,
        init_type_id="wire-bound",
    )
    fake_uow.products.save(notebook)

    batch_1 = StockBatch(
        init_product_id=notebook.id,
        init_init_quantity=50,
        init_current_quantity=10,
        unit_cost=Money(amount=Decimal("20.0")),
    )
    batch_2 = StockBatch(
        init_product_id=notebook.id,
        init_init_quantity=50,
        init_current_quantity=50,
        unit_cost=Money(amount=Decimal("22.0")),
    )
    fake_uow.batches.save(batch_1)
    fake_uow.batches.save(batch_2)

    use_case = GetProductUseCase(uow=fake_uow)
    result = use_case.execute(product_id=notebook.id)

    assert result.id == notebook.id
    assert result.sku == "NB-100"
    assert result.selling_price == Decimal("30.0")

    assert result.available_quantity == 60

    assert result.attributes["page_count"] == 100
    assert result.attributes["type_id"] == "wire-bound"


def test_get_product_raises_not_found(fake_uow: FakeUnitOfWork):
    use_case = GetProductUseCase(uow=fake_uow)

    with pytest.raises(ProductNotFoundError):
        use_case.execute(product_id="invalid-id")
