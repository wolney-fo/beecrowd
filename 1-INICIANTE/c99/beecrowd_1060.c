#include <stdio.h>

int main() {

    float num;
    int counter = 0;

    for (int i=0; i<6; i++) {
        scanf("%f", &num);

        if (num > 0) {
            ++counter;
        }
    }

    printf("%d valores positivos\n", counter);
    return 0;
}