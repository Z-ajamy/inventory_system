from application.exceptions.get_invoice import InvoiceNotFoundError
from application.invoice.dtos import InvoiceItemResponseDTO, InvoiceResponseDTO
from domain.interfaces.uow import UnitOfWorkProtocol


class GetInvoiceUseCase:
    def __init__(self, uow: UnitOfWorkProtocol):
        self.uow = uow

    def execute(self, invoice_id: str) -> InvoiceResponseDTO:
        with self.uow as db:
            invoice = db.invoices.get_by_id(invoice_id=invoice_id)

            if not invoice:
                raise InvoiceNotFoundError(invoice_id=invoice_id)

            items_dto = tuple(
                InvoiceItemResponseDTO(
                    product_id=item.product_id,
                    num_of_items=item.num_of_items,
                    total_price=item.price,
                )
                for item in invoice.items
            )

            return InvoiceResponseDTO(
                id=invoice.id,
                customer_id=invoice.customer_id,
                items=items_dto,
                date=invoice.date,
                total_price=invoice.total_price,
                items_count=invoice.items_count,
            )
