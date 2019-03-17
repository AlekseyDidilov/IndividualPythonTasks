import sys
from models.parser_algorithm import ParserCount, ParserReplace


if __name__ == "__main__":
    if len(sys.argv) == 3:
        new_parser = ParserCount(
            sys.argv[1],
            sys.argv[2]
        ).text_count()
    elif len(sys.argv) == 4:
        new_parser = ParserReplace(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        )
        text_changing = new_parser.preparing_replace()
        new_parser.replace_text(text_changing)
    else:
        print("Invalid data has been entered!")
