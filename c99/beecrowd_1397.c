#include <stdio.h>

int main()
{

    int n, a, b, count_a, count_b;

    while (1)
    {
        scanf("%d", &n);

        if (n == 0)
        {
            break;
        }

        count_a = count_b = 0;

        for (int i = 0; i < n; i++)
        {
            scanf("%d %d", &a, &b);
            if (a > b)
            {
                count_a++;
            }
            else if (b > a)
            {
                count_b++;
            }
        }

        printf("%d %d\n", count_a, count_b);
    }
    return 0;
}