from domain.exceptions.base import EntitiesBaseError

class CustomerNotFoundError(EntitiesBaseError):
    def __init__(self, customer_id: str):
        super().__init__(
            message=f"Customer with id '{customer_id}' not found.",
            code="CUSTOMER_NOT_FOUND",
            context={"customer_id": customer_id},
        )
