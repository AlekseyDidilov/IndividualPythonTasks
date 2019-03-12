from models.validation_value import (
    CheckRequirements,
    NoLessThanZero,
    LessOneMillionOne
)
from models.input_value import AskInput, IntInput
from models.happy_tickets_algorithm import HappyTickets


if __name__ == "__main__":
    start_number = IntInput(AskInput("Please, enter required number")).value()
    stop_number = IntInput(AskInput("Please, enter required number")).value()
    check_number = CheckRequirements(NoLessThanZero(), LessOneMillionOne())
    if check_number.passed(start_number) and check_number.passed(stop_number):
        new_happy_tickets_count = HappyTickets(start_number, stop_number)
        new_happy_tickets_count.get_happy_tickets()
        print(new_happy_tickets_count)

