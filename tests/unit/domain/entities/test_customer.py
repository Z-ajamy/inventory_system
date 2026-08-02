import pytest

from domain.entities.customer import Customer
from domain.exceptions.shared import InvalidStringError


def test_customer_creation_with_all_data():
    cust = Customer(init_name="Ahmed Ali", phone="01012345678")
    assert cust.name == "Ahmed Ali"
    assert cust.phone == "01012345678"
    assert cust.id is not None


def test_customer_creation_without_phone():
    cust = Customer(init_name="Mohamed")
    assert cust.name == "Mohamed"
    assert cust.phone is None


def test_customer_empty_name_raises_error():
    with pytest.raises(InvalidStringError):
        Customer(init_name="   ")
