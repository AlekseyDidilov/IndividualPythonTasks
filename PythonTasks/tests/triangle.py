from models.triangles_algorithm import Triangle


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



