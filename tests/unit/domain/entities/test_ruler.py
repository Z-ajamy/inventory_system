import pytest
from domain.entities.ruler import RulerType, RulerProduct
from domain.exceptions.ruler import InvalidRulerLengthError

def test_ruler_type_creation_success():
    ruler_type = RulerType(name="Engineering Ruler")
    assert ruler_type.name == "Engineering Ruler"
    assert ruler_type.id is not None

def test_ruler_product_creation_success():
    product = RulerProduct(
        sku="RUL-30-ENG", 
        brand_id="brand-1", 
        ruler_type_id="type-1", 
        length_cm=30
    )
    assert product.sku == "RUL-30-ENG"
    assert product.length_cm == 30

def test_ruler_product_negative_length_raises_error():
    with pytest.raises(InvalidRulerLengthError) as exc_info:
        RulerProduct(
            sku="RUL-BAD", 
            brand_id="brand-1", 
            ruler_type_id="type-1", 
            length_cm=-10
        )
    assert exc_info.value.code == "INVALID_RULER_LENGTH"

def test_ruler_product_zero_length_raises_error():
    with pytest.raises(InvalidRulerLengthError) as exc_info:
        RulerProduct(
            sku="RUL-ZERO", 
            brand_id="brand-1", 
            ruler_type_id="type-1", 
            length_cm=0
        )
    assert exc_info.value.code == "INVALID_RULER_LENGTH"
