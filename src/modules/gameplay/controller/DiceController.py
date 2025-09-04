import random


class DiceController:
    @staticmethod
    def roll(size: int) -> int:
        return random.randint(1, size)
