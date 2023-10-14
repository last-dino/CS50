def main():
    print(fuel_percentage())

def fuel_percentage():
    while True:
        try:
            fraction = input("Fraction: ")
            numer, denom = fraction.split("/")
            percentage = round(int(numer)/int(denom) * 100)
            if percentage > 100:
                continue
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    return f"{percentage}%"

main()