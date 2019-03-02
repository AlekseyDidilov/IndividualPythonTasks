from abc import ABC, abstractmethod
from typing import Any, List


class Requirements(ABC):

    @abstractmethod
    def passed(self, *value: Any) -> bool:
        pass


class GreaterThanZero(Requirements):

    def passed(self, value: int) -> bool:
        return value > 0


class LessOneMillion(Requirements):

    def passed(self, value: int) -> bool:
        return value < 1000000


class IntArgs(Requirements):

    def passed(self, *value: str) -> bool:
        try:
            return isinstance(int(*value), int)
        except ValueError:
            return False


class SidesFloat(Requirements):

    def passed(self, side_1: str, side_2: str, side_3: str) -> bool:
        try:
            float(side_1)
            float(side_2)
            float(side_3)
            return True
        except ValueError:
            print("Incorrect data, input must be in float!")


class SumTwoSides(Requirements):

    def passed(self, side_1: str, side_2: str, side_3: str) -> bool:
        return (float(side_1) + float(side_2) > float(side_3) and
                float(side_1) + float(side_3) > float(side_2) and
                float(side_2) + float(side_3) > float(side_1))


class LessZero(Requirements):

    def passed(self, side_1: str, side_2: str, side_3: str) -> bool:
        return min(float(side_1), float(side_2), float(side_3)) > 0


class StringLength(Requirements):

    def passed(self, value: List) -> bool:
        return len(value) == 4


class CheckRequirements(Requirements):

    def __init__(self, *requirements: Any):
        self._test = requirements

    def passed(self, *value: int) -> bool:
        for requirement in self._test:
            if not requirement.passed(*value):
                print(
                      f"{requirement.__class__.__name__} is failed."
                      f"Please, run program again!"
                )
                return False
        return True
