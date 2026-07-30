from dataclasses import dataclass

from domain.shared.base import Info, Product


@dataclass(slots=True, frozen=True, kw_only=True)
class SchoolBookSubject(Info):
    pass


@dataclass(slots=True, frozen=True, kw_only=True)
class SchoolBookClass(Info):
    pass


@dataclass(slots=True, frozen=True, kw_only=True)
class SchoolBook(Product):
    subject_id: str
    class_id: str
    academic_year: str
    # Publisher is the Brand
