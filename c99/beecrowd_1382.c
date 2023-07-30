#include <stdio.h>

int main() {

    int l, r;

    while (1) {
        scanf("%d %d", &l, &r);

        if (l == r && r == 0) {
            break;
        }

        printf("%d\n", l+r);
    }
    return 0;
}