"""
PyTest тести для класу Figure з файлу app.py
"""

import pytest
from app import Figure
import math


class TestFigureWithPytest:
    """Тестовий клас для перевірки Figure з використанням PyTest"""
    
    def setup_method(self):
        """Виконується перед кожним тестовим методом"""
        print("\nНалаштування тесту...")
    
    def teardown_method(self):
        """Виконується після кожного тестового методу"""
        print("Завершення тесту...")
    
    def test_figure_creation(self):
        """Тест створення об'єкта Figure"""
        figure = Figure("квадрат", 5)
        assert figure.type == "квадрат"
        assert figure.length == 5
    
    def test_figure_type_property(self):
        """Тест властивості get_figure_type"""
        figure = Figure("трикутник", 10)
        assert figure.get_figure_type == "трикутник"
    
    def test_figure_length_property(self):
        """Тест властивості get_figure_length (має провалитися через помилку!)"""
        figure = Figure("прямокутник", 7)
        # Цей тест провалиться, бо в app.py є помилка
        assert figure.get_figure_length == 7, "get_figure_length має повертати довжину, а не тип!"
    
    @pytest.mark.parametrize("figure_type,length", [
        ("квадрат", 5),
        ("прямокутник", 10),
        ("трикутник", 8),
    ])
    def test_valid_figures(self, figure_type, length):
        """Параметризований тест для різних типів фігур"""
        figure = Figure(figure_type, length)
        assert figure.type == figure_type
        assert figure.length == length
    
    @pytest.mark.parametrize("figure_type,length", [
        ("коло", 5),
        ("ромб", 10),
        ("трапеція", 8),
    ])
    def test_invalid_figure_types(self, figure_type, length):
        """Тест для недозволених типів фігур"""
        with pytest.raises(AssertionError):
            Figure(figure_type, length)
    
    @pytest.mark.parametrize("length", [0, -1, -10])
    def test_invalid_lengths(self, length):
        """Тест для некоректних довжин"""
        with pytest.raises(AssertionError):
            Figure("квадрат", length)
    
    def test_square_perimeter(self):
        """Тест розрахунку периметра квадрата"""
        square = Figure("квадрат", 5)
        assert square.calculate_perimeter() == 20
    
    def test_rectangle_perimeter(self):
        """Тест розрахунку периметра прямокутника"""
        rectangle = Figure("прямокутник", 6)
        assert rectangle.calculate_perimeter() == 24
    
    def test_triangle_perimeter(self):
        """Тест розрахунку периметра трикутника"""
        triangle = Figure("трикутник", 4)
        assert triangle.calculate_perimeter() == 12
    
    def test_square_area(self):
        """Тест розрахунку площі квадрата"""
        square = Figure("квадрат", 5)
        assert square.calculate_area() == 25
    
    def test_triangle_area(self):
        """Тест розрахунку площі трикутника"""
        triangle = Figure("трикутник", 4)
        expected_area = (16 * math.sqrt(3)) / 4
        assert abs(triangle.calculate_area() - expected_area) < 0.0001
    
    def test_string_representation(self):
        """Тест строкового представлення"""
        figure = Figure("квадрат", 7)
        str_repr = str(figure)
        assert "квадрат" in str_repr
        assert "7" in str_repr


@pytest.fixture
def square_figure():
    """Фікстура для створення квадрата"""
    return Figure("квадрат", 10)


@pytest.fixture
def triangle_figure():
    """Фікстура для створення трикутника"""
    return Figure("трикутник", 6)


def test_with_fixture_square(square_figure):
    """Тест з використанням фікстури для квадрата"""
    assert square_figure.type == "квадрат"
    assert square_figure.length == 10
    assert square_figure.calculate_perimeter() == 40


def test_with_fixture_triangle(triangle_figure):
    """Тест з використанням фікстури для трикутника"""
    assert triangle_figure.type == "трикутник"
    assert triangle_figure.length == 6
    assert triangle_figure.calculate_perimeter() == 18


# Тести з маркерами
@pytest.mark.slow
def test_multiple_figures_creation():
    """Тест створення багатьох фігур (позначено як повільний)"""
    figures = []
    for i in range(100):
        figures.append(Figure("квадрат", i + 1))
    assert len(figures) == 100


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
