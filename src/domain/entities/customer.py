from dataclasses import dataclass, field

from domain.shared.utils import create_uuid4


@dataclass(slots=True, kw_only=True)
class Customer:
    id: str = field(default_factory=create_uuid4)
    name: str
    phone: str | None = None
