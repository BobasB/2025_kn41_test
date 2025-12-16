# Лабораторна робота №3: Тестування

## Опис роботи
Ця лабораторна робота присвячена тестуванню Python коду з використанням assert перевірок, unittest та PyTest.

## Структура файлів

### 1. Перевірка assert
- **assert_input.py** - демонстрація використання assert для перевірки введення даних з клавіатури
- **assert_figure.py** - демонстрація використання assert в класі Figure для валідації даних
- **assert_name.py** - демонстрація використання raise ValueError для валідації даних

### 2. Юніт тести (unittest)
- **app.py** - основний клас Figure з навмисною помилкою в методі get_figure_length
- **test_figure.py** - юніт тести для класу Figure

### 3. PyTest тести
- **test_figure_pytest.py** - тести з використанням бібліотеки PyTest
- **test_dice.py** - тести для класу Dice

### 4. Інші файли
- **dice.py** - клас Dice для демонстрації роботи з кубиками
- **pyproject.toml** - конфігурація проекту з залежностями
- **poetry.lock** - залежності проекту

## Запуск тестів

### Assert приклади
```bash
# Запуск прикладу з класом Figure
python assert_figure.py

# Запуск прикладу з класом Name
python assert_name.py
```

### Unittest тести
```bash
# Запуск через виконання файлу
python test_figure.py

# Запуск через unittest модуль
python -m unittest test_figure.py

# Запуск з детальним виводом
python -m unittest test_figure.py -v
```

### PyTest тести
```bash
# Запуск всіх тестів
poetry run pytest

# Запуск з детальним виводом
poetry run pytest -v

# Запуск конкретного файлу
poetry run pytest test_figure_pytest.py -v
```

## Очікувані результати

### Assert тести
При запуску assert_figure.py ви побачите результати різних тестових сценаріїв з помилками та успішними створеннями фігур.

### Unittest тести
При запуску test_figure.py деякі тести провалюються через навмисну помилку в app.py (метод get_figure_length повертає тип замість довжини).

### PyTest тести
При запуску test_figure_pytest.py аналогічно провалюється тест на перевірку довжини через помилку в app.py.

## Примітки
- Файл app.py містить навмисну помилку для демонстрації роботи тестів
- __pycache__ та .pytest_cache додані до .gitignore
- Використовується Poetry для управління залежностями
