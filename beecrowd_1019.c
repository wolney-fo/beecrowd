#include <stdio.h>

int main() {

    int inp;
    scanf("%d", &inp);

    int hh = (inp / 3600);
    inp -= hh*3600;

    int mm = (inp / 60);
    inp -= mm*60;

    int ss = inp;

    printf("%d:%d:%d\n", hh, mm, ss);
    return 0;
}
