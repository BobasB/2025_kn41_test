from dice import Dice
import unittest
import random

# Тестовий клас має починатись з великої літери, слова "Test" і наслідувати unittest.TestCase
class TestDice(unittest.TestCase):
    def setUp(self):
        """Цей метод виконується перед кожним тестовим методом."""
        print("\nЗапуск тесту...")
        self.dice_faces = random.choice([4, 6, 8, 10, 12, 20])
        self.dice = Dice(self.dice_faces)  # Створюємо об'єкт Dice з випадковою кількістю граней для використання в тестах
    
    def tearDown(self):
        """Цей метод виконується після кожного тестового методу."""
        print("Тест завершено.")
        del self.dice
        del self.dice_faces
    
    # Тестовий метод має починатись з "test*"
    def test_initialization_of_dice_object(self):
        """Перевіряємо, що об'єкт Dice ініціалізується правильно з різною кількістю граней."""
        print("Запуск test_initialization_of_dice_object")
        # Виправлена навмисна помилка - тепер тест проходить
        self.assertEqual(self.dice.faces, self.dice_faces)
        self.assertIn(self.dice.roll(), range(1, self.dice_faces + 1))
        self.assertIsInstance(self.dice.roll(), int)
    
    def test_object_faces_is_a_grater_then_zero(self):
        """Перевіряємо, що кількість граней більше нуля."""
        print("Запуск test_object_faces_is_a_grater_then_zero")
        for sides in [4, 6, 8, 10, 12, 20]:
            dice = Dice(sides)
            self.assertGreater(dice.faces, 0)
    
    def test_roll_method_returns_int_within_range(self):
        """Перевіряємо, що метод roll завжди повертає ціле число."""
        print("Запуск test_roll_method_returns_int_within_range")
        for _ in range(100):  # Виконуємо 100 кидків для надійності
            result = self.dice.roll()
            self.assertIsInstance(result, int)
            self.assertGreaterEqual(result, 1)
            self.assertLessEqual(result, self.dice.faces)
        
        

if __name__ == "__main__":
    unittest.main(verbosity=2)