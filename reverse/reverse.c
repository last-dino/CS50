#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    // TODO #1
    if (argc != 3)
    {
        printf("Usage: ./reverse input.wav output.wav");
        return 1;
    }

    // Open input file for reading
    // TODO #2
    char *dot = strrchr(&argv[1], '.');
    if (!dot || dot == &argv[1])
    {
        printf("Input is not a WAV file.\n");
        return 1;
    }
    char *ext = dot + 1;
    if (strcmp(ext, "wav") != 0)
    {
        printf("Input is not a WAV file.\n");
        return 1;
    }
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // Read header
    // TODO #3
    WAVHEADER header;
    fread(header, sizeof(header), 1, input);


    // Use check_format to ensure WAV format
    // TODO #4
    if (check_format(header) == 1)
    {
        printf("Input is not a WAV file.\n");
        return 1;
    }


    // Open output file for writing
    // TODO #5
    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // Write header to file
    // TODO #6
    fwrite(header, sizeof(header), 1, output);

    // Use get_block_size to calculate size of block
    // TODO #7

    // Write reversed audio to file
    // TODO #8
}

int check_format(WAVHEADER header)
{
    // TODO #4
    if (header.format[0] == 'W' && header.format[1] == 'A' && header.format[2] == 'V' && header.format[3] == 'E')
    {
        return 0;
    }
    return 1;
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    return 0;
}