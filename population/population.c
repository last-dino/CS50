#include <cs50.h>
#include <stdio.h>

int get_start_size(void);
int get_end_size(int n);
int get_year(int start, int end);

int main(void)
{
    int start_size = get_start_size();

    int end_size = get_end_size(start_size);

    int year = get_year(start_size, end_size);

    printf("Years: %i\n", year);
}

int get_start_size(void)
{
    int n;
    do
    {
        n = get_int("Start size: ");
    }
    while (n < 9);
    return n;
}

int get_end_size(int n)
{
    int m;
    do
    {
        m = get_int("End size: ");
    }
    while (m < n);
    return m;
}

int get_year(int start, int end)
{
    int year = 0;
    while (start < end)
    {
        start = start + (start / 3) - (start / 4);
        year++;
    }
    return year;
}