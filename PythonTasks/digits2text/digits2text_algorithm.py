from digits2text.numbers import DIGITS


class TranslatorInText:

    def __init__(self, numbers: int):
        self.number = numbers
        self.output_text = ""

    def numbers_less_100(self, number: int) -> str:
        if 1 <= number <= 9:
            self.output_text = DIGITS["units"][number]
        elif 10 <= number <= 19:
            self.output_text = DIGITS["teen"][number]
        elif number == 0:
            self.output_text = DIGITS["units"][number]
        else:
            self.output_text = DIGITS["tens"][number // 10] + \
                               " " + DIGITS["units"][number % 10]
        return self.output_text

    def numbers_from_100_to_999(self, number: int) -> str:
        if number <= 99:
            return self.numbers_less_100(number)
        if number % 100 == 0:
            self.output_text += DIGITS["hundreds"][number // 100]
        else:
            self.output_text += DIGITS["hundreds"][number // 100] + \
                                " " + self.numbers_less_100(number % 100)
        return self.output_text

    def thousands(self, number: int) -> str:
        thousand_count = number // 1000
        if (10 <= thousand_count) and (10 <= (int((str(thousand_count))[-2] +
                                                  (str(thousand_count))[-1])) <= 19):

            thousand = self.numbers_from_100_to_999(thousand_count) + " тысяч"
        else:
            digit = int((str(thousand_count))[-1])
            thousand = self.numbers_from_100_to_999(thousand_count) + " тыся" + \
                       DIGITS["thousands_ends"][digit]

        thousand = thousand.replace("один ", "одна ")
        thousand = thousand.replace("два ", "две ")
        self.output_text = str()
        self.output_text += thousand + " " + self.numbers_from_100_to_999(number % 1000)
        return self.output_text

    def numbers_to_text(self) -> str:
        number = self.number
        if number == 0:
            self.output_text += DIGITS["zero"][number]
        elif 0 < number <= 999:
            self.output_text += self.numbers_from_100_to_999(number)
        elif 1 <= number // 1000 <= 999:
            self.output_text = self.thousands(number)
        return self.output_text




