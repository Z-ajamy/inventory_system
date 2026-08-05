from application.customer.dtos import UpdateCustomerRequestDTO
from application.exceptions.customer import CustomerNotFoundError
from domain.interfaces.uow import UnitOfWorkProtocol


class UpdateCustomerUseCase:
    def __init__(self, uow: UnitOfWorkProtocol):
        self.uow = uow

    def execute(self, request: UpdateCustomerRequestDTO) -> None:
        with self.uow as db:
            customer = db.customers.get_by_id(customer_id=request.customer_id)
            if not customer:
                raise CustomerNotFoundError(customer_id=request.customer_id)

            customer.name = request.name

            if request.phone is not None:
                customer.phone = str(request.phone).strip()

            db.customers.save(customer)
            db.commit()
