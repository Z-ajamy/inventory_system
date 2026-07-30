from domain.entities.notebook import NoteBook


def test_notebook_creation():
    notebook = NoteBook(
        sku="NB-96-SQ",
        brand_id="mintra",
        page_numbers=96,
        type_id="squared"
    )
    assert notebook.page_numbers == 96
