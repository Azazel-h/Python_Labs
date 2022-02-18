#include <stdio.h>

float** calculate_new_v_and_t(float first_V, float second_V, float first_temperature, float second_temperature, float **result_array);
float mass_calculation(float V, float ro);
float** test(float** some);

int main(void)
{
    float first_V, second_V, first_temperature, second_temperature;
    printf("Введите V1, T1: ");
    scanf("%f%f", &first_V, &first_temperature);
    printf("Введите V2, T2: ");
    scanf("%f%f", &second_V, &second_temperature);

    float* new_V_T[2];
    new_V_T = test(new_V_T);
    //new_V_T = calculate_new_v_and_t(first_V, second_V, first_temperature, second_temperature, new_V_T);
    printf("Итоговые значения V, T: %f%f", *new_V_T[0], *new_V_T[1]);
}

float** test(float** some)
{
    some[0] = 0;
    some[1] = 1;
    return some;
}

float* calculate_new_v_and_t(float first_V, float second_V, float first_temperature, float second_temperature, float *result_array)
{
    float water_ro = 997, first_mass, second_mass;
    first_mass = mass_calculation(first_V, water_ro);
    second_mass = mass_calculation(second_V, water_ro);

    float new_V, new_temperature;
    new_V = first_V + second_V;
    new_temperature = (first_mass * first_temperature + second_mass * second_temperature) / (first_mass + second_mass);
    result_array[0] = new_V;
    result_array[1] = new_temperature;

    return result_array;
}