"""This program has been created to check if the number or
 its part is a palindrome."""


def is_palindrome(input_value: str):
    if input_value == input_value[::-1]:
        return input_value
    else:
        return palindrome_part(input_value)


def is_palindrome_part(input_value: str) -> set:
    palindrome_list = list()
    start_index, stop_index = 0, 2

    for _ in range(len(input_value)-1):
        for _ in range(len(input_value)-1):
            slice_ = input_value[start_index:stop_index]
            stop_index += 1
            if slice_ == slice_[::-1]:
                palindrome_list.append(slice_)
        start_index += 1
        stop_index = start_index + 2

    if len(palindrome_list) > 0:
        palindrome_list = set(palindrome_list)
        return palindrome_list

    else:
        palindrome_list.append(0)
        palindrome_list = set(palindrome_list)
        return palindrome_list


def main():
    while True:
        try:
            is_palindrome = input("Please, enter alpha-numeric or special symbols: ")
            if isinstance(is_palindrome, str):
                break
        except ValueError:
            print("Please, enter value in string format")
    output_value = palindrome(is_palindrome)
    print(f"Your palindrome is: {output_value}")


if __name__ == '__main__':
    main()