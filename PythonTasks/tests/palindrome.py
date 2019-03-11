from models.palindrome_algorithm import Palindrome


class TestPalindrome:
    def test_is_palindrome_valid_output(self):
        output_value = "12321"
        palindrome_instance = Palindrome("12321").is_palindrome()
        assert output_value == palindrome_instance

    def test_is_palindrome_alpha_numeric_value(self):
        output_value = "12a21"
        palindrome_instance = Palindrome("12a21").is_palindrome()
        assert output_value == palindrome_instance

    def test_is_palindrome_output_half(self):
        output_value = "12"
        palindrome_instance = Palindrome("1221").is_palindrome()
        assert output_value != palindrome_instance

    def test_is_palindrome_as_part_one_entrance(self):
        output_value = {"44"}
        palindrome_instance = Palindrome("12344").is_palindrome_as_part()
        assert output_value == palindrome_instance

    def test_is_palindrome_as_part_two_entrance(self):
        output_value = {"44", "77"}
        palindrome_instance = Palindrome("123445677").is_palindrome_as_part()
        assert output_value == palindrome_instance

    def test_is_palindrome_as_part_zero_entrance(self):
        output_value = {"0"}
        palindrome_instance = Palindrome("1234567").is_palindrome_as_part()
        assert output_value == palindrome_instance

    def test_is_palindrome_as_part_output_half(self):
        output_value = {"7"}
        palindrome_instance = Palindrome("12345677").is_palindrome_as_part()
        assert output_value != palindrome_instance
