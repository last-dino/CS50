def main():
    while True:
        try:
            height = int(input("Height: "))
            if height > 0 and height < 9:
                break
        except ValueError:
            print("invalid input")

    pyramid(height)


def pyramid(n):
    for i in range(n):
        print(" " * (n - i - 1) + "#" * (i + 1) + "  " + "#" * (i + 1))


if __name__ == "__main__":
    main()
