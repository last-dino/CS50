def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            if percentage > 100:
                continue
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

    print(gauge(percentage))

def convert(fraction):
    numer, denom = fraction.split("/")
    return round(int(numer)/int(denom) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    return f"{percentage}%"


if __name__ == "__main__":
    main()