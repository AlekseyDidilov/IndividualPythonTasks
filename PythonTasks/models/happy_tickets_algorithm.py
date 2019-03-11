from typing import List, Tuple


class HappyTickets:
    def __init__(self, start_value: int, stop_value: int):
        self._start_ticket = start_value
        self._stop_ticket = stop_value
        self._tickets_output = list()
        self._happy_tickets_amount1 = 0
        self._happy_tickets_amount2 = 0

    def happy_ticket_list(self) -> List[str]:
        self._tickets_output = [
            str(_).zfill(6) for _ in range(self._start_ticket, self._stop_ticket)
        ]
        return self._tickets_output

    def method_easy(self) -> int:
        for digit in self._tickets_output:
            first_half = int(digit[0]) + int(digit[1]) + int(digit[2])
            second_half = int(digit[3]) + int(digit[4]) + int(digit[5])
            if first_half == second_half:
                self._happy_tickets_amount1 += 1
        return self._happy_tickets_amount1

    def method_hard(self) -> int:
        for digit in self._tickets_output:
            even = int(digit[0]) + int(digit[2]) + int(digit[4])
            odd = int(digit[1]) + int(digit[3]) + int(digit[5])
            if even == odd:
                self._happy_tickets_amount2 += 1
        return self._happy_tickets_amount2

    def get_happy_tickets(self) -> Tuple:
        if len(self._tickets_output) == 0:
            self.happy_ticket_list()
            return self.method_easy(), self.method_hard()

    def compare_winner(self) -> str:
        if self._happy_tickets_amount1 > self._happy_tickets_amount2:
            return "Method easy won!"
        if self._happy_tickets_amount1 < self._happy_tickets_amount2:
            return "Method hard won!"
        return "Variants equal!"

    def __str__(self) -> str:
        return (
            f"{self.compare_winner()}\n"
            f"Easy has {self._happy_tickets_amount1} happy tickets!\n"
            f"Hard has {self._happy_tickets_amount2} happy tickets!"
        )
