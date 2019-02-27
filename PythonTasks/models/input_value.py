from abc import ABC, abstractmethod
from typing import Any, List


class Input(ABC):

    @abstractmethod
    def value(self) -> Any:
        pass


class AskInput(Input):

    def __init__(self, question: str):
        self._question = question

    def value(self) -> Any:
        return input(self._question + '\n')


class SplitInput(Input):

    def __init__(self, origin: Input):
        self._origin = origin

    def value(self) -> List:
        return input(f"{self._origin}").split(",")


class IntInput(Input):

    def __init__(self, origin: Input):
        self._origin = origin

    def value(self) -> Any:
        return int(self._origin.value())


