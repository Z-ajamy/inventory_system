from domain.exceptions.base import EntitiesBaseError


class ProductNotFoundError(EntitiesBaseError):
    def __init__(self, product_id: str):
        super().__init__(
            message=f"Product with id '{product_id}' not found.",
            code="PRODUCT_NOT_FOUND",
            context={"product_id": product_id},
        )


class QuantityIsLessThanOrderError(EntitiesBaseError):
    def __init__(self, product_id: str, current_quantity: int):
        super().__init__(
            message=f"Insufficient quantity for product '{product_id}'. Available: {current_quantity}.",
            code="INSUFFICIENT_QUANTITY",
            context={"product_id": product_id, "current_quantity": current_quantity},
        )
