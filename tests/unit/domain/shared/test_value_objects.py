from decimal import Decimal

import pytest

from domain.shared.value_objects import Currency, Money


def test_money_creation_success():
    price = Money(amount=Decimal("10.50"), currency=Currency.USD)
    assert price.amount == Decimal("10.50")
    assert price.currency == "usd"  # Testing OldStrEnum behavior

def test_money_negative_amount_raises_error():
    with pytest.raises(ValueError, match="Money amount cannot be negative"):
        Money(amount=Decimal("-1.0"))

def test_currency_enum_lowercase():
    assert Currency.USD == "usd"
    assert Currency.EGP == "egp"
