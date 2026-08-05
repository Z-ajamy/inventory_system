from decimal import Decimal

from application.exceptions.inventory import InventoryProductNotFoundError
from application.inventory.dtos import ReceiveStockBatchRequestDTO
from domain.entities.stock_batch import StockBatch
from domain.interfaces.uow import UnitOfWorkProtocol
from domain.shared.value_objects import Money


class ReceiveStockBatchUseCase:
    def __init__(self, uow: UnitOfWorkProtocol):
        self.uow = uow

    def execute(self, request: ReceiveStockBatchRequestDTO) -> str:
        with self.uow as db:
            product = db.products.get_by_id(product_id=request.product_id)
            if not product:
                raise InventoryProductNotFoundError(product_id=request.product_id)

            batch = StockBatch(
                init_product_id=request.product_id,
                init_init_quantity=request.quantity,
                init_current_quantity=request.quantity,
                unit_cost=Money(amount=Decimal(str(request.unit_cost))),
            )

            db.batches.save(batch)
            db.commit()

            return batch.id
