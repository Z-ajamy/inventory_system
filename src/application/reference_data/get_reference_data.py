from application.reference_data.dtos import InfoResponseDTO
from domain.interfaces.uow import UnitOfWorkProtocol
from domain.shared.base import InfoCategory


class GetReferenceDataByCategoryUseCase:
    def __init__(self, uow: UnitOfWorkProtocol):
        self.uow = uow

    def execute(self, category: InfoCategory) -> tuple[InfoResponseDTO, ...]:
        with self.uow as db:
            items = db.reference_data.get_by_category(category=category)

            return tuple(
                InfoResponseDTO(id=item.id, name=item.name, category=item.category)
                for item in items
            )
