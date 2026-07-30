from domain.shared.base import Brand, ProductFamily


def test_brand_supports_family():
    brand = Brand(
        name="Faber-Castell",
        supported_families=(ProductFamily.PENS, ProductFamily.RULERS),
    )

    assert brand.supports(ProductFamily.PENS) is True
    assert brand.supports(ProductFamily.RULERS) is True
    assert brand.supports(ProductFamily.BOOKS) is False
