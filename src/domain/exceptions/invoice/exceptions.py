from domain.exceptions.base import EntitiesBaseError


class InvalidInvoiceItemQuantityError(EntitiesBaseError):
    def __init__(self, quantity: int):
        super().__init__(
            message="Invoice item quantity must be greater than zero.",
            code="INVALID_INVOICE_ITEM_QUANTITY",
            context={"quantity": quantity},
        )


class EmptyInvoiceFinalizationError(EntitiesBaseError):
    def __init__(self):
        super().__init__(
            message="Cannot finalize an invoice without any items.",
            code="EMPTY_INVOICE_FINALIZATION",
            context={},
        )


class AnonymousLargeInvoiceError(EntitiesBaseError):
    def __init__(self, limit: float, actual_total: float):
        super().__init__(
            message=f"Invoices over {limit} must have a customer name. Got: {actual_total}",
            code="ANONYMOUS_LARGE_INVOICE",
            context={"limit": limit, "actual_total": actual_total},
        )
