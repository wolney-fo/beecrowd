#include <stdio.h>

int main()
{

    int n, counter;

    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        counter = 0;

        int t;
        scanf("%d", &t);

        int tiros[50];
        for (int j = 0; j < t; j++)
        {
            scanf("%d", &tiros[j]);
        }

        char pulos[50];
        scanf("%s", pulos);

        for (int acao = 0; acao < t; acao++)
        {
            if ((tiros[acao] <= 2 && pulos[acao] == 'S') || (tiros[acao] > 2 && pulos[acao] == 'J'))
            {
                counter++;
            }
        }

        printf("%d\n", counter);
    }
    return 0;
}