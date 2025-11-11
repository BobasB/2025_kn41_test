from dice import Dice
import unittest

# Тестовий клас має починатись з великої літери, слова "Test" і наслідувати unittest.TestCase
class TestDice(unittest.TestCase):

    # Тестовий метод має починатись з "test*"
    def test_initialization_of_dice_object(self):
        """Перевіряємо, що об'єкт Dice ініціалізується правильно з різною кількістю граней."""
        for sides in [4, 6, 8, 10, 12, 20]:
            dice = Dice(sides)
            self.assertEqual(dice.faces, sides)
    
    def test_object_faces_is_a_grater_then_zero(self):
        """Перевіряємо, що кількість граней більше нуля."""
        for sides in [4, 6, 8, 10, 12, 20]:
            dice = Dice(sides)
            self.assertGreater(dice.faces, 0)
        

if __name__ == "__main__":
    unittest.main(verbosity=2)