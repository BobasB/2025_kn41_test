"""
Юніт тести для класу Figure з файлу app.py
"""

import unittest
from random import choice, randint

from app import Figure  # назва файлу з нашим класом повинна бути app.py


class TestFigure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Виконається лише раз на початку тестів"""
        print("\n" + "="*50)
        print("Початок тестування класу Figure")
        print("="*50)
    
    def setUp(self) -> None:
        """Виконується кожного разу коли запускається тест"""
        self.figure = choice(Figure.FIGURES)
        self.length = randint(1, 10)
        self.obj = Figure(self.figure, self.length)
        return super().setUp()

    def tearDown(self) -> None:
        """Виконується після кожного тестового методу"""
        del self.obj
        return super().tearDown()
    
    @classmethod
    def tearDownClass(cls):
        """Виконається лише раз після всіх тестів"""
        print("\n" + "="*50)
        print("Завершення тестування класу Figure")
        print("="*50)

    def test_figure_type(self):
        """Перевіряємо, що властивість get_figure_type повертає правильний тип"""
        print(f"\nТестуємо вивід типу, має бути: {self.figure} == {self.obj.get_figure_type}")
        self.assertEqual(self.figure, self.obj.get_figure_type, 
                        "Властивість get_figure_type повертає непривильну фігуру!")

    def test_figure_length(self):
        """Перевіряємо, що властивість get_figure_length повертає правильну довжину"""
        print(f"\nТестуємо вивід довжини, має бути: {self.length} == {self.obj.get_figure_length}")
        self.assertEqual(self.length, self.obj.get_figure_length, 
                        "Властивість get_figure_length повертає непривильну довжину!")
    
    def test_obj(self):
        """Перевіряємо, що AssertionError викликається при недозволених параметрах"""
        print("\nПеревіряємо виклик AssertionError для недозволеної фігури")
        with self.assertRaises(AssertionError):
            Figure("коло", 1)  # Спробуємо створити об'єкт з недозволеними параметрами
    
    def test_negative_length(self):
        """Перевіряємо, що AssertionError викликається при від'ємній довжині"""
        print("\nПеревіряємо виклик AssertionError для від'ємної довжини")
        with self.assertRaises(AssertionError):
            Figure("квадрат", -1)
    
    def test_zero_length(self):
        """Перевіряємо, що AssertionError викликається при нульовій довжині"""
        print("\nПеревіряємо виклик AssertionError для нульової довжини")
        with self.assertRaises(AssertionError):
            Figure("трикутник", 0)
    
    def test_perimeter_calculation(self):
        """Перевіряємо правильність розрахунку периметра"""
        print(f"\nТестуємо розрахунок периметра для {self.figure}")
        perimeter = self.obj.calculate_perimeter()
        self.assertIsInstance(perimeter, (int, float))
        self.assertGreater(perimeter, 0)
        
        # Перевіряємо конкретні значення
        if self.figure == "квадрат":
            self.assertEqual(perimeter, 4 * self.length)
        elif self.figure == "прямокутник":
            self.assertEqual(perimeter, 4 * self.length)
        elif self.figure == "трикутник":
            self.assertEqual(perimeter, 3 * self.length)
    
    def test_area_calculation(self):
        """Перевіряємо правильність розрахунку площі"""
        print(f"\nТестуємо розрахунок площі для {self.figure}")
        area = self.obj.calculate_area()
        self.assertIsInstance(area, (int, float))
        self.assertGreater(area, 0)
    
    def test_string_representation(self):
        """Перевіряємо строкове представлення об'єкта"""
        print(f"\nТестуємо строкове представлення об'єкта")
        str_repr = str(self.obj)
        self.assertIn(self.figure, str_repr)
        self.assertIn(str(self.length), str_repr)


if __name__ == '__main__':
    # unittest.main()  # базовий запуск
    unittest.main(verbosity=2)  # детальний вивід
