#include <stdio.h>
#include <math.h>

int main() {

    float a, b, c, d, r1, r2;
    scanf("%f %f %f", &a, &b, &c);

    d = (b*b) - (4*a*c);

    if (d < 0 || a == 0) {
            printf("Impossivel calcular");
        return 0;
    }

    r1 = ( (-1 * b) + sqrt(d) ) / (2*a);
    r2 = ( (-1 * b) - sqrt(d) ) / (2*a);

    printf("R1 = %.5f\n", r1);
    printf("R1 = %.5f\n", r2);

    return 0;
}
