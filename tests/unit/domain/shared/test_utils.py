from domain.shared.utils import create_uuid4


def test_create_uuid4_returns_valid_string():
    uuid_str = create_uuid4()
    assert isinstance(uuid_str, str)
    assert len(uuid_str) == 32  # hex format without dashes


def test_create_uuid4_is_unique():
    uuid1 = create_uuid4()
    uuid2 = create_uuid4()
    assert uuid1 != uuid2
