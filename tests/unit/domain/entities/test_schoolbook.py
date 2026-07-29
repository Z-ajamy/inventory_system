from domain.entities.schoolbook import SchoolBook

def test_schoolbook_creation():
    book = SchoolBook(
        sku="BOOK-MATH-G1",
        brand_id="ministry-edu",
        subject_id="math",
        class_id="grade-1",
        academic_year="2023/2024"
    )
    assert book.subject_id == "math"
    assert book.academic_year == "2023/2024"
