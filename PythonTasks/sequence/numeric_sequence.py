"""This program has been created to print a comma-separated row
of length consisting of natural numbers whose square is not
less than a given number."""

from math import sqrt


def sequence_calculation(length: int, square_number: int) -> list:
    first_number_seq = sqrt(square_number)
    if first_number_seq % 1 != 0:
        first_number_seq: float = int(first_number_seq) + 1
    sequence_list = [number for number in range(int(first_number_seq),
                                                int(first_number_seq) + length)]
    return sequence_list


def is_valid_data(input_item: str) -> int:
    while True:
        try:
            entered_value = int(input(f"Please, enter {input_item}: "))
            if 0 < entered_value < 1000:
                break
        except ValueError:
            print("Please, enter integer")
    return entered_value


def main():
    output_sequence = (sequence_calculation(is_valid_data("sequence length"),
                       is_valid_data("square number")))

    print(f"You've been got sequence: {output_sequence}")


if __name__ == '__main__':
    main()



