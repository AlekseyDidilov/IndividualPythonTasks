from typing import List


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
            for triangle_name, triangle_square in enumerate(sorted_triangles, 1):
                print(triangle_name, triangle_square, end="\n")

