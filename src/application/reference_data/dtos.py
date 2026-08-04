from dataclasses import dataclass
from domain.shared.base import InfoCategory

@dataclass(slots=True, frozen=True, kw_only=True)
class CreateInfoRequestDTO:
    name: str
    category: InfoCategory

@dataclass(slots=True, frozen=True, kw_only=True)
class InfoResponseDTO:
    id: str
    name: str
    category: InfoCategory
