from domain.exceptions.base import EntitiesBaseError


class NegativeMoneyError(EntitiesBaseError):
    def __init__(self, amount: float):
        super().__init__(
            message="Money amount cannot be negative.",
            code="NEGATIVE_MONEY",
            context={"amount": amount},
        )


class CurrencyMismatchError(EntitiesBaseError):
    def __init__(self, base_currency: str, other_currency: str):
        super().__init__(
            message=f"Cannot perform operations between different currencies: {base_currency} and {other_currency}.",
            code="CURRENCY_MISMATCH",
            context={"base_currency": base_currency, "other_currency": other_currency},
        )


class InvalidMoneyOperationError(EntitiesBaseError):
    def __init__(self, operation: str, unsupported_type: str):
        super().__init__(
            message=f"Cannot perform '{operation}' between Money and {unsupported_type}.",
            code="INVALID_MONEY_OPERATION",
            context={"operation": operation, "unsupported_type": unsupported_type},
        )
