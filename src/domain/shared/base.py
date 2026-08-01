from dataclasses import dataclass, field
from enum import auto

from domain.shared.utils import create_uuid4
from domain.shared.value_objects import OldStrEnum


class InfoCategory(OldStrEnum):
    PEN_COLOR = auto()
    PEN_TYPE = auto()
    RULER_TYPE = auto()
    SCHOOLBOOK_SUBJECT = auto()
    SCHOOLBOOK_CLASS = auto()
    BRAND = auto()


@dataclass(slots=True, frozen=True, kw_only=True)
class Info:
    id: str = field(default_factory=create_uuid4)
    name: str
    category: InfoCategory


class ProductFamily(OldStrEnum):
    PENS = auto()
    RULERS = auto()
    BOOKS = auto()
    NOTEBOOKS = auto()


@dataclass(slots=True, frozen=True, kw_only=True)
class Brand(Info):
    supported_families: tuple[ProductFamily, ...]

    category: InfoCategory = field(default=InfoCategory.BRAND, init=False)

    def supports(self, family: ProductFamily) -> bool:
        return family in self.supported_families


@dataclass(slots=True, kw_only=True, frozen=True)
class Product:
    id: str = field(default_factory=create_uuid4)
    type: ProductFamily
    sku: str
    brand_id: str
