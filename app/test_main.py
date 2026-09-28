from app.main import is_isogram


def test_letters_no_repeat() -> None:
    assert is_isogram("playgrounds") == True


def test_letters_repeat() -> None:
    assert is_isogram("look") == False


def test_letters_no_upper_and_lower() -> None:
    assert is_isogram("Adam") == False


def test_letters_empty() -> None:
    assert is_isogram("") == True

