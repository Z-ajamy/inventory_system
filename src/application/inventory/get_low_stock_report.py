from application.inventory.dtos import LowStockBatchResponseDTO
from domain.interfaces.uow import UnitOfWorkProtocol


class GetLowStockReportUseCase:
    def __init__(self, uow: UnitOfWorkProtocol):
        self.uow = uow

    def execute(self, threshold_quantity: int) -> tuple[LowStockBatchResponseDTO, ...]:
        with self.uow as db:
            low_batches = db.batches.get_low_stock(threshold_quantity=threshold_quantity)

            report = tuple(
                LowStockBatchResponseDTO(
                    batch_id=batch.id,
                    product_id=batch.product_id,
                    current_quantity=batch.current_quantity,
                    received_at=batch.received_at,
                    unit_cost=batch.unit_cost.amount
                )
                for batch in low_batches
            )

            return report
