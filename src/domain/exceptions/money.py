from domain.exceptions.base import EntitiesBaseError

class NegativeMoneyError(EntitiesBaseError):
    def __init__(self, amount: float):
        super().__init__(
            message="Money amount cannot be negative.",
            code="NEGATIVE_MONEY",
            context={"amount": amount}
        )
        
