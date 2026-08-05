from dataclasses import dataclass
from decimal import Decimal

from domain.shared.base import ProductFamily


@dataclass(slots=True, frozen=True, kw_only=True)
class CreatePenRequestDTO:
    sku: str
    brand_id: str
    selling_price: Decimal
    color_id: str
    pen_type_id: str


@dataclass(slots=True, frozen=True, kw_only=True)
class CreateRulerRequestDTO:
    sku: str
    brand_id: str
    selling_price: Decimal
    ruler_type_id: str
    length_cm: int


@dataclass(slots=True, frozen=True, kw_only=True)
class CreateNoteBookRequestDTO:
    sku: str
    brand_id: str
    selling_price: Decimal
    page_count: int
    type_id: str


@dataclass(slots=True, frozen=True, kw_only=True)
class CreateSchoolBookRequestDTO:
    sku: str
    brand_id: str
    selling_price: Decimal
    subject_id: str
    class_id: str
    academic_year: str


@dataclass(slots=True, frozen=True, kw_only=True)
class UpdateProductPriceRequestDTO:
    product_id: str
    new_price: Decimal


@dataclass(slots=True, frozen=True, kw_only=True)
class ProductResponseDTO:
    id: str
    sku: str
    type: ProductFamily
    brand_id: str
    selling_price: Decimal
    available_quantity: int
    attributes: dict[str, str | int]
