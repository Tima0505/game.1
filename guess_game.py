import random


def generate_secret_number(min_val: int = 1, max_val: int = 100) -> int:
    """Генерирует случайное число в заданном диапазоне."""
    return random.randint(min_val, max_val)


def check_guess(secret: int, guess: int) -> str:
    """
    Сравнивает догадку с загаданным числом.
    Возвращает: 'equal', 'greater' или 'less'.
    """
    if guess == secret:
        return "equal"
    elif guess < secret:
        return "greater"  # загаданное больше
    else:
        return "less"     # загаданное меньше


def validate_guess(user_input: str) -> int:
    """
    Проверяет корректность ввода пользователя.
    Возвращает целое число или вызывает ValueError.
    """
    try:
        value = int(user_input.strip())
        return value
    except (ValueError, AttributeError):
        raise ValueError("Нужно ввести целое число!")


def play_game(secret: int = None, max_attempts: int = 10, input_func=input, print_func=print) -> bool:
    """
    Основная логика игры.
    Возвращает True, если игрок выиграл, иначе False.
    input_func и print_func можно подменить для тестирования.
    """
    if secret is None:
        secret = generate_secret_number()

    print_func("=== Игра «Угадай число» ===")
    print_func("Я загадал число от 1 до 100.")
    print_func(f"У тебя есть {max_attempts} попыток.\n")

    for move in range(1, max_attempts + 1):
        raw = input_func(f"Ход {move}/{max_attempts}. Твой вариант: ")
        try:
            guess = validate_guess(raw)
        except ValueError as e:
            print_func(str(e))
            continue

        result = check_guess(secret, guess)

        if result == "equal":
            print_func(f"\nПоздравляю! Ты угадал число {secret} за {move} ход(ов)!")
            return True
        elif result == "greater":
            print_func("Загаданное число БОЛЬШЕ")
        else:
            print_func("Загаданное число МЕНЬШЕ")

    print_func(f"\nПопытки закончились. Я загадал число {secret}.")
    return False


if __name__ == "__main__":
    play_game()
    input("\nНажми Enter, чтобы выйти...")