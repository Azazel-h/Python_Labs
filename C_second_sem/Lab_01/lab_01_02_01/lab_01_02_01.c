#include <stdio.h>
#include <math.h>

float calculate_s(float a, float b, float fi);

int main(void)
{
    float a, b, fi;
    scanf("%f%f%f", &a, &b, &fi);
    printf("S: %f", calculate_s(a, b, fi));
}

float calculate_s(float a, float b, float fi)
{

    return a * b * sinf(fi);
};