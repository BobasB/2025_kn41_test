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
- **test_figure.py** - юніт тести для класу Figure (8 тестів)
- **dice.py** - клас Dice для роботи з кубиками
- **test_dice.py** - юніт тести для класу Dice (3 тести)

### 3. PyTest тести
- **test_figure_pytest.py** - тести для класу Figure з використанням PyTest (21 тест)
- **test_dice_pytest.py** - тести для класу Dice з використанням PyTest (14 тестів)

### 4. Документація
- **README.md** - цей файл з інструкціями
- **REPORT.md** - детальний звіт про виконання лабораторної роботи
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
# Запуск окремих тестових файлів
python -m unittest test_figure.py -v
python -m unittest test_dice.py -v

# Запуск всіх unittest тестів
python -m unittest discover -v
```

### PyTest тести
```bash
# Запуск всіх тестів
python -m pytest

# Запуск з детальним виводом
python -m pytest -v

# Запуск конкретного файлу
python -m pytest test_figure_pytest.py -v
python -m pytest test_dice_pytest.py -v

# Запуск з виводом print
python -m pytest -v -s
```

## Очікувані результати

### Assert тести
При запуску assert_figure.py та assert_name.py ви побачите результати різних тестових сценаріїв з помилками та успішними створеннями об'єктів.

### Unittest тести
- **test_dice.py**: Всі 3 тести проходять успішно ✅
- **test_figure.py**: 7 з 8 тестів проходять, 1 провалюється через навмисну помилку в app.py ❌

### PyTest тести
- **test_dice_pytest.py**: Всі 14 тестів проходять успішно ✅
- **test_figure_pytest.py**: 20 з 21 тесту проходять, 1 провалюється через навмисну помилку в app.py ❌

**Загальна статистика PyTest**: 44 passed, 2 failed, 1 warning

## Примітки
- Файл app.py містить навмисну помилку (метод get_figure_length повертає type замість length) для демонстрації роботи тестів
- __pycache__ та .pytest_cache додані до .gitignore
- Використовується Poetry для управління залежностями (або pip якщо Poetry недоступний)

## Виконані завдання

✅ Створено приклади використання assert  
✅ Створено класи з валідацією даних (Figure, Name)  
✅ Додано власне ім'я та додатковий параметр (хоббі) до класу Name  
✅ Створено юніт тести з використанням unittest  
✅ Виправлено тест в test_dice.py (було self.assertTrue(False))  
✅ Додано __pycache__ до .gitignore  
✅ Розширено функціонал класу Figure (методи calculate_perimeter, calculate_area)  
✅ Встановлено PyTest  
✅ Створено тести з використанням PyTest  
✅ Використано параметризацію (@pytest.mark.parametrize) та фікстури (@pytest.fixture)  
✅ Створено детальний звіт про виконання роботи (REPORT.md)  

**Всі завдання лабораторної роботи №3 виконано успішно!** ✨

