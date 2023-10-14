def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    return acceptableNumber(s) and correctFormat(s)

def acceptableNumber(plate):
    for i in range(1, len(plate)):
        if plate[i].isalpha() and plate[i - 1].isdigit():
            return False
        if plate[i].isdigit() and plate[i - 1].isalpha():
            if plate[i] == "0":
                return False
    return True

def correctFormat(plate):
    for c in plate:
        if not c.isalpha() and not c.isdigit():
            return False
    return True

main()