from typing import List


class Chessboard:

    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def chessboard_building(self) -> List[str]:
        chessboard_model = list()
        for line_number in range(self._length):
            if line_number % 2 == 0:
                chessboard_model.append(("* " * (self._width // 2)) + ("*" * (self._width % 2)))
            else:
                chessboard_model.append((" *" * (self._width // 2)) + (" " * (self._width % 2)))
        return chessboard_model
