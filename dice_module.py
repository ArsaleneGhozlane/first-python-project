import random

class Dice:
    def __init__(self):
        self._value = 0

    def roll(self):
        self._value = random.randint(1, 6)
        return self._value

    @property
    def value(self):
        return self._value

""" did nothing"""
class DiceGame:
    def __init__(self):
        self.dice1 = Dice()
        self.dice2 = Dice()
        self.total = 0

    def roll_dice(self):
        self.total = self.dice1.roll() + self.dice2.roll()
        return self.total

    @property
    def result(self):
        if self.total >= 10:
            return "You Win!"
        else:
            return "Try Again!"


def main():
    game = DiceGame()
    while True:
        input("Press Enter to roll the dice...")
        total = game.roll_dice()
        print(f"Dice 1: {game.dice1.value}, Dice 2: {game.dice2.value}, Total: {total}")
        print(game.result)
        if input("Do you want to roll again? (y/n): ").lower() != 'y':
            break


if __name__ == "__main__":
    main()