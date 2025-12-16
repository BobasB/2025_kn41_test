"""
Приклад використання raise ValueError для валідації даних
"""

class Name:
    def __init__(self, name, hobby=None) -> None:
        # Перевірка імені
        if name not in ["Богдан", "Анонім", "Олександр"]:
            raise ValueError("Дозволені імена: Богдан, Анонім, Олександр")
        
        # Перевірка що хоббі не пусте
        if hobby is not None and (not hobby or hobby.strip() == ""):
            raise ValueError("Хоббі не може бути пустим!")
        
        self.name = name
        self.hobby = hobby if hobby else "Не вказано"
    
    def __str__(self):
        return f"Ім'я: {self.name}, Хоббі: {self.hobby}"


if __name__ == "__main__":
    print("=== Тестування класу Name ===\n")
    
    # Тест 1: Спроба створити об'єкт з недозволеним ім'ям
    print("Тест 1: Спроба створити об'єкт з ім'ям 'Бодько'")
    try:
        a = Name("Бодько")
        print(f"Створено: {a}")
    except ValueError as e:
        print(f"Помилка: {e}\n")
    
    # Тест 2: Створення об'єкта з дозволеним ім'ям без хоббі
    print("Тест 2: Створення об'єкта з ім'ям 'Богдан' без хоббі")
    try:
        b = Name("Богдан")
        print(f"Створено: {b}\n")
    except ValueError as e:
        print(f"Помилка: {e}\n")
    
    # Тест 3: Створення об'єкта з власним ім'ям та хоббі
    print("Тест 3: Створення об'єкта з ім'ям 'Олександр' та хоббі 'Програмування'")
    try:
        c = Name("Олександр", "Програмування")
        print(f"Створено: {c}\n")
    except ValueError as e:
        print(f"Помилка: {e}\n")
    
    # Тест 4: Спроба створити об'єкт з пустим хоббі
    print("Тест 4: Спроба створити об'єкт з пустим хоббі")
    try:
        d = Name("Анонім", "")
        print(f"Створено: {d}")
    except ValueError as e:
        print(f"Помилка: {e}\n")
    
    # Тест 5: Спроба створити об'єкт з хоббі з пробілів
    print("Тест 5: Спроба створити об'єкт з хоббі з тільки пробілів")
    try:
        e = Name("Богдан", "   ")
        print(f"Створено: {e}")
    except ValueError as e:
        print(f"Помилка: {e}\n")
    
    # Тест 6: Успішне створення з коректним хоббі
    print("Тест 6: Створення об'єкта з ім'ям 'Анонім' та хоббі 'Читання'")
    try:
        f = Name("Анонім", "Читання")
        print(f"Створено: {f}\n")
    except ValueError as e:
        print(f"Помилка: {e}\n")
