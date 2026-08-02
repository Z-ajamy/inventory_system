from dataclasses import InitVar, dataclass, field

from domain.exceptions.shared import InvalidStringError
from domain.shared.base import Info, InfoCategory, Product, ProductFamily
from domain.shared.value_objects import Money


@dataclass(slots=True, kw_only=True)
class SchoolBookSubject(Info):
    category: InfoCategory = field(default=InfoCategory.SCHOOLBOOK_SUBJECT, init=False)


@dataclass(slots=True, kw_only=True)
class SchoolBookClass(Info):
    category: InfoCategory = field(default=InfoCategory.SCHOOLBOOK_CLASS, init=False)


@dataclass(slots=True, kw_only=True)
class SchoolBook(Product):
    type: ProductFamily = field(default=ProductFamily.BOOKS, init=False)

    init_subject_id: InitVar[str]
    init_class_id: InitVar[str]
    init_academic_year: InitVar[str]

    _subject_id: str = field(init=False)
    _class_id: str = field(init=False)
    _academic_year: str = field(init=False)

    def __post_init__(
        self,
        init_sku: str,
        init_selling_price: Money,
        init_subject_id: str,
        init_class_id: str,
        init_academic_year: str,
    ):
        Product.__post_init__(self, init_sku, init_selling_price)

        self.subject_id = init_subject_id
        self.class_id = init_class_id
        self.academic_year = init_academic_year

    @property
    def subject_id(self) -> str:
        return self._subject_id

    @subject_id.setter
    def subject_id(self, value: str):
        if not value or not str(value).strip():
            raise InvalidStringError(field_name="subject_id")
        self._subject_id = str(value).strip()

    @property
    def class_id(self) -> str:
        return self._class_id

    @class_id.setter
    def class_id(self, value: str):
        if not value or not str(value).strip():
            raise InvalidStringError(field_name="class_id")
        self._class_id = str(value).strip()

    @property
    def academic_year(self) -> str:
        return self._academic_year

    @academic_year.setter
    def academic_year(self, value: str):
        if not value or not str(value).strip():
            raise InvalidStringError(field_name="academic_year")
        self._academic_year = str(value).strip()
