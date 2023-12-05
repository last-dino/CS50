def main():
    cardNumber = int(input("Number: "))
    print(validate(cardNumber))


def validate(num):
    digit = 0
    sum, pre, cur = 0, 0, 0
    while num > 0:
        if digit % 2 == 0:
            sum += num % 10
        else:
            prod = (num % 10) * 2

            if prod > 9:
                prod = prod // 10 + prod % 10
            sum += prod

        pre = cur
        cur = num % 10
        digit += 1
        num //= 10

    if sum % 10 != 0:
        return "INVALID"

    beginningNum = cur * 10 + pre

    if digit == 15 and (beginningNum == 34 or beginningNum == 37):
        return "AMEX"

    if digit == 16 and beginningNum > 50 and beginningNum < 56:
        return "MASTERCARD"

    if (digit == 13 or digit == 16) and cur == 4:
        return "VISA"

    return "INVALID"


if __name__ == "__main__":
    main()
