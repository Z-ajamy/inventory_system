from decimal import Decimal

from domain.entities.settings import SystemSettings
from domain.shared.value_objects import Currency, Money


def test_system_settings_creation():
    limit = Money(amount=Decimal("100.0"), currency=Currency.EGP)

    settings = SystemSettings(max_anonymous_invoice_amount=limit)

    assert settings.max_anonymous_invoice_amount.amount == Decimal("100.0")
    assert settings.max_anonymous_invoice_amount.currency == Currency.EGP
    assert settings.id is not None
