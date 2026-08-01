from typing import Protocol

from domain.shared.base import Info, InfoCategory


class ReferenceDataRepositoryProtocol(Protocol):
    def save(self, info: Info) -> None: ...

    def get_by_id(self, info_id: str) -> Info | None: ...

    def get_by_category(self, category: InfoCategory) -> tuple[Info, ...]: ...
