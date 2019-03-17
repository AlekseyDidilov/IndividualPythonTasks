from typing import Text


class ParserCount:
    def __init__(self, file: str, str_to_count: str):
        self.file = file
        self._str_to_count = str_to_count

    def text_count(self) -> None:
        try:
            with open(self.file, "r") as f:
                current_file = f.read()
                count_occur = current_file.count(self._str_to_count)
                print(f"{self._str_to_count}: has been found {count_occur} times")
        except FileNotFoundError:
            print("Required file hasn't been found!")


class ParserReplace:
    def __init__(self, file, old_str, new_str):
        self.file = file
        self._old_str = old_str
        self._new_str = new_str

    def preparing_replace(self) -> Text:
        try:
            with open(self.file, "r") as f:
                current_file = f.read()
            current_file = current_file.replace(self._old_str, self._new_str)
            return current_file
        except FileNotFoundError:
            print("File hasn't been found!")

    def replace_text(self, current_file) -> None:
        try:
            with open(self.file, "w") as f:
                f.write(current_file)
            print("Text has been changed")
        except FileNotFoundError:
            print("File hasn't been found")
