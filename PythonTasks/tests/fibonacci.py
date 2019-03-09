from models.fibonacci_algorithm import FibonacciRange, FibonacciLength


class TestFibonacciRange:
    def test_range_calculation_valid_output(self):
        fibonacci_output_list = [34, 55, 89, 144, 233, 377]
        fibonacci_instance = FibonacciRange(10, 15).range_calculation()
        assert fibonacci_output_list == fibonacci_instance

    def test_range_calculation_invalid_output(self):
        fibonacci_output_list = [20, 55, 89, 144, 233, 377]
        fibonacci_instance = FibonacciRange(10, 14).range_calculation()
        assert fibonacci_output_list != fibonacci_instance

    def test_range_calculation_invalid_seq_length(self):
        fibonacci_output_list = [55, 89, 144]
        fibonacci_instance = FibonacciRange(11, 12).range_calculation()
        assert fibonacci_output_list != fibonacci_instance

    def test_range_calculation_alpha_in_output(self):
        fibonacci_output_list = ["a", "b", 89, 144, 233, "f"]
        fibonacci_instance = FibonacciRange(8, 12).range_calculation()
        assert fibonacci_output_list != fibonacci_instance


class TestFibonacciLength:
    def test_length_calculation_valid_output(self):
        fibonacci_output_list = [144, 233, 377, 610, 987]
        fibonacci_instance = FibonacciLength(3).length_calculation()
        assert fibonacci_output_list == fibonacci_instance

    def test_length_calculation_invalid_output(self):
        fibonacci_output_list = [144, 233, 377, 610, 987]
        fibonacci_instance = FibonacciLength(4).length_calculation()
        assert fibonacci_output_list != fibonacci_instance

    def test_length_calculation_invalid_seq_length(self):
        fibonacci_output_list = [144, 233, 377, 610]
        fibonacci_instance = FibonacciLength(3).length_calculation()
        assert fibonacci_output_list != fibonacci_instance

    def test_length_calculation_in_output(self):
        fibonacci_output_list = [144, 233, 377, 610, "fib"]
        fibonacci_instance = FibonacciLength(3).length_calculation()
        assert fibonacci_output_list != fibonacci_instance
