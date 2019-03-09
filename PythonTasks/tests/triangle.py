from models.triangles_algorithm import Triangle, TriangleList


class TestTriangle:
    def test_square_calculation_valid_output(self):
        output_list = ["first", 2.9]
        triangle = Triangle("first", 2.0, 3.0, 4.0).square_calculation()
        assert output_list == triangle

    def test_square_calculation_invalid_output(self):
        output_list = ["first", 2.9]
        triangle = Triangle("first", 2.5, 3.0, 4.0).square_calculation()
        assert output_list != triangle

    def test_square_calculation_negative_output(self):
        output_list = ["first", -2.9]
        triangle = Triangle("first", 2.0, 3.0, 4.0).square_calculation()
        assert output_list != triangle


class TestTriangleList:
    def test_add_triangle_invalid_square(self):
        triangle = ["first", 2.9]
        added_triangle = TriangleList().add_triangle(["first", 3.9])
        assert added_triangle != triangle

    def test_add_triangle_alpha_square(self):
        triangle = ["first", 2.1]
        added_triangle = TriangleList().add_triangle(["first", "second"])
        assert added_triangle != triangle

    def test_add_triangle_valid_square(self):
        triangle = ["first", 2.9]
        added_triangle = TriangleList().add_triangle(["first", 2.9])
        assert added_triangle == triangle
