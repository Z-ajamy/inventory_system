from decimal import Decimal
from application.catalog.dtos import CreateNoteBookRequestDTO, CreatePenRequestDTO, CreateRulerRequestDTO
from application.exceptions.catalog import DuplicateSkuError, ReferenceNotFoundError
from domain.entities.notebook import NoteBook
from domain.entities.pen import PenProduct
from domain.entities.ruler import RulerProduct
from domain.interfaces.uow import UnitOfWorkProtocol
from domain.shared.value_objects import Money


class CreatePenUseCase:
    def __init__(self, uow: UnitOfWorkProtocol):
        self.uow = uow

    def execute(self, request: CreatePenRequestDTO) -> str:
        with self.uow as db:
            if db.products.get_by_sku(request.sku):
                raise DuplicateSkuError(sku=request.sku)
            
            if not db.reference_data.get_by_id(request.brand_id):
                raise ReferenceNotFoundError(ref_type="Brand", ref_id=request.brand_id)

            pen = PenProduct(
                brand_id=request.brand_id,
                init_sku=request.sku,
                init_selling_price=Money(amount=Decimal(str(request.selling_price))),
                init_color_id=request.color_id,
                init_pen_type_id=request.pen_type_id
            )
            
            db.products.save(pen)
            db.commit()
            return pen.id


class CreateRulerUseCase:
    def __init__(self, uow: UnitOfWorkProtocol):
        self.uow = uow

    def execute(self, request: CreateRulerRequestDTO) -> str:
        with self.uow as db:
            if db.products.get_by_sku(request.sku):
                raise DuplicateSkuError(sku=request.sku)

            ruler = RulerProduct(
                brand_id=request.brand_id,
                init_sku=request.sku,
                init_selling_price=Money(amount=Decimal(str(request.selling_price))),
                init_ruler_type_id=request.ruler_type_id,
                init_length_cm=request.length_cm
            )
            
            db.products.save(ruler)
            db.commit()
            return ruler.id

from application.catalog.dtos import CreateNoteBookRequestDTO, CreateSchoolBookRequestDTO
from domain.entities.notebook import NoteBook
from domain.entities.schoolbook import SchoolBook

class CreateNoteBookUseCase:
    def __init__(self, uow: UnitOfWorkProtocol):
        self.uow = uow

    def execute(self, request: CreateNoteBookRequestDTO) -> str:
        with self.uow as db:
            if db.products.get_by_sku(request.sku):
                raise DuplicateSkuError(sku=request.sku)

            notebook = NoteBook(
                brand_id=request.brand_id,
                init_sku=request.sku,
                init_selling_price=Money(amount=Decimal(str(request.selling_price))),
                init_page_count=request.page_count,
                init_type_id=request.type_id
            )
            
            db.products.save(notebook)
            db.commit()
            return notebook.id


class CreateSchoolBookUseCase:
    def __init__(self, uow: UnitOfWorkProtocol):
        self.uow = uow

    def execute(self, request: CreateSchoolBookRequestDTO) -> str:
        with self.uow as db:
            if db.products.get_by_sku(request.sku):
                raise DuplicateSkuError(sku=request.sku)

            book = SchoolBook(
                brand_id=request.brand_id,
                init_sku=request.sku,
                init_selling_price=Money(amount=Decimal(str(request.selling_price))),
                init_subject_id=request.subject_id,
                init_class_id=request.class_id,
                init_academic_year=request.academic_year
            )
            
            db.products.save(book)
            db.commit()
            return book.id
