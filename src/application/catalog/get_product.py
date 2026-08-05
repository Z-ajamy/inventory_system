from application.catalog.dtos import ProductResponseDTO
from application.exceptions.catalog import ProductNotFoundError
from domain.entities.notebook import NoteBook
from domain.entities.pen import PenProduct
from domain.entities.ruler import RulerProduct
from domain.entities.schoolbook import SchoolBook
from domain.interfaces.uow import UnitOfWorkProtocol


class GetProductUseCase:
    def __init__(self, uow: UnitOfWorkProtocol):
        self.uow = uow

    def execute(self, product_id: str) -> ProductResponseDTO:
        with self.uow as db:
            product = db.products.get_by_id(product_id=product_id)
            if not product:
                raise ProductNotFoundError(product_id=product_id)

            available_qty = db.batches.get_total_quantity_for_product(
                product_id=product.id
            )

            attributes = {}
            if isinstance(product, PenProduct):
                attributes = {
                    "color_id": product.color_id,
                    "pen_type_id": product.pen_type_id,
                }
            elif isinstance(product, RulerProduct):
                attributes = {
                    "ruler_type_id": product.ruler_type_id,
                    "length_cm": product.length_cm,
                }
            elif isinstance(product, NoteBook):
                attributes = {
                    "type_id": product.type_id,
                    "page_count": product.page_count,
                }
            elif isinstance(product, SchoolBook):
                attributes = {
                    "subject_id": product.subject_id,
                    "class_id": product.class_id,
                    "academic_year": product.academic_year,
                }

            return ProductResponseDTO(
                id=product.id,
                sku=product.sku,
                type=product.type,
                brand_id=product.brand_id,
                selling_price=product.selling_price.amount,
                available_quantity=available_qty,
                attributes=attributes,
            )
