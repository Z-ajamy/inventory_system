import pytest

from application.reference_data.create_reference_data import CreateReferenceDataUseCase
from application.reference_data.dtos import CreateInfoRequestDTO
from domain.shared.base import InfoCategory
from tests.fakes.fake_uow import FakeUnitOfWork


def test_create_reference_data_success(fake_uow: FakeUnitOfWork):
    request = CreateInfoRequestDTO(name="Red", category=InfoCategory.PEN_COLOR)
    use_case = CreateReferenceDataUseCase(uow=fake_uow)

    info_id = use_case.execute(request)

    assert fake_uow.committed is True
    
    saved_info = fake_uow.reference_data.get_by_id(info_id)
    assert saved_info is not None
    assert saved_info.name == "Red"
    assert saved_info.category == InfoCategory.PEN_COLOR
