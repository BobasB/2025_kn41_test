import random
class Dice:
    def __init__(self, sides: int):
        self.faces = sides

    # Це методи а в нього передається завжди self - вказівка на об'єкт
    def roll(self) -> int:
        return random.randint(1, self.faces)

if __name__ == "__main__":
    dice = Dice(6)
    result = dice.roll()
    print(f"Кубик з {dice.faces} гранями. Випало число: {result}")
