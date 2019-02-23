"""This program creates and shows chessboard after user
 inputting from the keyboard length and width. """


def chessboard_building(length: int, width: int):
    for string_number in range(length):
        if string_number % 2 == 0:
                print(("* " * (width // 2)) + ("*" * (width % 2)))
        else:
                print((" *" * (width // 2)) + (" " * (width % 2)))


def validation_input_parameters(input_side: str) -> int:
    while True:
        try:
            entered_value = int(input(f"Please, enter {input_side}: "))
            if 0 < entered_value < 1000:
                break
        except ValueError:
            print("Please, enter integer")
    return entered_value


def main():
    chessboard_building(validation_input_parameters("chessboard length"),
                        validation_input_parameters("chessboard width"))


if __name__ == '__main__':
    main()