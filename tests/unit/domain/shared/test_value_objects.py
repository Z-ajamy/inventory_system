import pytest
from decimal import Decimal
from domain.shared.value_objects import Currency, Money
from domain.exceptions.money import NegativeMoneyError

def test_money_creation_success():
    price = Money(amount=Decimal("10.50"), currency=Currency.USD)
    assert price.amount == Decimal("10.50")
    assert price.currency == "usd"

def test_money_negative_amount_raises_error():
    with pytest.raises(NegativeMoneyError) as exc_info:
        Money(amount=Decimal("-1.0"))
    
    assert exc_info.value.code == "NEGATIVE_MONEY"

def test_currency_enum_lowercase():
    assert Currency.USD == "usd"
    assert Currency.EGP == "egp"
