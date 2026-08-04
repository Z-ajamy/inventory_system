from decimal import Decimal
from application.catalog.dtos import UpdateProductPriceRequestDTO
from application.exceptions.catalog import ProductNotFoundError
from domain.interfaces.uow import UnitOfWorkProtocol
from domain.shared.value_objects import Money


class UpdateProductPriceUseCase:
    def __init__(self, uow: UnitOfWorkProtocol):
        self.uow = uow

    def execute(self, request: UpdateProductPriceRequestDTO) -> None:
        with self.uow as db:
            product = db.products.get_by_id(product_id=request.product_id)
            if not product:
                raise ProductNotFoundError(product_id=request.product_id)

            product.change_price(new_price=Money(amount=Decimal(str(request.new_price))))
            
            db.products.save(product)
            db.commit()
