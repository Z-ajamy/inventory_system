from decimal import Decimal

import pytest

from domain.entities.settings import SystemSettings
from domain.shared.value_objects import Money
from tests.fakes.fake_uow import FakeUnitOfWork


@pytest.fixture
def fake_uow():
    settings = SystemSettings(
        max_anonymous_invoice_amount=Money(amount=Decimal("1000.0"))
    )
    return FakeUnitOfWork(default_settings=settings)
