from models.numbers import DIGITS


class TranslatorInText:

    def __init__(self, numbers: int):
        self.number = numbers
        self.translated_text = ""

    def less_hundred(self, number: int) -> str:
        if 1 <= number <= 9:
            self.translated_text = DIGITS["units"][number]
        elif 10 <= number <= 19:
            self.translated_text = DIGITS["teen"][number]
        elif number == 0:
            self.translated_text = DIGITS["units"][number]
        else:
            self.translated_text = DIGITS["tens"][number // 10] + \
                               " " + DIGITS["units"][number % 10]
        return self.translated_text

    def hundreds(self, number: int) -> str:
        if number <= 99:
            return self.less_hundred(number)
        if number % 100 == 0:
            self.translated_text += DIGITS["hundreds"][number // 100]
        else:
            self.translated_text += DIGITS["hundreds"][number // 100] + \
                                " " + self.less_hundred(number % 100)
        return self.translated_text

    def thousands(self, number: int) -> str:
        divided_thousand = number // 1000
        if (10 <= divided_thousand) and (10 <= (int((str(divided_thousand))[-2] +
                                                    (str(divided_thousand))[-1])) <= 19):

            thousand = self.hundreds(divided_thousand) + " тысяч"
        else:
            digit = int((str(divided_thousand))[-1])
            thousand = self.hundreds(divided_thousand) + " тыся" + \
                        DIGITS["thousands_ends"][digit]

        thousand = thousand.replace("один ", "одна ")
        thousand = thousand.replace("два ", "две ")
        self.translated_text = str()
        self.translated_text += thousand + " " + self.hundreds(number % 1000)
        return self.translated_text

    def numbers_to_text(self) -> str:
        number = self.number
        if number == 0:
            self.translated_text += DIGITS["zero"][number]
        elif 0 < number <= 999:
            self.translated_text += self.hundreds(number)
        elif 1 <= number // 1000 <= 999:
            self.translated_text = self.thousands(number)
        return self.translated_text




