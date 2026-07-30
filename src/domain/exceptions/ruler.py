from domain.exceptions.base import EntitiesBaseError

class InvalidRulerLengthError(EntitiesBaseError):
    def __init__(self, length_cm: int):
        super().__init__(
            message=f"Ruler length must be greater than zero. Got: {length_cm}",
            code="INVALID_RULER_LENGTH",
            context={"length_cm": length_cm}
        )
