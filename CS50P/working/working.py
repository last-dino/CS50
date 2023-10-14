import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError")


def convert(s):
    match = re.search(r"^((?:1[0-2])|[1-9])(?::([0-5][0-9]))? ((?:A|P)M) to ((?:1[0-2])|[1-9])(?::([0-5][0-9]))? ((?:A|P)M)$", s)
    if match:
        start_hour = int(match.group(1))
        start_day = match.group(3)
        end_hour = int(match.group(4))
        end_day = match.group(6)
        start_hour = fix_hour(start_hour, start_day)
        end_hour = fix_hour(end_hour, end_day)

        if not match.group(2):
            start_minute = "00"
        else:
            start_minute = match.group(2)

        if not match.group(5):
            end_minute = "00"
        else:
            end_minute = match.group(5)

        return f"{start_hour:02}:{start_minute} to {end_hour:02}:{end_minute}"

    raise ValueError

def fix_hour(hour, daytime):
    if daytime == "AM" and hour == 12:
        hour = 0
    if daytime == "PM" and hour != 12:
        hour += 12
    return hour


if __name__ == "__main__":
    main()