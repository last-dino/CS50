#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

string cipher(string word, string key);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    int n = strlen(argv[1]);
    if (n != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    int key[26] = {0};
    for (int i = 0; i < n; i++)
    {
        if (argv[1][i] < 'A' || (argv[1][i] > 'Z' && argv[1][i] < 'a') || argv[1][i] > 'z')
        {
            printf("Key must only contain alphabetic characters.\n");
            return 1;
        }
        argv[1][i] = toupper(argv[1][i]);
        if (key[argv[1][i] - 'A'] == 1)
        {
            printf("Key must not contain repeated characters.\n");
            return 1;
        }
        key[argv[1][i] - 'A'] = 1;
    }

    string word = get_string("plaintext: ");
    string code = cipher(word, argv[1]);
    printf("ciphertext: %s\n", code);
}

string cipher(string word, string key)
{
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        if (word[i] >= 'A' && word[i] <= 'Z')
        {
            word[i] = key[word[i] - 'A'];
        }
        if (word[i] >= 'a' && word[i] <= 'z')
        {
            word[i] = tolower(key[toupper(word[i]) - 'A']);
        }
    }
    return word;
}