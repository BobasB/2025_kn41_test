"""
Клас Figure для демонстрації unittest тестування
Містить навмисну помилку в методі get_figure_length
"""

class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]
    
    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length

    @property
    def get_figure_type(self):
        """Повертає тип фігури"""
        return self.type

    @property
    def get_figure_length(self):
        """Повертає довжину фігури (тут навмисна помилка для демонстрації роботи тестів!)"""
        # УВАГА: Це навмисна помилка для лабораторної роботи!
        # Метод має повертати self.length, але повертає self.type
        # Це демонструє як тести виявляють помилки в коді
        return self.type  # ПОМИЛКА: повертаємо type замість length
    
    def calculate_perimeter(self):
        """Розрахунок периметра фігури"""
        if self.type == "квадрат":
            return 4 * self.length
        elif self.type == "прямокутник":
            # Для простоти припустимо, що це квадратний прямокутник
            return 4 * self.length
        elif self.type == "трикутник":
            # Для рівностороннього трикутника
            return 3 * self.length
        return 0
    
    def calculate_area(self):
        """Розрахунок площі фігури"""
        if self.type == "квадрат":
            return self.length ** 2
        elif self.type == "прямокутник":
            # Для простоти припустимо, що це квадратний прямокутник
            return self.length ** 2
        elif self.type == "трикутник":
            # Для рівностороннього трикутника: площа = (a^2 * sqrt(3)) / 4
            import math
            return (self.length ** 2 * math.sqrt(3)) / 4
        return 0
    
    def __str__(self):
        return f"Figure(type={self.type}, length={self.length})"


if __name__ == "__main__":
    print("=== Тестування класу Figure ===\n")
    
    # Створюємо кілька об'єктів
    square = Figure("квадрат", 5)
    print(f"Створено: {square}")
    print(f"Тип: {square.get_figure_type}")
    print(f"Довжина (має бути помилка!): {square.get_figure_length}")
    print(f"Периметр: {square.calculate_perimeter()}")
    print(f"Площа: {square.calculate_area()}\n")
    
    rectangle = Figure("прямокутник", 10)
    print(f"Створено: {rectangle}")
    print(f"Тип: {rectangle.get_figure_type}")
    print(f"Довжина (має бути помилка!): {rectangle.get_figure_length}")
    print(f"Периметр: {rectangle.calculate_perimeter()}")
    print(f"Площа: {rectangle.calculate_area()}\n")
    
    triangle = Figure("трикутник", 8)
    print(f"Створено: {triangle}")
    print(f"Тип: {triangle.get_figure_type}")
    print(f"Довжина (має бути помилка!): {triangle.get_figure_length}")
    print(f"Периметр: {triangle.calculate_perimeter()}")
    print(f"Площа: {triangle.calculate_area()}\n")
