#include <stdio.h>

int main() {

    char alp[] = "abcdefghijklmnopqrstuvwxyz";

    for (int i=0; i<26; i++) {
        printf("%d e %c\n", i+97, alp[i]);
    }
    return 0;
}