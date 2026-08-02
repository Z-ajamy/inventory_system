from application.exceptions.create_invoice import (
    ProductNotFoundError,
    QuantityIsLessThanOrderError,
)
from application.invoice.dtos import CreateInvoiceRequestDTO
from domain.entities.invoice.draft_invoice import DraftInvoice
from domain.interfaces.uow import UnitOfWorkProtocol


class CreateInvoiceUseCase:
    def __init__(self, uow: UnitOfWorkProtocol):
        self.uow = uow

    def execute(self, request: CreateInvoiceRequestDTO) -> str:
        with self.uow as db:
            settings = db.settings.get_current_setting()

            draft = DraftInvoice(customer_id=request.customer_id)
            for item in request.invoice_items:
                product = db.products.get_by_id(product_id=item.product_id)
                if not product:
                    raise ProductNotFoundError(product_id=item.product_id)

                current_quantity = db.batches.get_total_quantity_for_product(
                    product_id=product.id
                )
                num: int = item.num_of_items
                if num > current_quantity:
                    raise QuantityIsLessThanOrderError(
                        product_id=product.id, current_quantity=current_quantity
                    )

                batches = db.batches.get_available_for_product(product_id=product.id)

                for batch in batches:
                    if num <= 0:
                        break

                    qty_to_take = min(num, batch.current_quantity)

                    draft.add_item(
                        batch=batch,
                        quantity=qty_to_take,
                        selling_price=product.selling_price,
                    )

                    batch.sell_items(qty_to_take)
                    db.batches.save(stock_batch=batch)

                    num -= qty_to_take

            invoice = draft.finalize(
                anonymous_limit=settings.max_anonymous_invoice_amount
            )
            db.invoices.save(invoice=invoice)
            db.commit()

            return invoice.id
