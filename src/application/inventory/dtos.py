from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass(slots=True, frozen=True, kw_only=True)
class ReceiveStockBatchRequestDTO:
    product_id: str
    quantity: int
    unit_cost: Decimal


@dataclass(slots=True, frozen=True, kw_only=True)
class LowStockBatchResponseDTO:
    batch_id: str
    product_id: str
    current_quantity: int
    received_at: datetime
    unit_cost: Decimal
