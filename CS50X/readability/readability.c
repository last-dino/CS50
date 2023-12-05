#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int main(void)
{
    char *text = get_string("Text: ");
    int letter = 0, sentence = 0, word = 1;
    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            letter++;
        }
        if (isspace(text[i]))
        {
            word++;
        }
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentence++;
        }
    }
    double L, S;
    int index;
    L = (double) letter / word * 100;
    S = (double) sentence / word * 100;
    index = round(0.0588 * L - 0.296 * S - 15.8);

    if (index >= 1 && index <= 16)
    {
        printf("Grade %i\n", index);
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade 16+\n");
    }
    return 0;
}