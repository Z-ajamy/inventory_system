from typing import Protocol

from domain.entities.stock_batch import StockBatch


class StockBatchRepositoryProtocol(Protocol):
    def save(self, stock_batch: StockBatch) -> None: ...

    def get_by_id(self, stock_batch_id: str) -> StockBatch | None: ...

    def get_by_product_id(self, product_id: str) -> tuple[StockBatch, ...]: ...

    def get_available_for_product(
        self, product_id: str
    ) -> tuple[
        StockBatch, ...
    ]: ...  # Just current_quantity > 0 and ORDER BY received_at ASC

    def get_total_quantity_for_product(self, product_id: str) -> int: ...

    def get_low_stock(self, threshold_quantity: int) -> tuple[StockBatch, ...]: ...
