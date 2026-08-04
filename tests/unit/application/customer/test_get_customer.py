import pytest

from application.customer.get_customer import GetCustomerUseCase
from application.exceptions.customer import CustomerNotFoundError
from domain.entities.customer import Customer
from tests.fakes.fake_uow import FakeUnitOfWork


def test_get_customer_success(fake_uow: FakeUnitOfWork):
    customer = Customer(init_name="Alice Smith", phone="555-1234")
    fake_uow.customers.save(customer)

    use_case = GetCustomerUseCase(uow=fake_uow)

    result = use_case.execute(customer_id=customer.id)

    assert result.id == customer.id
    assert result.name == "Alice Smith"
    assert result.phone == "555-1234"


def test_get_customer_raises_not_found(fake_uow: FakeUnitOfWork):
    use_case = GetCustomerUseCase(uow=fake_uow)

    with pytest.raises(CustomerNotFoundError):
        use_case.execute(customer_id="invalid-id")
