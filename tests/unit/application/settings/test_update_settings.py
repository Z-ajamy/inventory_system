import pytest
from decimal import Decimal

from application.settings.dtos import UpdateSettingsRequestDTO
from application.settings.update_settings import UpdateSystemSettingsUseCase
from tests.fakes.fake_uow import FakeUnitOfWork


def test_update_system_settings_success(fake_uow: FakeUnitOfWork):
    request = UpdateSettingsRequestDTO(max_anonymous_invoice_amount=Decimal("2500.0"))
    use_case = UpdateSystemSettingsUseCase(uow=fake_uow)

    settings_id = use_case.execute(request)

    assert fake_uow.committed is True
    
    updated_settings = fake_uow.settings.get_by_id(settings_id)
    assert updated_settings is not None
    assert updated_settings.max_anonymous_invoice_amount.amount == Decimal("2500.0")
