class Envelope:
    def __init__(self, side_1: float, side_2: float):
        self._side_1 = side_1
        self._side_2 = side_2

    def __lt__(self, other) -> bool:
        return self._side_1 < other._side_1 and self._side_2 < other._side_2
