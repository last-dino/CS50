#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int BLOCK_SIZE = 512;
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }
    FILE *in_file = fopen(argv[1], "r");
    if (in_file == NULL)
    {
        printf("Could not open input file.\n");
        return 1;
    }
    BYTE buffer[BLOCK_SIZE];
    int file_number = 0;
    char filename[8];
    FILE *img = NULL;
    while (fread(buffer, 1, BLOCK_SIZE, in_file) == BLOCK_SIZE)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (img != NULL)
            {
                fclose(img);
            }
            sprintf(filename, "%03i.jpg", file_number);
            img = fopen(filename, "w");
            if (img == NULL)
            {
                printf("Could not create image file.\n");
                fclose(in_file);
                return 1;
            }
            file_number++;
        }
        else
        {
            fwrite(buffer, 1, BLOCK_SIZE, img);
        }
    }
    if (img != NULL)
    {
        fclose(img);
    }

    fclose(in_file);

    return 0;
}