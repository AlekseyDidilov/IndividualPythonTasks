from models.input_value import AskInput
from models.palindrome_algorithm import Palindrome


if __name__ == "__main__":
    required_value = AskInput("Please, enter required value:").value()
    check_palindrome = Palindrome(required_value).is_palindrome()
    print(f"After checking, your palindrome is: {check_palindrome}")
