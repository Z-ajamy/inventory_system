import pytest
from decimal import Decimal

from application.catalog.create_product import CreatePenUseCase
from application.catalog.dtos import CreatePenRequestDTO
from application.exceptions.catalog import DuplicateSkuError, ReferenceNotFoundError
from domain.entities.pen import PenProduct
from domain.shared.base import Brand, InfoCategory, ProductFamily
from domain.shared.value_objects import Money
from tests.fakes.fake_uow import FakeUnitOfWork


def test_create_pen_success(fake_uow: FakeUnitOfWork):
    brand = Brand(init_name="Roco", supported_families=[ProductFamily.PENS])
    fake_uow.reference_data.save(brand)

    request = CreatePenRequestDTO(
        sku="PEN-100",
        brand_id=brand.id,
        selling_price=Decimal("15.50"),
        color_id="color-red",
        pen_type_id="type-ballpoint"
    )
    use_case = CreatePenUseCase(uow=fake_uow)

    product_id = use_case.execute(request)

    assert fake_uow.committed is True
    saved_pen = fake_uow.products.get_by_id(product_id)
    assert saved_pen is not None
    assert saved_pen.sku == "PEN-100"
    assert saved_pen.selling_price.amount == Decimal("15.50")
    assert isinstance(saved_pen, PenProduct)


def test_create_pen_raises_duplicate_sku(fake_uow: FakeUnitOfWork):
    existing_pen = PenProduct(
        brand_id="brand-1", init_sku="PEN-100", 
        init_selling_price=Money(amount=Decimal("10.0")),
        init_color_id="c1", init_pen_type_id="t1"
    )
    fake_uow.products.save(existing_pen)

    request = CreatePenRequestDTO(
        sku="PEN-100", brand_id="brand-1", selling_price=Decimal("15.0"),
        color_id="c1", pen_type_id="t1"
    )
    use_case = CreatePenUseCase(uow=fake_uow)

    with pytest.raises(DuplicateSkuError):
        use_case.execute(request)


def test_create_pen_raises_brand_not_found(fake_uow: FakeUnitOfWork):
    request = CreatePenRequestDTO(
        sku="PEN-200", brand_id="invalid-brand", selling_price=Decimal("15.0"),
        color_id="c1", pen_type_id="t1"
    )
    use_case = CreatePenUseCase(uow=fake_uow)

    with pytest.raises(ReferenceNotFoundError):
        use_case.execute(request)
