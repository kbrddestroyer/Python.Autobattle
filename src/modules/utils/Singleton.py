"""
Defines Singleton utility class
"""
from __future__ import annotations
import typing


if typing.TYPE_CHECKING:
    from typing import Any


class AlreadyDefinedException(Exception):
    def __init__(self, className):
        self.className = className

    def __str__(self):
        return f"Singleton instance was already defined: {self.className}"


class Singleton:
    INSTANCES = {}

    def __new__(cls, *args, **kwargs) -> Any:
        if cls.__name__ in Singleton.INSTANCES:
            raise AlreadyDefinedException(cls.__name__)

        instance = super().__new__(cls, args, kwargs)
        Singleton.INSTANCES[cls.__name__] = instance
        return instance

    @staticmethod
    def get_instance(className: str):
        return Singleton.INSTANCES[className]
