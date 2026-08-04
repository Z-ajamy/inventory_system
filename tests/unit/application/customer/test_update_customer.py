import pytest

from application.customer.dtos import UpdateCustomerRequestDTO
from application.customer.update_customer import UpdateCustomerUseCase
from application.exceptions.customer import CustomerNotFoundError
from domain.entities.customer import Customer
from tests.fakes.fake_uow import FakeUnitOfWork


def test_update_customer_success(fake_uow: FakeUnitOfWork):
    customer = Customer(init_name="Old Name", phone="000-000")
    fake_uow.customers.save(customer)

    request = UpdateCustomerRequestDTO(
        customer_id=customer.id, 
        name="New Name", 
        phone="111-111"
    )
    use_case = UpdateCustomerUseCase(uow=fake_uow)

    use_case.execute(request)

    assert fake_uow.committed is True
    
    updated_customer = fake_uow.customers.get_by_id(customer.id)
    assert updated_customer.name == "New Name"
    assert updated_customer.phone == "111-111"


def test_update_customer_raises_not_found(fake_uow: FakeUnitOfWork):
    request = UpdateCustomerRequestDTO(
        customer_id="invalid-id", 
        name="New Name"
    )
    use_case = UpdateCustomerUseCase(uow=fake_uow)

    with pytest.raises(CustomerNotFoundError):
        use_case.execute(request)
