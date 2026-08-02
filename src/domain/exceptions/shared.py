from domain.exceptions.base import EntitiesBaseError


class InvalidStringError(EntitiesBaseError):
    def __init__(self, field_name: str):
        super().__init__(
            message=f"The field '{field_name}' cannot be empty or whitespace.",
            code="INVALID_STRING",
            context={"field_name": field_name},
        )


class InvalidPriceError(EntitiesBaseError):
    def __init__(self, amount: float):
        super().__init__(
            message="Price amount must be greater than zero.",
            code="INVALID_PRICE",
            context={"amount": amount},
        )
