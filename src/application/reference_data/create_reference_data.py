from application.reference_data.dtos import CreateInfoRequestDTO
from domain.interfaces.uow import UnitOfWorkProtocol
from domain.shared.base import Info


class CreateReferenceDataUseCase:
    def __init__(self, uow: UnitOfWorkProtocol):
        self.uow = uow

    def execute(self, request: CreateInfoRequestDTO) -> str:
        with self.uow as db:
            info = Info(
                init_name=request.name,
                category=request.category
            )
            
            db.reference_data.save(info)
            db.commit()

            return info.id
