#include "helpers.h"
#include <math.h>
#include <stdio.h>

void swap(RGBTRIPLE *pixel1, RGBTRIPLE *pixel2);
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE pixel = image[i][j];
            BYTE ave = round((pixel.rgbtRed + pixel.rgbtGreen + pixel.rgbtBlue) / 3.0);
            image[i][j].rgbtRed = ave;
            image[i][j].rgbtGreen = ave;
            image[i][j].rgbtBlue = ave;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        int left = 0;
        int right = width - 1;
        while (left < right)
        {
            swap(&image[i][left], &image[i][right]);
            left++;
            right--;
        }
    }
    return;
}

void swap(RGBTRIPLE *pixel1, RGBTRIPLE *pixel2)
{
    RGBTRIPLE temp = *pixel1;
    *pixel1 = *pixel2;
    *pixel2 = temp;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE blurred[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int red = 0, green = 0, blue = 0;
            double counter = 0.0;
            for (int di = -1; di <= 1; di++) {
                int ni = i + di;
                for (int dj = -1; dj <= 1; dj++) {
                    int nj = j + dj;

                    if (ni >= 0 && ni < height && nj >= 0 && nj < width) {
                        red += image[ni][nj].rgbtRed;
                        green += image[ni][nj].rgbtGreen;
                        blue += image[ni][nj].rgbtBlue;
                        counter++;
                    }
                }
            }
            blurred[i][j].rgbtRed = round(red / counter);
            blurred[i][j].rgbtGreen = round(green / counter);
            blurred[i][j].rgbtBlue = round(blue / counter);
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = blurred[i][j];
        }
    }
    return;
}

// Detect edges

int min(int x, int y)
{
    return x < y? x : y;
}

void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE edge[height][width];
    int Gx[9] = {-1, 0, 1, -2, 0, 2, -1, 0, 1};
    int Gy[9] = {-1, -2, -1, 0, 0, 0, 1, 2, 1};
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int red_x = 0, green_x = 0, blue_x = 0, red_y = 0, green_y = 0, blue_y = 0;
            int counter = 0;
            for (int di = -1; di <= 1; di++) {
                for (int dj = -1; dj <= 1; dj++) {
                    int ni = i + di;
                    int nj = j + dj;

                    if (ni >= 0 && ni < height && nj >= 0 && nj < width)
                    {
                        red_x += image[ni][nj].rgbtRed * Gx[counter];
                        green_x += image[ni][nj].rgbtGreen * Gx[counter];
                        blue_x += image[ni][nj].rgbtBlue * Gx[counter];
                        red_y += image[ni][nj].rgbtRed * Gy[counter];
                        green_y += image[ni][nj].rgbtGreen * Gy[counter];
                        blue_y += image[ni][nj].rgbtBlue * Gy[counter];

                    }
                    counter++;
                }
            }
            edge[i][j].rgbtRed = min(round(sqrt(red_x * red_x + red_y * red_y)), 255);
            edge[i][j].rgbtGreen = min(round(sqrt(green_x * green_x + green_y * green_y)), 255);
            edge[i][j].rgbtBlue = min(round(sqrt(blue_x * blue_x + blue_y * blue_y)), 255);
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = edge[i][j];
        }
    }
    return;
}
