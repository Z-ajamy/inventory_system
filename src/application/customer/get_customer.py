from application.customer.dtos import CustomerResponseDTO
from application.exceptions.customer import CustomerNotFoundError
from domain.interfaces.uow import UnitOfWorkProtocol


class GetCustomerUseCase:
    def __init__(self, uow: UnitOfWorkProtocol):
        self.uow = uow

    def execute(self, customer_id: str) -> CustomerResponseDTO:
        with self.uow as db:
            customer = db.customers.get_by_id(customer_id=customer_id)
            if not customer:
                raise CustomerNotFoundError(customer_id=customer_id)

            return CustomerResponseDTO(
                id=customer.id,
                name=customer.name,
                phone=customer.phone
            )
