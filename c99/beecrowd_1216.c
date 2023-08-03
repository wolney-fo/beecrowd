#include <stdio.h>

int main() {

    char name[100];
    int counter = 0;
    int dist, sum;

    while (scanf("%[^\n]", &name) != EOF) {
        scanf("%d", &dist);
        sum += dist;
        ++counter;
    }

    printf("%.1f\n", (float) sum/counter);
    return 0;
}