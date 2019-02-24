from validation.validation_value import (
    CheckRequirements,
    GreaterThanZero
)
from input.input_value import AskInput, IntInput
from digits2text.digits2text_algorithm import TranslatorInText


if __name__ == "__main__":
    required_number = IntInput(AskInput("Please, enter required number")).value()
    check_number = CheckRequirements(GreaterThanZero())

    if check_number.passed(required_number):
        new_translation = TranslatorInText(required_number).numbers_to_text()
        print(f"Converted value from number in text is: {new_translation}")
