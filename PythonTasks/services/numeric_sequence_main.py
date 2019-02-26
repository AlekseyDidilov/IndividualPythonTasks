from models.validation_value import (
    CheckRequirements,
    GreaterThanZero,
    LessOneMillion
)
from models.input_value import AskInput, IntInput
from models.numeric_sequence_algorithm import Sequence


if __name__ == "__main__":
    required_number = IntInput(AskInput("Please, enter sequence length")).value()
    required_square = IntInput(AskInput("Please, enter number in square")).value()
    check_number = CheckRequirements(GreaterThanZero(), LessOneMillion())

    if check_number.passed(required_number) and check_number.passed(required_square):
        new_sequence = Sequence(required_number, required_square).sequence_calculation()
        print(f"Sequence has next elements: {new_sequence}")
