from models.validation_value import (
    CheckRequirements,
    GreaterThanZero,
    IntArgs
)
from models.input_value import AskInput, SplitInput
from models.fibonacci_algorithm import FibonacciRange, FibonacciLength


if __name__ == '__main__':
    required_number = SplitInput(AskInput("Please, enter fibonacci number")).value()
    check_required_number = CheckRequirements(IntArgs(), GreaterThanZero())

    if len(required_number) == 1 and check_required_number.passed(
           int(required_number[0])):
        fibo_length = FibonacciLength(
            int(required_number[0])).fibonacci_calculation_sequence()

        print(f"You've got next fibonacci sequence: {fibo_length}")

    if len(required_number) == 2 and check_required_number.passed(
           int(required_number[0])):
        fibo_range = FibonacciRange(
            int(required_number[0]),
            int(required_number[1])
        ).fibonacci_range()

        print(f"You've got next fibonacci sequence: {fibo_range}")

