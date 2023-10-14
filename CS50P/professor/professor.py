import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        if generate_integer(level):
            score += 1
    print("Score:", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                raise ValueError
            break
        except ValueError:
            pass
    return level


def generate_integer(level):
    lb = 10**(level - 1) if level > 1 else 0
    ub = 10**level - 1

    num1, num2 = random.randint(lb, ub), random.randint(lb, ub)

    for _ in range(3):
        try:
            answer = int(input(f"{num1} + {num2} = "))
            if answer != num1 + num2:
                raise ValueError
            return True
        except ValueError:
            print("EEE")
    print(f"{num1} + {num2} = {num1 + num2}")
    return False


if __name__ == "__main__":
    main()