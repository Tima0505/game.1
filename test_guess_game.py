import pytest
from guess_game import (
    generate_secret_number,
    check_guess,
    validate_guess,
    play_game,
)




def test_generate_secret_number_in_range():
    """Проверяем, что число генерируется в правильном диапазоне."""
    for _ in range(50):
        num = generate_secret_number(1, 100)
        assert 1 <= num <= 100


def test_check_guess_equal():
    """Проверка: угадали число."""
    assert check_guess(50, 50) == "equal"


def test_check_guess_greater():
    """Проверка: загаданное число больше."""
    assert check_guess(50, 30) == "greater"


def test_check_guess_less():
    """Проверка: загаданное число меньше."""
    assert check_guess(50, 70) == "less"


def test_play_game_win_first_try():
    """Игрок угадывает с первой попытки."""
    inputs = iter(["42"])
    outputs = []

    def fake_input(prompt):
        return next(inputs)

    def fake_print(msg):
        outputs.append(msg)

    result = play_game(secret=42, max_attempts=10, input_func=fake_input, print_func=fake_print)
    assert result is True
    assert any("Поздравляю" in str(o) for o in outputs)


def test_play_game_win_on_third_try():
    """Игрок угадывает на третьей попытке."""
    inputs = iter(["10", "30", "42"])
    outputs = []

    def fake_input(prompt):
        return next(inputs)

    def fake_print(msg):
        outputs.append(msg)

    result = play_game(secret=42, max_attempts=10, input_func=fake_input, print_func=fake_print)
    assert result is True
    assert any("Поздравляю" in str(o) for o in outputs)


def test_play_game_lose():
    """Игрок не угадывает за отведённые попытки."""
    inputs = iter(["1", "2", "3"])
    outputs = []

    def fake_input(prompt):
        return next(inputs)

    def fake_print(msg):
        outputs.append(msg)

    result = play_game(secret=42, max_attempts=3, input_func=fake_input, print_func=fake_print)
    assert result is False
    assert any("Попытки закончились" in str(o) for o in outputs)




def test_validate_guess_correct():
    """Корректный ввод числа."""
    assert validate_guess("42") == 42
    assert validate_guess("  7  ") == 7
    assert validate_guess("-5") == -5


def test_validate_guess_empty_string():
    """Пустая строка должна вызывать ValueError."""
    with pytest.raises(ValueError, match="Нужно ввести целое число"):
        validate_guess("")


def test_validate_guess_letters():
    """Буквы вместо числа."""
    with pytest.raises(ValueError, match="Нужно ввести целое число"):
        validate_guess("abc")


def test_validate_guess_float():
    """Дробное число (не целое)."""
    with pytest.raises(ValueError, match="Нужно ввести целое число"):
        validate_guess("3.14")


def test_validate_guess_none():
    """None вместо строки."""
    with pytest.raises(ValueError, match="Нужно ввести целое число"):
        validate_guess(None)


def test_play_game_with_invalid_input_then_win():
    """Сначала некорректный ввод, потом правильный ответ."""
    inputs = iter(["abc", "hello", "42"])
    outputs = []

    def fake_input(prompt):
        return next(inputs)

    def fake_print(msg):
        outputs.append(msg)

    result = play_game(secret=42, max_attempts=5, input_func=fake_input, print_func=fake_print)
    assert result is True
  
    error_messages = [o for o in outputs if "Нужно ввести целое число" in str(o)]
    assert len(error_messages) == 2