from decimal import Decimal

from domain.entities.pen import PenProduct
from domain.shared.value_objects import Money


def test_pen_product_creation():
    pen = PenProduct(
        init_sku="PEN-BLUE-001",
        brand_id="brand-1",
        init_color_id="color-blue",
        init_pen_type_id="type-ballpoint",
        init_selling_price=Money(amount=Decimal("15.0")),
    )
    assert pen.sku == "PEN-BLUE-001"
    assert pen.color_id == "color-blue"
    assert pen.id is not None
