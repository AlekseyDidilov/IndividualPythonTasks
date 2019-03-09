from models.validation_value import (
    CheckRequirements,
    SidesFloat,
    SumTwoSides,
    LessZero,
    StringLength,
)

from models.input_value import AskInput, SplitInput
from models.execution import NewExecution

from models.triangles_algorithm import Triangle, TriangleList


if __name__ == "__main__":
    triangles_sorted = TriangleList()
    while True:
        triangle_data = SplitInput(
            AskInput(
                "Please, enter triangle name and size of sides \n"
                "Input format - 'name, side_a, side_b, side_c':"
            )
        ).value()
        checked_length = CheckRequirements(StringLength())
        checked_sides = CheckRequirements(SidesFloat(), SumTwoSides(), LessZero())
        if checked_length.passed(triangle_data) and checked_sides.passed(
            triangle_data[1], triangle_data[2], triangle_data[3]
        ):
            new_triangle = Triangle(
                str(triangle_data[0]),
                float(triangle_data[1]),
                float(triangle_data[2]),
                float(triangle_data[3]),
            ).square_calculation()
            triangles_sorted.add_triangle(new_triangle)
        else:
            break
        new_app_run = NewExecution(
            "Do you want add new triangle?\n" "If yes, please type 'y' or 'yes'\n"
        ).choose_action()
        if not new_app_run:
            break
    triangles_sorted.print_triangles()
