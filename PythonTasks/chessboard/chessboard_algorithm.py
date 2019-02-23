class Chessboard:

    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def chessboard_rendering(self) -> None:
        for line_number in range(self.length):
            if line_number % 2 == 0:
                print(("* " * (self.width // 2)) + ("*" * (self.width % 2)))
            else:
                print((" *" * (self.width // 2)) + (" " * (self.width % 2)))

