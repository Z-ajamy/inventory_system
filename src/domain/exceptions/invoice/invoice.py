from domain.exceptions.base import EntitiesBaseError


class InvalidInVoiceItemsNumberError(EntitiesBaseError):
    def __init__(self, num: int):
        super().__init__(
            message="the number of invoice items cannot be negative or zero.",
            code="INVALID_NUMBER_OF_INVOICE_ITEMS",
            context={"number": num},
        )
