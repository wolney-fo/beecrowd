#include <stdio.h>

int main() {
    int password;
    while (scanf("%d", &password) != EOF) {
        printf("%d\n", --password);
    }
    return 0;

}