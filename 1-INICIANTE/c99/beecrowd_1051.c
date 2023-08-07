#include <stdio.h>

int main() {

    float sal, val, temp;
    scanf("%f", &sal);

    if (sal <= 2000) {
        printf("Isento\n");
        return 0;
    }

    val = 0;

    if (sal > 4500) {
        temp = sal - 4500;
        val += temp * 0.28;
        sal -= temp;
    }

    if (sal >= 3000.01) {
        temp = sal - 3000;
        val += temp * 0.18;
        sal -= temp;
    }

    if (sal >= 2000.01) {
        temp = sal - 2000;
        val += temp * 0.08;
    }

    printf("R$ %.2f\n", val);

    return 0;
}