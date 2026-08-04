from application.customer.dtos import RegisterCustomerRequestDTO
from domain.entities.customer import Customer
from domain.interfaces.uow import UnitOfWorkProtocol


class RegisterCustomerUseCase:
    def __init__(self, uow: UnitOfWorkProtocol):
        self.uow = uow

    def execute(self, request: RegisterCustomerRequestDTO) -> str:
        with self.uow as db:
            customer = Customer(
                init_name=request.name,
                phone=request.phone
            )
            
            db.customers.save(customer)
            db.commit()

            return customer.id
