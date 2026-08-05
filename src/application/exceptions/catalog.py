from domain.exceptions.base import EntitiesBaseError


class DuplicateSkuError(EntitiesBaseError):
    def __init__(self, sku: str):
        super().__init__(
            message=f"Product with SKU '{sku}' already exists.",
            code="DUPLICATE_SKU",
            context={"sku": sku},
        )


class ReferenceNotFoundError(EntitiesBaseError):
    def __init__(self, ref_type: str, ref_id: str):
        super().__init__(
            message=f"Reference data '{ref_type}' with id '{ref_id}' not found.",
            code="REFERENCE_NOT_FOUND",
            context={"ref_type": ref_type, "ref_id": ref_id},
        )


class ProductNotFoundError(EntitiesBaseError):
    def __init__(self, product_id: str):
        super().__init__(
            message=f"Product with id '{product_id}' not found.",
            code="PRODUCT_NOT_FOUND",
            context={"product_id": product_id},
        )
