"""This program has been created to convert numbers which
inputted as digits and translate in text representation."""

digits_dictionary = {
        "zero": {0: "ноль"},
        "units": {
            1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть",
            7: "семь", 8: "восемь", 9: "девять", 0: ""
        },
        "tens": {
            2: "двадцать", 3: "тридцать", 4: "сорок", 5: "пятьдесят",
            6: "шестьдесят", 7: "семьдесят", 8: "восемьдесят", 9: "девяносто"
        },
        "hundreds": {
            1: "сто", 2: "двести", 3: "триста", 4: "четыреста", 5: "пятьсот",
            6: "шестьсот", 7: "семьсот", 8: "восемьсот", 9: "девятьсот"
        },
        "teen": {
            10: "десять", 11: "одинадцать", 12: "двенадцать", 13: "тринадцать",
            14: "четырнадцать", 15: "пятнадцать", 16: "шестнадцать", 17: "семнадцать",
            18: "восемнадцать", 19: "девятнадцать"
        },
        "thousands_ends": {
            1: "ча", 2: "чи", 3: "чи", 4: "чи", 5: "ч", 6: "ч", 7: "ч", 8: "ч",
            9: "ч", 0: "ч"
        }
    }


def numbers_less_100(number: int) -> str:
    if 1 <= number <= 9:
        output_text = digits_dictionary["units"][number]
    elif 10 <= number <= 19:
        output_text = digits_dictionary["teen"][number]
    elif number == 0:
        output_text = digits_dictionary["units"][number]
    else:
        output_text = digits_dictionary["tens"][number // 10] + \
                      " " + digits_dictionary["units"][number % 10]
    return output_text


def numbers_from_100_to_999(number: int) -> str:
    output_text = ""
    if number <= 99:
        return numbers_less_100(number)
    if number % 100 == 0:
        output_text += digits_dictionary["hundreds"][number // 100]
    else:
        output_text += digits_dictionary["hundreds"][number // 100] + \
                       " " + numbers_less_100(number % 100)
    return output_text


def thousands(number: int) -> str:
    output_text = ""
    thousand_count = number // 1000
    if (10 <= thousand_count) and (10 <= (int((str(thousand_count))[-2] +
                                  (str(thousand_count))[-1])) <= 19):

        thousand = numbers_from_100_to_999(thousand_count) + " тысяч"
    else:
        digit = int((str(thousand_count))[-1])
        thousand = numbers_from_100_to_999(thousand_count) + " тыся" + \
                   digits_dictionary["thousands_ends"][digit]

    thousand = thousand.replace("один ", "одна ")
    thousand = thousand.replace("два ", "две ")
    output_text += thousand + " " + numbers_from_100_to_999(number % 1000)
    return output_text


def numbers_to_text(number: int) -> str:
    output_text = ""
    if number == 0:
        output_text += digits_dictionary["zero"][number]
    elif 0 < number <= 999:
        output_text += numbers_from_100_to_999(number)
    elif 1 <= number // 1000 <= 999:
        output_text = thousands(number)
    return output_text


def validation_input_data() -> int:
    while True:
        try:
            entered_value = int(input(f"Please, enter integer number between 0 to 1000000: "))

            if 0 <= entered_value < 1000000:
                break
        except ValueError:
            print("Please, enter integer")
    return entered_value


def main():
    digits_convert = numbers_to_text(validation_input_data())

    print(f"Number was converted in: {digits_convert}")


if __name__ == "__main__":
    main()
