// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <strings.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;
int count = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int index = hash(word);
    node *ptr = table[index];
    while (ptr != NULL)
    {
        if (strcasecmp(word, ptr->word) == 0)
        {
            return true;
        }
        ptr = ptr->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *in_file = fopen(dictionary, "r");
    if (in_file == NULL)
    {
        return false;
    }
    char *word = malloc(LENGTH + 1);
    if (word == NULL)
    {
        return false;
    }
    while (fscanf(in_file, "%s", word) != EOF)
    {
        node *single_word = malloc(sizeof(node));
        if (single_word == NULL)
        {
            return false;
        }
        strcpy(word, single_word->word);
        int index = hash(single_word->word);
        single_word->next = table[index];
        table[index] = single_word;
        count++;
    }
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
         node *ptr = table[i];
         node *next = ptr;
         while (ptr != NULL)
         {
             next = ptr->next;
             free(ptr);
             ptr = next;
         }
         table[i] = NULL;
    }
    if (table[0] != NULL)
    {
        return false;
    }
    return true;
}
