from dataclasses import dataclass, field
from enum import auto

from domain.shared.utils import create_uuid4
from domain.shared.value_objects import Money, OldStrEnum


class SettingStatus(OldStrEnum):
    CURRENT = auto()
    ARCHIVED = auto()


@dataclass(slots=True, frozen=True, kw_only=True)
class SystemSettings:
    id: str = field(default_factory=create_uuid4)
    max_anonymous_invoice_amount: Money
    status: SettingStatus = field(default=SettingStatus.CURRENT)
