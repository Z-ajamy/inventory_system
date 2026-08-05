from domain.exceptions.base import EntitiesBaseError


class InventoryProductNotFoundError(EntitiesBaseError):
    def __init__(self, product_id: str):
        super().__init__(
            message=f"Cannot receive stock. Product with id '{product_id}' not found in catalog.",
            code="INVENTORY_PRODUCT_NOT_FOUND",
            context={"product_id": product_id},
        )
