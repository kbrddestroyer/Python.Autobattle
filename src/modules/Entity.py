"""
Entity class is pretty much everything that can be processed in BattleController instance
"""
from __future__ import annotations
import typing
from utils.Singleton import Singleton, AlreadyDefinedException


class EntityRegistry(metaclass=Singleton):
    pass

class Entity:
    def __init__(self):
        pass

