from app.main import is_isogram

def lettes_no_repeat() -> None:
    assert is_isogram("playgrounds") == True

def lettes_repeat() -> None:
    assert is_isogram("look") == False

def lettes_no_upper_and_lower() -> None:
    assert is_isogram("Adam") == False

def lettes_empty() -> None:
    assert is_isogram("") == True


