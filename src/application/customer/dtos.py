from dataclasses import dataclass


@dataclass(slots=True, frozen=True, kw_only=True)
class RegisterCustomerRequestDTO:
    name: str
    phone: str | None = None


@dataclass(slots=True, frozen=True, kw_only=True)
class UpdateCustomerRequestDTO:
    customer_id: str
    name: str
    phone: str | None = None


@dataclass(slots=True, frozen=True, kw_only=True)
class CustomerResponseDTO:
    id: str
    name: str
    phone: str | None
