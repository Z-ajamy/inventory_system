from decimal import Decimal

import pytest

from domain.entities.ruler import RulerProduct, RulerType
from domain.exceptions.ruler import InvalidRulerLengthError
from domain.shared.value_objects import Money


def test_ruler_type_creation_success():
    ruler_type = RulerType(init_name="Engineering Ruler")
    assert ruler_type.name == "Engineering Ruler"
    assert ruler_type.id is not None


def test_ruler_product_creation_success():
    product = RulerProduct(
        init_sku="RUL-30-ENG",
        brand_id="brand-1",
        init_ruler_type_id="type-1",
        init_length_cm=30,
        init_selling_price=Money(amount=Decimal("10.0")),
    )
    assert product.sku == "RUL-30-ENG"
    assert product.length_cm == 30


def test_ruler_product_negative_length_raises_error():
    with pytest.raises(InvalidRulerLengthError) as exc_info:
        RulerProduct(
            init_sku="RUL-BAD",
            brand_id="brand-1",
            init_ruler_type_id="type-1",
            init_length_cm=-10,
            init_selling_price=Money(amount=Decimal("10.0")),
        )
    assert exc_info.value.code == "INVALID_RULER_LENGTH"


def test_ruler_product_zero_length_raises_error():
    with pytest.raises(InvalidRulerLengthError) as exc_info:
        RulerProduct(
            init_sku="RUL-ZERO",
            brand_id="brand-1",
            init_ruler_type_id="type-1",
            init_length_cm=0,
            init_selling_price=Money(amount=Decimal("10.0")),
        )
    assert exc_info.value.code == "INVALID_RULER_LENGTH"
