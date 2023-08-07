#include <stdio.h>

int main() {

    float val, sum;
    int count;

    sum = count = 0;

    for (int i=0; i<6; i++) {
        scanf("%f", &val);
        if (val > 0) {
            sum += val;
            count++;
        }
    }

    printf("%d valores positivos\n", count);
    printf("%.1f\n", sum / count);

    return 0;
}