from domain.exceptions.base import EntitiesBaseError


class InvalidBatchQuantityError(EntitiesBaseError):
    def __init__(self, quantity: int):
        super().__init__(
            message="Batch initial or current quantity cannot be negative.",
            code="INVALID_BATCH_QUANTITY",
            context={"quantity": quantity}
        )

class NegativeSellAmountError(EntitiesBaseError):
    def __init__(self, amount: int):
        super().__init__(
            message="Cannot sell a negative amount of items.",
            code="NEGATIVE_SELL_AMOUNT",
            context={"amount": amount}
        )

class InsufficientStockError(EntitiesBaseError):
    def __init__(self, requested: int, available: int):
        super().__init__(
            message=f"Cannot sell {requested} items. Only {available} available.",
            code="INSUFFICIENT_STOCK",
            context={"requested": requested, "available": available}
        )
