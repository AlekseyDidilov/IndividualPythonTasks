from models.validation_value import (
    CheckRequirements,
    GreaterThanZero,
    LessOneHundred,
    IntArgs,
)
from models.input_value import AskInput, SplitInput
from models.fibonacci_algorithm import FibonacciRange, FibonacciLength


if __name__ == "__main__":
    required_number = SplitInput(AskInput("Please, enter fibonacci number")).value()
    check_required_number = CheckRequirements(
        IntArgs(),
        LessOneHundred(),
        GreaterThanZero()
    )
    if len(required_number) == 1:
        if check_required_number.passed((int(required_number[0]))):
            fibo_length = FibonacciLength(int(required_number[0])).length_calculation()
            print(f"You've got next fibonacci sequence: {fibo_length}")

    if len(required_number) == 2:
        if check_required_number.passed(int(required_number[0])
        and check_required_number.passed(int(required_number[1]))):
            fibo_range = FibonacciRange(
                int(required_number[0]),
                int(required_number[1])
            ).range_calculation()

        print(f"You've got next fibonacci sequence: {fibo_range}")
