from domain.exceptions.base import EntitiesBaseError


class InvoiceNotFoundError(EntitiesBaseError):
    def __init__(self, invoice_id: str):
        super().__init__(
            message=f"Invoice with id '{invoice_id}' not found.",
            code="INVOICE_NOT_FOUND",
            context={"invoice_id": invoice_id},
        )
