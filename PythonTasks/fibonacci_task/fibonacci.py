"""This program has been created to print all Fibonacci numbers
that satisfy the constraint passed to the function:
are in the specified range, or have the specified length."""


def fibonacci_number(end_number: int) -> list:
    sequence = list()
    number1, number2 = 0, 1
    while True:
        number1, number2 = number2, number1 + number2
        length_number = str(number1)
        if len(length_number) == end_number:
            sequence.append(number1)
        elif len(length_number) > end_number:
            break
    return sequence


def fibonacci_range(start_range: int, end_range: int) -> list:
    sequence = list()
    number_start1, number_start2 = 0, 1
    number_end1, number_end2 = 0, 1
    for _ in range(start_range - 1):
        number_end1, number_end2 = number_end2, number_end1 + number_end2
    for _ in range(end_range - 1):
        number_start1, number_start2 = number_start2, number_start1 + number_start2
        if number_start1 >= number_end1:
            sequence.append(number_start1)
    return sequence


def is_valid(input_value: str) -> int:
    while True:
        try:
            entered_value = int(input(f"Please, enter {input_value}: "))
            if 0 <= entered_value <= 1000:
                break
        except ValueError:
            print("Please, enter integer")
    return entered_value


def main():
    first_value = is_valid("number")
    while True:
        try:
            continue_input = input("If you want to continue enter - y, otherwise - n ")
            if continue_input.lower() == "n":
                fibonacci_list = fibonacci_number(first_value)
                break
            elif continue_input.lower() == "y":
                second_value = is_valid("second number")
                fibonacci_list = fibonacci_range(first_value, second_value)
                break
        except ValueError:
            print("Please enter y or n ")
    print(f"You've been got following fibonacci sequences: {fibonacci_list}")


if __name__ == '__main__':
    main()



