from decimal import Decimal

import pytest

from domain.entities.notebook import NoteBook
from domain.exceptions.notebook import InvalidPageCountError
from domain.shared.value_objects import Money


def test_notebook_creation():
    notebook = NoteBook(
        init_sku="NB-96-SQ",
        brand_id="mintra",
        init_page_count=96,
        init_type_id="squared",
        init_selling_price=Money(amount=Decimal("25.0")),
    )
    assert notebook.page_count == 96
    assert notebook.sku == "NB-96-SQ"
    assert notebook.selling_price.amount == Decimal("25.0")


def test_notebook_invalid_page_count_raises_error():
    with pytest.raises(InvalidPageCountError):
        NoteBook(
            init_sku="NB-BAD",
            brand_id="mintra",
            init_page_count=0,
            init_type_id="squared",
            init_selling_price=Money(amount=Decimal("25.0")),
        )
