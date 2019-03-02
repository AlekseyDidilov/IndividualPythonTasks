from typing import List


class FibonacciLength:

    def __init__(self, number):
        self._number = number

    def fibonacci_calculation_sequence(self) -> List:
        sequence = list()
        number1, number2 = 0, 1
        while True:
            number1, number2 = number2, number1 + number2
            length_number = str(number1)
            if len(length_number) == self._number:
                sequence.append(number1)
            if len(length_number) > self._number:
                break
        return sequence


class FibonacciRange:

    def __init__(self, start_range: int, end_range: int):
        self._start_range = start_range
        self._end_range = end_range

    def fibonacci_range(self) -> List:
        sequence = list()
        number_start1, number_start2 = 0, 1
        number_end1, number_end2 = 0, 1
        for _ in range(self._start_range - 1):
            number_end1, number_end2 = number_end2, number_end1 + number_end2
        for _ in range(self._end_range - 1):
            number_start1, number_start2 = number_start2, number_start1 + number_start2
            if number_start1 >= number_end1:
                sequence.append(number_start1)
        return sequence



