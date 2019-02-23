"""Create a console program that performs the output of triangles in descending order.
their area. After adding each new triangle, the program asks if user add one more.
If the user answers “y” or “yes” (case insensitive),the program will ask you to enter
data for another triangle, otherwise it displays result in the console.
- The calculation of the area of a triangle should be set using the Heron formula.
- Input format (comma separated): <Name>, <side_1>, <side_2>, <side_3>.
- An application must handle floating point numbers."""


from typing import Any, List
from abc import ABC, abstractmethod


class Input(ABC):

    @abstractmethod
    def inputted_data(self) -> Any:
        pass


class StrInput(Input):

    def __init__(self, value: str):
        self._value = value

    def inputted_data(self) -> List:
        return input(f"{self._value}").split(",")


class Requirements(ABC):

    @abstractmethod
    def passed(self, *value: Any) -> bool:
        pass


class StringLength(Requirements):

    def passed(self, value: List) -> bool:
        return len(value) == 4


class SidesFloat(Requirements):

    def passed(self, side_1: str, side_2:str, side_3: str) -> bool:
        try:
            float(side_1)
            float(side_2)
            float(side_3)
            return True
        except ValueError:
            print("Incorrect data, input must be in float!")


class SumTwoSides(Requirements):

    def passed(self, side_1: str, side_2: str, side_3: str) -> bool:
        return (float(side_1) + float(side_2) > float(side_3) and
                    float(side_1) + float(side_3) > float(side_2) and
                    float(side_2) + float(side_3) > float(side_1))


class LessZero(Requirements):

    def passed(self, side_1: str, side_2: str, side_3: str) -> bool:
        return min(float(side_1), float(side_2), float(side_3)) > 0


class CheckRequirements(Requirements):

    def __init__(self, *requirements: Any):
        self._test = requirements

    def passed(self, side_1: str, side_2: str, side_3: str) -> bool:
        for requirement in self._test:
            if not requirement.passed(side_1, side_2, side_3):
                print(f"{requirement.__class__.__name__} is failed.")
                return False
        return True


class Triangle:

    def __init__(self, name: str, side_1: float, side_2: float, side_3: float):
        self._name = name
        self._side_1 = side_1
        self._side_2 = side_2
        self._side_3 = side_3

    def square_calculation(self) -> List:
        perimeter = (self._side_1 + self._side_2 + self._side_3) / 2
        square = round(((perimeter * (perimeter - self._side_1) *
                                     (perimeter - self._side_2) *
                                     (perimeter - self._side_3)) ** 0.5), 2)

        triangle_name_square = list()
        triangle_name_square.append(self._name)
        triangle_name_square.append(square)
        return triangle_name_square


class TriangleList:

    def __init__(self):
        self.triangles = list()

    def add_triangle(self, triangle: List) -> List:
        return self.triangles.append(triangle)

    def print_triangles(self) -> None:
        sorted_triangles = sorted(self.triangles, reverse=True)
        if len(sorted_triangles) > 0:
            print("==== Triangle's list ====")
            for triangle, key in enumerate(sorted_triangles, 1):
                print(triangle, key, end="\n")


class NewExecution:

    def choose_action(self) -> bool:
        enter_choice = input("Do you want to continue, enter y or yes: ")
        if enter_choice.lower() in ("yes", "y"):
            return True
        return False


if __name__ == '__main__':
    triangles_sorted = TriangleList()
    while True:
        triangle_data = StrInput("Please, enter triangle name and size of sides \n"
                                 "Input format - 'name, side_a, side_b, side_c':\n"
                                ).inputted_data()
        checked_length = StringLength()
        checked_sides = CheckRequirements(SidesFloat(), SumTwoSides(), LessZero())
        if checked_length.passed(triangle_data) and \
            checked_sides.passed(
                                triangle_data[1],
                                triangle_data[2],
                                triangle_data[3]
                ):
            new_triangle = Triangle(
                                    str(triangle_data[0]),
                                    float(triangle_data[1]),
                                    float(triangle_data[2]),
                                    float(triangle_data[3])
                ).square_calculation()
            triangles_sorted.add_triangle(new_triangle)
        else:
            print("Inputted value isn't correct, please run program again!")
            break
        if not NewExecution().choose_action():
            break
    triangles_sorted.print_triangles()

