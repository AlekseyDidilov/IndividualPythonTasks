from abc import ABC, abstractmethod
from typing import Any


class Input(ABC):

    @abstractmethod
    def value(self) -> Any:
        pass


class AskInput(Input):

    def __init__(self, prompt: str):
        self._q = prompt

    def value(self) -> Any:
        return input(self._q + '\n')


class IntInput(Input):

    def __init__(self, origin: Input):
        self._origin = origin

    def value(self) -> Any:
        return int(self._origin.value())


