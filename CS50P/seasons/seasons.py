import datetime
import inflect
import re
import sys



def main():
    print(convert(input("Date of Birth: ")))


def convert(s):
    match = re.search(r"^([0-9]{1,4})-(1[0-2]|0[1-9])-(0[1-9]|[1-2][0-9]|3[0-1])$", s)
    if match:
        year = int(match.group(1))
        month = int(match.group(2))
        day = int(match.group(3))
    else:
        sys.exit("Invalid date")

    p = inflect.engine()
    try:
        delta = datetime.date.today() - datetime.date(year, month, day)
    except ValueError:
        sys.exit("Invalid date")
    word = p.number_to_words(delta.days * 24 * 60, andword="").capitalize()
    return f"{word} minutes"

if __name__ == "__main__":
    main()