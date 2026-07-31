from domain.exceptions.base import EntitiesBaseError


class InvalidInVoiceQuantityError(EntitiesBaseError):
    def __init__(self, quantity: int):
        super().__init__(
            message="Invoice item's quantity cannot be negative or zero.",
            code="INVALID_INVOICE_ITEM_QUANTITY",
            context={"quantity": quantity},
        )
