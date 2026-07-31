from domain.entities.customer import Customer


def test_customer_creation_with_all_data():
    cust = Customer(name="Ahmed Ali", phone="01012345678")
    assert cust.name == "Ahmed Ali"
    assert cust.phone == "01012345678"
    assert cust.id is not None


def test_customer_creation_without_phone():
    cust = Customer(name="Mohamed")
    assert cust.name == "Mohamed"
    assert cust.phone is None
