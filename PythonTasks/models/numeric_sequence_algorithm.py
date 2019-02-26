from typing import List
from math import sqrt


class Sequence:

    def __init__(self, seq_length: int, square_number: int):
        self._seq_length = seq_length
        self._square_number = square_number

    def sequence_calculation(self) -> List:
        first_number_seq = sqrt(self._square_number)
        if first_number_seq % 1 != 0:
            first_number_seq: float = int(first_number_seq) + 1
        sequence_list = [_ for _ in range(int(first_number_seq),
                                          int(first_number_seq) + self._seq_length)]
        return sequence_list


