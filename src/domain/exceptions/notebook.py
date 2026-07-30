from domain.exceptions.base import EntitiesBaseError

class InvalidPageCountError(EntitiesBaseError):
    def __init__(self, page_count: int):
        super().__init__(
            message=f"Notebook page count must be greater than zero. Got: {page_count}",
            code="INVALID_PAGE_COUNT",
            context={"page_count": page_count}
        )
