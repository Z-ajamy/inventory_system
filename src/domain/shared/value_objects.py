from dataclasses import dataclass
from decimal import Decimal
from enum import Enum, auto
from typing import Any

from domain.exceptions.money import (
    CurrencyMismatchError,
    InvalidMoneyOperationError,
    NegativeMoneyError,
)


class OldStrEnum(str, Enum):
    @staticmethod
    def _generate_next_value_(
        name: str, start: int, count: int, last_values: list[Any]
    ) -> str:
        return name.lower()


class Currency(OldStrEnum):
    USD = auto()
    EGP = auto()


@dataclass(slots=True, kw_only=True, frozen=True)
class Money:
    amount: Decimal
    currency: Currency = Currency.EGP

    def __post_init__(self):
        if self.amount < Decimal("0.0"):
            raise NegativeMoneyError(amount=float(self.amount))

    def __add__(self, other: Any) -> "Money":
        if not isinstance(other, Money):
            raise InvalidMoneyOperationError(
                operation="addition", unsupported_type=type(other).__name__
            )

        if self.currency != other.currency:
            raise CurrencyMismatchError(
                base_currency=self.currency, other_currency=other.currency
            )

        return Money(amount=self.amount + other.amount, currency=self.currency)

    def __mul__(self, multiplier: Any) -> "Money":
        if not isinstance(multiplier, (int, Decimal)):
            raise InvalidMoneyOperationError(
                operation="multiplication", unsupported_type=type(multiplier).__name__
            )

        return Money(amount=self.amount * Decimal(multiplier), currency=self.currency)

    def __rmul__(self, multiplier: Any) -> "Money":
        return self.__mul__(multiplier)

    def __sub__(self, other: Any) -> "Money":
        if not isinstance(other, Money):
            raise InvalidMoneyOperationError(
                operation="subtraction", unsupported_type=type(other).__name__
            )

        if self.currency != other.currency:
            raise CurrencyMismatchError(
                base_currency=self.currency, other_currency=other.currency
            )

        return Money(amount=self.amount - other.amount, currency=self.currency)
