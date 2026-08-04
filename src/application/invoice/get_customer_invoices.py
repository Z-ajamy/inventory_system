from application.invoice.dtos import InvoiceItemResponseDTO, InvoiceResponseDTO
from domain.interfaces.uow import UnitOfWorkProtocol


class GetCustomerInvoicesUseCase:
    def __init__(self, uow: UnitOfWorkProtocol):
        self.uow = uow

    def execute(self, customer_id: str) -> tuple[InvoiceResponseDTO, ...]:
        with self.uow as db:
            invoices = db.invoices.get_by_customer_id(customer_id=customer_id)

            response_list = []
            for invoice in invoices:
                items_dto = tuple(
                    InvoiceItemResponseDTO(
                        product_id=item.product_id,
                        num_of_items=item.num_of_items,
                        total_price=item.price,
                    )
                    for item in invoice.items
                )

                response_list.append(
                    InvoiceResponseDTO(
                        id=invoice.id,
                        customer_id=invoice.customer_id,
                        items=items_dto,
                        date=invoice.date,
                        total_price=invoice.total_price,
                        items_count=invoice.items_count,
                    )
                )

            return tuple(response_list)
