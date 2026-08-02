from dataclasses import InitVar, dataclass, field

from domain.exceptions.shared import InvalidStringError
from domain.shared.utils import create_uuid4


@dataclass(slots=True, kw_only=True)
class Customer:
    id: str = field(default_factory=create_uuid4)

    init_name: InitVar[str]
    _name: str = field(init=False)

    phone: str | None = None

    def __post_init__(self, init_name: str):
        self.name = init_name
        if self.phone is not None:
            self.phone = str(self.phone).strip()

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value or not str(value).strip():
            raise InvalidStringError(field_name="name")
        self._name = str(value).strip()
