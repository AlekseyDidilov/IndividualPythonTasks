class Chessboard:

    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def chessboard_rendering(self) -> None:
        for line_number in range(self._length):
            if line_number % 2 == 0:
                print(("* " * (self._width // 2)) + ("*" * (self._width % 2)))
            else:
                print((" *" * (self._width // 2)) + (" " * (self._width % 2)))

