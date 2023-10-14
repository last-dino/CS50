import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match =  re.search(r"\"(https?://)(?:www.)?(youtu)(be)\.com/embed(/.+)\"", s)
    if match:
        return f"https://{match.group(2)}.{match.group(3)}{match.group(4)}"
    return None

if __name__ == "__main__":
    main()