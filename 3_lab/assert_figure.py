"""
Приклад використання assert в класі Figure для валідації даних
"""

class Figure:
    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in ["квадрат", "прямокутник", "трикутник"], "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length
    
    def __str__(self):
        return f"Фігура: {self.type}, довжина: {self.length}"


if __name__ == "__main__":
    print("=== Тестування класу Figure ===\n")
    
    # Тест 1: Спроба створити фігуру з недозволеним типом
    print("Тест 1: Спроба створити трапецію")
    try:
        a = Figure("трапеція", 12)
        print(f"Створено: {a}")
    except AssertionError as e:
        print(f"Помилка: {e}\n")
    
    # Тест 2: Спроба створити фігуру з некоректною довжиною
    print("Тест 2: Спроба створити квадрат з довжиною 0")
    try:
        b = Figure("квадрат", 0)
        print(f"Створено: {b}")
    except AssertionError as e:
        print(f"Помилка: {e}\n")
    
    # Тест 3: Спроба створити фігуру з від'ємною довжиною
    print("Тест 3: Спроба створити прямокутник з від'ємною довжиною")
    try:
        d = Figure("прямокутник", -5)
        print(f"Створено: {d}")
    except AssertionError as e:
        print(f"Помилка: {e}\n")
    
    # Тест 4: Успішне створення фігури
    print("Тест 4: Створення коректного квадрата")
    try:
        c = Figure("квадрат", 10)
        print(f"Створено: {c}\n")
    except AssertionError as e:
        print(f"Помилка: {e}\n")
    
    # Тест 5: Створення трикутника
    print("Тест 5: Створення трикутника")
    try:
        e = Figure("трикутник", 15)
        print(f"Створено: {e}\n")
    except AssertionError as e:
        print(f"Помилка: {e}\n")
