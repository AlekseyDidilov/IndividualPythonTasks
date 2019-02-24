from abc import ABC, abstractmethod
from typing import Any


class Requirements(ABC):

    @abstractmethod
    def passed(self, value: Any) -> bool:
        pass


class GreaterThanZero(Requirements):

    def passed(self, value: int) -> bool:
        return value > 0


class LessOneMillion(Requirements):

    def passed(self, value: int) -> bool:
        return value < 1000000


class CheckRequirements(Requirements):

    def __init__(self, *requirements: Any):
        self._test = requirements

    def passed(self, value: int) -> bool:
        for requirement in self._test:
            if not requirement.passed(value):
                print(f"{requirement.__class__.__name__} is failed.")
                return False
        return True
