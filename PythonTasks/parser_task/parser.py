import sys


class Parser(object):
    def __init__(self, file):
        self.file = file

    def text_count(self, str_to_count) -> str:
        try:
            with open(self.file, 'r') as f:
                current_file = f.read()
                count_occur = current_file.count(str_to_count)
                print(count_occur)
                return f"{str_to_count}: has been found {count_occur} times"
        except FileNotFoundError:
            print("Required file hasn't been found!")

    def preparing_replace(self, old_str, new_str):
        try:
            with open(self.file, 'r') as f:
                current_file = f.read()
            current_file = current_file.replace(old_str, new_str)
            return current_file
        except FileNotFoundError:
            print("File hasn't been found!")
            quit()

    def replace_text(self, current_file):
        try:
            with open(self.file, 'w') as f:
                f.write(current_file)
            print("Text has been changed")
        except FileNotFoundError:
            print("File hasn't been found")


if __name__ == '__main__':
    if len(sys.argv) == 3:
        new_parser = Parser(sys.argv[1])
        print(new_parser.text_count(sys.argv[2]))
    elif len(sys.argv) == 4:
        new_parser = Parser(sys.argv[1])
        text_changing = new_parser.preparing_replace(sys.argv[2], sys.argv[3])
        new_parser.replace_text(text_changing)
    else:
        print("Invalid data has been entered!")


