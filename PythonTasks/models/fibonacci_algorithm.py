from typing import List


class FibonacciLength:
    def __init__(self, number: int):
        self._number = number

    def length_calculation(self) -> List[int]:
        sequence = list()
        number_1, number_2 = 0, 1
        while True:
            number_1, number_2 = number_2, number_1 + number_2
            number_length = str(number_1)
            if len(number_length) == self._number:
                sequence.append(number_1)
            if len(number_length) > self._number:
                break
        return sequence


class FibonacciRange:
    def __init__(self, start_range: int, end_range: int):
        self._start_range = start_range
        self._end_range = end_range

    def range_calculation(self) -> List[int]:
        sequence = list()
        start_num_1, start_num_2 = 0, 1
        end_num_1, end_num_2 = 0, 1
        for _ in range(self._start_range - 1):
            end_num_1, end_num_2 = end_num_2, end_num_1 + end_num_2
        for _ in range(self._end_range - 1):
            start_num_1, start_num_2 = start_num_2, start_num_1 + start_num_2
            if start_num_1 >= end_num_1:
                sequence.append(start_num_1)
        return sequence
