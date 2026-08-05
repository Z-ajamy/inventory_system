from decimal import Decimal

import pytest

from application.catalog.dtos import UpdateProductPriceRequestDTO
from application.catalog.update_product_price import UpdateProductPriceUseCase
from application.exceptions.catalog import ProductNotFoundError
from domain.entities.ruler import RulerProduct
from domain.shared.value_objects import Money
from tests.fakes.fake_uow import FakeUnitOfWork


def test_update_product_price_success(fake_uow: FakeUnitOfWork):
    ruler = RulerProduct(
        brand_id="b1",
        init_sku="RUL-20",
        init_selling_price=Money(amount=Decimal("10.0")),
        init_ruler_type_id="t1",
        init_length_cm=20,
    )
    fake_uow.products.save(ruler)

    request = UpdateProductPriceRequestDTO(
        product_id=ruler.id, new_price=Decimal("25.0")
    )
    use_case = UpdateProductPriceUseCase(uow=fake_uow)
    use_case.execute(request)

    assert fake_uow.committed is True
    updated_ruler = fake_uow.products.get_by_id(ruler.id)
    assert updated_ruler.selling_price.amount == Decimal("25.0")


def test_update_product_price_raises_not_found(fake_uow: FakeUnitOfWork):
    request = UpdateProductPriceRequestDTO(
        product_id="invalid-id", new_price=Decimal("25.0")
    )
    use_case = UpdateProductPriceUseCase(uow=fake_uow)

    with pytest.raises(ProductNotFoundError):
        use_case.execute(request)
