from typing import override

from modules.Entity import Entity
from modules.gameplay.controller.DiceController import DiceController
from modules.utils.Logger import Logger


class Character(Entity):
    MAX_HEALTH_BY_CHARACTER = {}
    DICE_TO_ROLL_INITIATIVE = 20

    def __init__(self) -> None:
        self.__health = Character.MAX_HEALTH_BY_CHARACTER.get(self.__class__.__name__, 0)
        self.__initiative = 0

        if self.__health <= 0:
            Logger.get_instance().error(f"Character {self.__class__.__name__} has no health set")

    @override
    def initialize(self):
        self.__initiative = DiceController.roll(Character.DICE_TO_ROLL_INITIATIVE)
