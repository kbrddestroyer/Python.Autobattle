"""
Entity class is pretty much everything that can be processed in BattleController instance
"""
from __future__ import annotations
from abc import abstractmethod

from utils.Singleton import Singleton


class EntityRegistry(Singleton):
    def __init__(self):
        self.__entities = []

    def add(self, entity: Entity):
        self.__entities.append(entity)
        entity.initialize()

    def initialize(self):
        for entity in self.__entities:
            entity.initialize()


class Entity:
    def __init__(self):
        EntityRegistry.get_instance().add(self)

    @abstractmethod
    def initialize(self, *args, **kwargs):
        raise NotImplementedError
