#include <stdio.h>

int main()
{
    int h1, m1, h2, m2, ht, mt;

    scanf("%d %d %d %d", &h1, &m1, &h2, &m2);

    if (h1 == h2 && m1 == m2 && h1 == m1) {
        printf("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)\n");
        return 0;
    }

    if (h2 < h1)
    {
        ht = (24 - h1) + h2;
    }
    else
    {
        ht = h2 - h1;
    }

    if (m2 < m1)
    {
        if (h1 == h2)
        {
            ht = 23;
        }
        else
        {
            ht--;
        }
        mt = (60 - m1) + m2;
    }
    else
    {
        mt = m2 - m1;
    }

    printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", ht, mt);

    return 0;
}