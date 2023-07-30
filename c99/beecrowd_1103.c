#include <stdio.h>

int main()
{
    int h1, m1, h2, m2, ht, mt;

    while (h1 != EOF)
    {
        scanf("%d %d %d %d", &h1, &m1, &h2, &m2);
        if (h1 == 0 && m1 == 0 && h2 == 0 && m2 == 0) {
            break;
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
            if (h1 == h2) {
                ht = 23;
            } else {
                ht--;
            }
            mt = (60 - m1) + m2;
        }
        else
        {
            mt = m2 - m1;
        }

        mt += 60 * ht;

        printf("%d\n", mt);
    }

    return 0;
}