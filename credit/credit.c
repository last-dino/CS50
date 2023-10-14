#include <cs50.h>
#include <stdio.h>

string validate(long num);

int main(void)
{
    long cardNumber = get_long("Number: ");
    string type = validate(cardNumber);
    printf("%s\n", type);
}

string validate(long num)
{
    int digit = 0;
    int sum = 0, pre = 0, cur = 0;
    while (num > 0)
    {
        if (digit % 2 == 0)
        {
            sum += num % 10;
        }
        else
        {
            int prod = (num % 10) * 2;
            if (prod > 9)
            {
                prod = prod / 10 + prod % 10;
            }
            sum += prod;
        }
        pre = cur;
        cur = num % 10;
        digit++;
        num /= 10;
    }

    if (sum % 10 != 0)
    {
        return "INVALID";
    }

    int beginningNum = cur * 10 + pre;

    if (digit == 15 && (beginningNum == 34 || beginningNum == 37))
    {
        return "AMEX";
    }
    if (digit == 16 && beginningNum > 50 && beginningNum < 56)
    {
        return "MASTERCARD";
    }
    if ((digit == 13 || digit == 16) && cur == 4)
    {
        return "VISA";
    }
    return "INVALID";
}