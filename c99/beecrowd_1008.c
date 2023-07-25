#include <stdio.h>

int main() {

    int id, hours;
    float perh;

    scanf("%d", &id);
    scanf("%d", &hours);
    scanf("%f", &perh);

    printf("NUMBER = %d\n", id);
    printf("SALARY = U$ %.2f\n", hours*perh);

    return 0;
}
