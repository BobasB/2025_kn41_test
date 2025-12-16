# Звіт про виконання лабораторної роботи №3

## 1. Перевірка assert

### 1.1 Файл: assert_figure.py
Демонструє використання assert в класі для валідації параметрів.

**Результати виконання:**
```
=== Тестування класу Figure ===

Тест 1: Спроба створити трапецію
Помилка: Дозволені фігури: квадрат, прямокутник, трикутник

Тест 2: Спроба створити квадрат з довжиною 0
Помилка: Довжина має бути більшою за 0!

Тест 3: Спроба створити прямокутник з від'ємною довжиною
Помилка: Довжина має бути більшою за 0!

Тест 4: Створення коректного квадрата
Створено: Фігура: квадрат, довжина: 10

Тест 5: Створення трикутника
Створено: Фігура: трикутник, довжина: 15
```

**Висновок:** Assert правильно перевіряє:
- Тип фігури (дозволені тільки квадрат, прямокутник, трикутник)
- Довжину (має бути > 0)

### 1.2 Файл: assert_name.py
Демонструє використання raise ValueError для валідації даних.

**Результати виконання:**
```
=== Тестування класу Name ===

Тест 1: Спроба створити об'єкт з ім'ям 'Бодько'
Помилка: Дозволені імена: Богдан, Анонім, Олександр

Тест 2: Створення об'єкта з ім'ям 'Богдан' без хоббі
Створено: Ім'я: Богдан, Хоббі: Не вказано

Тест 3: Створення об'єкта з ім'ям 'Олександр' та хоббі 'Програмування'
Створено: Ім'я: Олександр, Хоббі: Програмування

Тест 4: Спроба створити об'єкт з пустим хоббі
Помилка: Хоббі не може бути пустим!

Тест 5: Спроба створити об'єкт з хоббі з тільки пробілів
Помилка: Хоббі не може бути пустим!

Тест 6: Створення об'єкта з ім'ям 'Анонім' та хоббі 'Читання'
Створено: Ім'я: Анонім, Хоббі: Читання
```

**Висновок:** ValueError правильно перевіряє:
- Дозволені імена (Богдан, Анонім, Олександр)
- Поле хоббі не може бути пустим або містити тільки пробіли

### 1.3 Файл: app.py (демонстрація)
Показує роботу класу Figure з навмисною помилкою.

**Результати виконання:**
```
=== Тестування класу Figure ===

Створено: Figure(type=квадрат, length=5)
Тип: квадрат
Довжина (має бути помилка!): квадрат  ← ПОМИЛКА: повертає тип замість довжини!
Периметр: 20
Площа: 25
```

**Висновок:** Видно, що метод get_figure_length повертає тип фігури замість довжини - це навмисна помилка для демонстрації роботи тестів.

---

## 2. Юніт тести (unittest)

### Файл: test_figure.py
Містить 8 тестів для перевірки класу Figure.

**Результати виконання:**
```
python -m unittest test_figure.py -v

==================================================
Початок тестування класу Figure
==================================================
test_area_calculation ... ok
test_figure_length ... FAIL  ← Провалився через помилку в app.py
test_figure_type ... ok
test_negative_length ... ok
test_obj ... ok
test_perimeter_calculation ... ok
test_string_representation ... ok
test_zero_length ... ok

======================================================================
FAIL: test_figure_length
Перевіряємо, що властивість get_figure_length повертає правильну довжину
----------------------------------------------------------------------
AssertionError: 9 != 'прямокутник' : Властивість get_figure_length повертає непривильну довжину!

----------------------------------------------------------------------
Ran 8 tests in 0.001s

FAILED (failures=1)
```

**Статистика тестів:**
- ✅ Успішних: 7
- ❌ Провалених: 1 (test_figure_length - через навмисну помилку)

**Висновок:** Тести успішно виявляють помилку в методі get_figure_length.

---

## 3. PyTest тести

### Файл: test_figure_pytest.py
Містить 21 тест з використанням PyTest, включаючи параметризовані тести та фікстури.

