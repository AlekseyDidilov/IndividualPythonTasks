from typing import Set, Any


class Palindrome:
    def __init__(self, value: str):
        self._value = value

    def is_palindrome(self) -> Any:
        if self._value == self._value[::-1]:
            return self._value
        else:
            return self.is_palindrome_as_part()

    def is_palindrome_as_part(self) -> Set[Any]:
        palindrome_list = list()
        start_index, stop_index = 0, 2

        for _ in range(len(self._value) - 1):
            for _ in range(len(self._value) - 1):
                slice_ = self._value[start_index:stop_index]
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
