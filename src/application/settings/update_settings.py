from decimal import Decimal

from application.settings.dtos import UpdateSettingsRequestDTO
from domain.entities.settings import SystemSettings
from domain.interfaces.uow import UnitOfWorkProtocol
from domain.shared.value_objects import Money


class UpdateSystemSettingsUseCase:
    def __init__(self, uow: UnitOfWorkProtocol):
        self.uow = uow

    def execute(self, request: UpdateSettingsRequestDTO) -> str:
        with self.uow as db:
            new_settings = SystemSettings(
                max_anonymous_invoice_amount=Money(
                    amount=Decimal(str(request.max_anonymous_invoice_amount))
                )
            )

            db.settings.save(new_settings)
            db.commit()

            return new_settings.id
