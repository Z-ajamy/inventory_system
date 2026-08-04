import pytest
from decimal import Decimal

from application.settings.get_settings import GetCurrentSettingsUseCase
from tests.fakes.fake_uow import FakeUnitOfWork


def test_get_current_settings_success(fake_uow: FakeUnitOfWork):
    use_case = GetCurrentSettingsUseCase(uow=fake_uow)

    result = use_case.execute()

    assert result.max_anonymous_invoice_amount == Decimal("1000.0")
