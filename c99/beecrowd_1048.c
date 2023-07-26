#include <stdio.h>

int main() {

    float sal, nSal, porc;
    scanf("%f", &sal);


    if (sal <= 400.0) {
        porc = 0.15;
    } else if (sal <= 800.0) {
        porc = 0.12;
    } else if (sal <= 1200) {
        porc = 0.1;
    } else if (sal <= 2000) {
        porc = 0.07;
    } else {
        porc = 0.04;
    }

    nSal = sal + sal*porc;
    
    printf("Novo salario: %.2f\n", nSal);
    printf("Reajuste ganho: %.2f\n", nSal-sal);
    printf("Em percentual: %.0f %\n", porc*100);

    return 0;
}