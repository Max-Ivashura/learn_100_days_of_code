# Test Debugging

def divide_numbers(num1, num2):
    """Делит num1 на num2 и обрабатывает ошибки."""
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль!")
        return None
    except TypeError:
        print("Ошибка: Ожидалось число, получено что-то другое!")
        return None
    else:
        print(f"Результат: {result}")
        return result

def main():
    print("Тест деления двух чисел:")

    # Тесты
    test_cases = [
        (10, 2),   # Ожидаемый результат: 5.0
        (10, 0),   # Ожидаемая ошибка: Деление на ноль!
        (10, "a"), # Ожидаемая ошибка: Ожидалось число
    ]

    for num1, num2 in test_cases:
        print(f"Делим {num1} на {num2}:")
        divide_numbers(num1, num2)

if __name__ == "__main__":
    main()
