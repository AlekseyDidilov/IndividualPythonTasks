from models.validation_value import CheckRequirements, GreaterThanZero, LessOneMillion
from models.input_value import AskInput, IntInput
from models.digits2text_algorithm import TranslateInText


if __name__ == "__main__":
    required_number = IntInput(AskInput("Please, enter required number")).value()
    check_number = CheckRequirements(GreaterThanZero(), LessOneMillion())

    if check_number.passed(required_number):
        new_translation = TranslateInText(required_number).numbers_to_text()
        print(f"Converted value from number in text is: {new_translation}")
