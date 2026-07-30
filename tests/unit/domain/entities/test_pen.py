from domain.entities.pen import PenProduct


def test_pen_product_creation():
    pen = PenProduct(
        sku="PEN-BLUE-001",
        brand_id="brand-1",
        color_id="color-blue",
        pen_type_id="type-ballpoint",
    )
    assert pen.sku == "PEN-BLUE-001"
    assert pen.color_id == "color-blue"
    assert pen.id is not None
