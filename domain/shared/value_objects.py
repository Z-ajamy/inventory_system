from dataclasses import dataclass
from decimal import Decimal
from enum import Enum, auto
from typing import Any


class OldStrEnum(str, Enum):
    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list[Any]) -> str:
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
            raise ValueError("Money amount cannot be negative")

