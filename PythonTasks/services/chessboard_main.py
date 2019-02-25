from models.validation_value import (
    CheckRequirements,
    GreaterThanZero
)
from models.input_value import AskInput, IntInput

from models.chessboard_algorithm import Chessboard


if __name__ == '__main__':
    length_chessboard = IntInput(AskInput("Please, enter length")).value()
    width_chessboard = IntInput(AskInput("Please, enter width")).value()
    check_side = CheckRequirements(GreaterThanZero())

    if check_side.passed(length_chessboard) and\
       check_side.passed(width_chessboard):
        new_chessboard = Chessboard(
                                    length_chessboard,
                                    width_chessboard
                                   ).chessboard_rendering()

