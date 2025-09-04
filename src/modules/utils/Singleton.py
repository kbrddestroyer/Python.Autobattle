"""
Defines Singleton utility class
"""
from __future__ import annotations
import typing
from tokenize import Single

if typing.TYPE_CHECKING:
    from typing import Any


class Singleton:
    INSTANCES = {}

    def __new__(cls, *args, **kwargs) -> Any:
        class_name = cls.__name__
        instance = Singleton.INSTANCES.get(class_name)
        if instance:
            return instance

        instance = super().__new__(cls)
        Singleton.INSTANCES[class_name] = instance
        return instance

    @classmethod
    def get_instance(cls):
        if cls.__name__ not in Singleton.INSTANCES:
            return Singleton.__new__(cls)

        return Singleton.INSTANCES[cls.__name__]
