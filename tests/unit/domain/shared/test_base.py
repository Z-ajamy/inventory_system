from decimal import Decimal

import pytest

from domain.exceptions.shared import InvalidPriceError, InvalidStringError
from domain.shared.base import Brand, Info, Product, ProductFamily
from domain.shared.value_objects import Money


def test_info_creation_and_validation():
    info = Info(init_name="  Blue  ", category=ProductFamily.PENS)
    assert info.name == "Blue"

    with pytest.raises(InvalidStringError):
        Info(init_name="   ", category=ProductFamily.PENS)


def test_brand_supports_family():
    brand = Brand(
        init_name="Faber-Castell",
        supported_families=[ProductFamily.PENS, ProductFamily.RULERS],
    )

    assert brand.supports(ProductFamily.PENS) is True
    assert brand.supports(ProductFamily.RULERS) is True
    assert brand.supports(ProductFamily.BOOKS) is False


def test_product_price_and_sku_validation():
    price = Money(amount=Decimal("50.0"))
    product = Product(
        type=ProductFamily.PENS,
        brand_id="b-1",
        init_sku="SKU-123",
        init_selling_price=price,
    )

    assert product.sku == "SKU-123"
    assert product.selling_price.amount == Decimal("50.0")

    # اختبار تغيير السعر بسعر غير صالح (<= 0)
    with pytest.raises(InvalidPriceError):
        product.change_price(Money(amount=Decimal("0.0")))

    # اختبار إدخال SKU فارغ
    with pytest.raises(InvalidStringError):
        product.sku = "   "
