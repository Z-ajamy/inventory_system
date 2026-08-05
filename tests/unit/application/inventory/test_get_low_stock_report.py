from decimal import Decimal

from application.inventory.get_low_stock_report import GetLowStockReportUseCase
from domain.entities.stock_batch import StockBatch
from domain.shared.value_objects import Money
from tests.fakes.fake_uow import FakeUnitOfWork


def test_get_low_stock_report_success(fake_uow: FakeUnitOfWork):
    batch_1 = StockBatch(
        init_product_id="prod-1",
        init_init_quantity=50,
        init_current_quantity=5,
        unit_cost=Money(amount=Decimal("10.0")),
    )
    batch_2 = StockBatch(
        init_product_id="prod-2",
        init_init_quantity=20,
        init_current_quantity=2,
        unit_cost=Money(amount=Decimal("15.0")),
    )
    batch_3 = StockBatch(
        init_product_id="prod-3",
        init_init_quantity=100,
        init_current_quantity=100,
        unit_cost=Money(amount=Decimal("5.0")),
    )

    fake_uow.batches.save(batch_1)
    fake_uow.batches.save(batch_2)
    fake_uow.batches.save(batch_3)

    use_case = GetLowStockReportUseCase(uow=fake_uow)

    report = use_case.execute(threshold_quantity=10)

    assert len(report) == 2

    returned_batch_ids = [item.batch_id for item in report]
    assert batch_1.id in returned_batch_ids
    assert batch_2.id in returned_batch_ids
    assert batch_3.id not in returned_batch_ids
