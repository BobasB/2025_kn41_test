"""
PyTest тести для класу Dice
"""

import pytest
from dice import Dice


class TestDiceWithPytest:
    """Тестовий клас для перевірки Dice з використанням PyTest"""
    
    def setup_method(self):
        """Виконується перед кожним тестовим методом"""
        self.dice = Dice(6)
    
    def test_dice_creation(self):
        """Тест створення об'єкта Dice"""
        dice = Dice(6)
        assert dice.faces == 6
    
    def test_roll_returns_valid_number(self):
        """Тест що roll повертає число в правильному діапазоні"""
        result = self.dice.roll()
        assert isinstance(result, int)
        assert 1 <= result <= 6
    
    @pytest.mark.parametrize("sides", [4, 6, 8, 10, 12, 20])
    def test_different_dice_types(self, sides):
        """Параметризований тест для різних типів кубиків"""
        dice = Dice(sides)
        assert dice.faces == sides
        result = dice.roll()
        assert 1 <= result <= sides
    
    def test_roll_multiple_times(self):
        """Тест багаторазового кидання"""
        results = [self.dice.roll() for _ in range(100)]
        # Всі результати мають бути в діапазоні
        assert all(1 <= r <= 6 for r in results)
        # Має бути різноманітність (хоча б 2 різні результати)
        assert len(set(results)) >= 2
    
    @pytest.mark.parametrize("sides,expected_min,expected_max", [
        (6, 1, 6),
        (20, 1, 20),
        (4, 1, 4),
    ])
    def test_roll_range(self, sides, expected_min, expected_max):
        """Тест діапазону значень для різних кубиків"""
        dice = Dice(sides)
        for _ in range(10):
            result = dice.roll()
            assert expected_min <= result <= expected_max


@pytest.fixture
def standard_dice():
    """Фікстура для стандартного 6-гранного кубика"""
    return Dice(6)


@pytest.fixture
def d20_dice():
    """Фікстура для 20-гранного кубика"""
    return Dice(20)


def test_with_fixture_standard(standard_dice):
    """Тест з використанням фікстури для стандартного кубика"""
    assert standard_dice.faces == 6
    result = standard_dice.roll()
    assert 1 <= result <= 6


def test_with_fixture_d20(d20_dice):
    """Тест з використанням фікстури для d20 кубика"""
    assert d20_dice.faces == 20
    result = d20_dice.roll()
    assert 1 <= result <= 20


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
