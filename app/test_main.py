from app.main import is_isogram


def test_lettes_no_repeat() -> None:
    assert is_isogram("playgrounds") == True


def test_lettes_repeat() -> None:
    assert is_isogram("look") == False


def test_lettes_no_upper_and_lower() -> None:
    assert is_isogram("Adam") == False


def test_lettes_empty() -> None:
    assert is_isogram("") == True
