from dataclasses import dataclass
from decimal import Decimal

# --- Request DTOs ---
@dataclass(slots=True, frozen=True, kw_only=True)
class UpdateSettingsRequestDTO:
    max_anonymous_invoice_amount: Decimal

# --- Response DTOs ---
@dataclass(slots=True, frozen=True, kw_only=True)
class SettingsResponseDTO:
    id: str
    max_anonymous_invoice_amount: Decimal
