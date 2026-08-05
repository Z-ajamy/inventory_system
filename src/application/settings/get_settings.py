from application.settings.dtos import SettingsResponseDTO
from domain.interfaces.uow import UnitOfWorkProtocol


class GetCurrentSettingsUseCase:
    def __init__(self, uow: UnitOfWorkProtocol):
        self.uow = uow

    def execute(self) -> SettingsResponseDTO:
        with self.uow as db:
            current_settings = db.settings.get_current_setting()

            return SettingsResponseDTO(
                id=current_settings.id,
                max_anonymous_invoice_amount=current_settings.max_anonymous_invoice_amount.amount,
            )
