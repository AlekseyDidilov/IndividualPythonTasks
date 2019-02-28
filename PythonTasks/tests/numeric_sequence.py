from models.numeric_sequence_algorithm import Sequence


class TestSequence:

    def test_sequence_calculation_valid_output(self):
        sequence_output_list = [5, 6, 7]
        sequence_instance = Sequence(3, 25).sequence_calculation()
        assert sequence_output_list == sequence_instance

    def test_sequence_calculation_invalid_output(self):
        sequence_output_list = [5.9, 6, 7]
        sequence_instance = Sequence(3, 25).sequence_calculation()
        assert sequence_output_list != sequence_instance

    def test_sequence_calculation_invalid_seq_length(self):
        sequence_output_list = [5.9, 6, 7]
        sequence_instance = Sequence(5, 25).sequence_calculation()
        assert sequence_output_list != sequence_instance

    def test_sequence_calculation_alpha_arg(self):
        sequence_list = ["a", 6, 7]
        sequence_instance = Sequence(3, 25).sequence_calculation()
        assert sequence_list != sequence_instance
