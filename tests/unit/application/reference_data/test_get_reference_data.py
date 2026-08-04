import pytest

from application.reference_data.get_reference_data import GetReferenceDataByCategoryUseCase
from domain.shared.base import Info, InfoCategory
from tests.fakes.fake_uow import FakeUnitOfWork


def test_get_reference_data_by_category_success(fake_uow: FakeUnitOfWork):
    info1 = Info(init_name="Red", category=InfoCategory.PEN_COLOR)
    info2 = Info(init_name="Blue", category=InfoCategory.PEN_COLOR)
    info3 = Info(init_name="Ballpoint", category=InfoCategory.PEN_TYPE)
    
    fake_uow.reference_data.save(info1)
    fake_uow.reference_data.save(info2)
    fake_uow.reference_data.save(info3)

    use_case = GetReferenceDataByCategoryUseCase(uow=fake_uow)

    results = use_case.execute(category=InfoCategory.PEN_COLOR)

    assert len(results) == 2
    
    returned_names = [r.name for r in results]
    assert "Red" in returned_names
    assert "Blue" in returned_names
    assert "Ballpoint" not in returned_names
