from models.chessboard_algorithm import Chessboard


class TestChessboard:
    def test_chessboard_building_valid_output(self):
        output_list = ["* * *", " * * ", "* * *", " * * ", "* * *"]
        chessboard_instance = Chessboard(5, 5).chessboard_building()
        assert output_list == chessboard_instance

    def test_chessboard_building_invalid_first_line(self):
        output_list = [" * * ", " * * ", "* * *", " * * ", "* * *"]
        chessboard_instance = Chessboard(5, 5).chessboard_building()
        assert output_list != chessboard_instance

    def test_chessboard_building_invalid_size(self):
        output_list = [" * * ", " * * ", "* * *", " * * "]
        chessboard_instance = Chessboard(5, 5).chessboard_building()
        assert output_list != chessboard_instance
