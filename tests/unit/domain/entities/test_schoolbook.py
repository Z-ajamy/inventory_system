from decimal import Decimal

from domain.entities.schoolbook import SchoolBook
from domain.shared.value_objects import Money


def test_schoolbook_creation():
    book = SchoolBook(
        init_sku="BOOK-MATH-G1",
        brand_id="ministry-edu",
        init_subject_id="math",
        init_class_id="grade-1",
        init_academic_year="2023/2024",
        init_selling_price=Money(amount=Decimal("100.0")),
    )
    assert book.subject_id == "math"
    assert book.academic_year == "2023/2024"
    assert book.id is not None
