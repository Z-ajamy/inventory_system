from dataclasses import dataclass, field
from domain.shared.base import Product
from domain.shared.base import Info

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
    #Publisher is the Brand