**Результати виконання:**
```
python -m pytest test_figure_pytest.py -v

================================================= test session starts ==================================================
collected 21 items

test_figure_pytest.py::TestFigureWithPytest::test_figure_creation PASSED                    [  4%]
test_figure_pytest.py::TestFigureWithPytest::test_figure_type_property PASSED               [  9%]
test_figure_pytest.py::TestFigureWithPytest::test_figure_length_property FAILED             [ 14%] ← ПОМИЛКА
test_figure_pytest.py::TestFigureWithPytest::test_valid_figures[квадрат-5] PASSED          [ 19%]
test_figure_pytest.py::TestFigureWithPytest::test_valid_figures[прямокутник-10] PASSED     [ 23%]
test_figure_pytest.py::TestFigureWithPytest::test_valid_figures[трикутник-8] PASSED        [ 28%]
test_figure_pytest.py::TestFigureWithPytest::test_invalid_figure_types[коло-5] PASSED      [ 33%]
test_figure_pytest.py::TestFigureWithPytest::test_invalid_figure_types[ромб-10] PASSED     [ 38%]
test_figure_pytest.py::TestFigureWithPytest::test_invalid_figure_types[трапеція-8] PASSED  [ 42%]
test_figure_pytest.py::TestFigureWithPytest::test_invalid_lengths[0] PASSED                [ 47%]
test_figure_pytest.py::TestFigureWithPytest::test_invalid_lengths[-1] PASSED               [ 52%]
test_figure_pytest.py::TestFigureWithPytest::test_invalid_lengths[-10] PASSED              [ 57%]
test_figure_pytest.py::TestFigureWithPytest::test_square_perimeter PASSED                  [ 61%]
test_figure_pytest.py::TestFigureWithPytest::test_rectangle_perimeter PASSED               [ 66%]
test_figure_pytest.py::TestFigureWithPytest::test_triangle_perimeter PASSED                [ 71%]
test_figure_pytest.py::TestFigureWithPytest::test_square_area PASSED                       [ 76%]
test_figure_pytest.py::TestFigureWithPytest::test_triangle_area PASSED                     [ 80%]
test_figure_pytest.py::TestFigureWithPytest::test_string_representation PASSED             [ 85%]
test_figure_pytest.py::test_with_fixture_square PASSED                                     [ 90%]
test_figure_pytest.py::test_with_fixture_triangle PASSED                                   [ 95%]
test_figure_pytest.py::test_multiple_figures_creation PASSED                               [100%]

======================================================= FAILURES =======================================================
___________________________________ TestFigureWithPytest.test_figure_length_property ___________________________________

AssertionError: get_figure_length має повертати довжину, а не тип!
assert 'прямокутник' == 7

=============================================== short test summary info ================================================
FAILED test_figure_pytest.py::TestFigureWithPytest::test_figure_length_property
======================================= 1 failed, 20 passed, 1 warning in 0.08s ========================================
```

**Статистика тестів:**
- ✅ Успішних: 20
- ❌ Провалених: 1 (test_figure_length_property - через навмисну помилку)
- ⚠️ Попереджень: 1 (незареєстрований маркер "slow")

**Особливості PyTest тестів:**
- Використання параметризації (@pytest.mark.parametrize) для тестування різних комбінацій даних
- Використання фікстур (@pytest.fixture) для підготовки тестових даних
- Використання маркерів (@pytest.mark.slow) для позначення повільних тестів
- Більш лаконічний синтаксис порівняно з unittest

---

## 4. Порівняння unittest та PyTest

| Характеристика | unittest | PyTest |
|----------------|----------|--------|
| Синтаксис | self.assertEqual() | assert == |
| Фікстури | setUp/tearDown методи | @pytest.fixture декоратор |
| Параметризація | Потрібно писати циклами | @pytest.mark.parametrize |
| Виконання | python -m unittest | pytest або python -m pytest |
| Вивід | Менш детальний | Більш детальний та зрозумілий |
| Стандартна бібліотека | Так | Ні (потрібно встановлювати) |

---

## 5. Висновки

1. **Assert перевірки** є простим та ефективним способом валідації даних на етапі виконання програми.

2. **unittest** - стандартна бібліотека Python для юніт-тестування, яка надає повний набір інструментів для створення тестів.

3. **PyTest** - більш сучасна та зручна бібліотека з лаконічним синтаксом, параметризацією та потужними фікстурами.

4. Обидві бібліотеки успішно виявили навмисну помилку в методі `get_figure_length` класу `Figure`.

5. Тестування допомагає:
   - Виявляти помилки на ранніх етапах розробки
   - Забезпечувати правильність роботи коду
   - Документувати очікувану поведінку програми
   - Спрощувати рефакторинг коду

---

## 6. Виконані завдання

✅ Створено приклади використання assert (assert_input.py, assert_figure.py, assert_name.py)  
✅ Створено клас з валідацією даних через assert (Figure)  
✅ Створено клас з валідацією через raise ValueError (Name)  
✅ Додано власне ім'я та додатковий параметр (хоббі) до класу Name  
✅ Створено клас Figure з навмисною помилкою (app.py)  
✅ Створено юніт тести з використанням unittest (test_figure.py)  
✅ Протестовано виконання тестів через Visual Studio Code та консоль  
✅ Додано __pycache__ до .gitignore  
✅ Розширено функціонал класу Figure (додано методи calculate_perimeter, calculate_area)  
✅ Створено відповідні тести для нового функціоналу  
✅ Встановлено PyTest  
✅ Створено тести з використанням PyTest (test_figure_pytest.py)  
✅ Використано параметризацію та фікстури в PyTest тестах  

**Всі завдання лабораторної роботи №3 виконано успішно!** ✨
