import pytest

from application.customer.dtos import RegisterCustomerRequestDTO
from application.customer.register_customer import RegisterCustomerUseCase
from domain.exceptions.shared import InvalidStringError
from tests.fakes.fake_uow import FakeUnitOfWork


def test_register_customer_success(fake_uow: FakeUnitOfWork):
    request = RegisterCustomerRequestDTO(name="John Doe", phone="1234567890")
    use_case = RegisterCustomerUseCase(uow=fake_uow)

    customer_id = use_case.execute(request)

    assert fake_uow.committed is True
    
    saved_customer = fake_uow.customers.get_by_id(customer_id)
    assert saved_customer is not None
    assert saved_customer.name == "John Doe"
    assert saved_customer.phone == "1234567890"


def test_register_customer_raises_invalid_string_error(fake_uow: FakeUnitOfWork):
    request = RegisterCustomerRequestDTO(name="   ", phone="1234567890")
    use_case = RegisterCustomerUseCase(uow=fake_uow)

    with pytest.raises(InvalidStringError):
        use_case.execute(request)
