from dataclasses import dataclass, field

from domain.shared.base import Info, Product, ProductFamily


@dataclass(slots=True, frozen=True, kw_only=True)
class SchoolBookSubject(Info):
    category: InfoCategory = field(default=InfoCategory.SCHOOLBOOK_SUBJECT, init=False)


@dataclass(slots=True, frozen=True, kw_only=True)
class SchoolBookClass(Info):
    category: InfoCategory = field(default=InfoCategory.SCHOOLBOOK_CLASS, init=False)


@dataclass(slots=True, frozen=True, kw_only=True)
class SchoolBook(Product):
    type: ProductFamily = field(default=ProductFamily.BOOKS, init=False)
    subject_id: str
    class_id: str
    academic_year: str
    # Publisher is the Brand
