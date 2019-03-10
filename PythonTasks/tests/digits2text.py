from models.digits2text_algorithm import TranslateInText


class TestTranslatorInText:
    def test_less_hundred_low_boundary_value(self):
        output_str = 'один'
        translate_instance = TranslateInText(1).less_hundred(1)
        assert output_str == translate_instance

    def test_less_hundred_high_boundary_value(self):
        output_str = 'девяносто девять'
        translate_instance = TranslateInText(99).less_hundred(99)
        assert output_str == translate_instance

    def test_less_hundred_invalid_output(self):
        output_str = '10'
        translate_instance = TranslateInText(10).less_hundred(10)
        assert output_str != translate_instance

    def test_hundreds_valid_low_boundary_value(self):
        output_str = 'сто'
        translate_instance = TranslateInText(100).hundreds(100)
        assert output_str == translate_instance

    def test_hundreds_valid_high_boundary_value(self):
        output_str = 'девятьсот девяносто девять'
        translate_instance = TranslateInText(999).hundreds(999)
        assert output_str == translate_instance

    def test_hundreds_invalid_output(self):
        output_str = '333'
        translate_instance = TranslateInText(333).hundreds(333)
        assert output_str != translate_instance

    def test_thousands_low_boundary_value(self):
        output_str = 'одна тысяча '
        translate_instance = TranslateInText(1000).thousands(1000)
        assert output_str == translate_instance

    def test_thousands_high_boundary_value(self):
        output_str = 'девятьсот девяносто девять тысяч девятьсот девяносто девять'
        translate_instance = TranslateInText(999999).thousands(999999)
        assert output_str == translate_instance

    def test_thousands_invalid_output(self):
        output_str = '3454'
        translate_instance = TranslateInText(3454).thousands(3454)
        assert output_str != translate_instance

    def test_numbers_to_text_zero(self):
        output_str = '0'
        translate_instance = TranslateInText(0).numbers_to_text()
        assert output_str != translate_instance

    def test_numbers_to_text_less_thousand(self):
        output_str = 'сорок семь'
        translate_instance = TranslateInText(47).numbers_to_text()
        assert output_str == translate_instance

    def test_numbers_to_text_less_million(self):
        output_str = 'восемьдесят семь тысяч двести тридцать пять'
        translate_instance = TranslateInText(87235).numbers_to_text()
        assert output_str == translate_instance

