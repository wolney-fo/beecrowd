#include <stdio.h>

int main()
{

    char tab[4][9] = {"Rolien", "Naej", "Elehcim", "Odranoel"};
    int _, n, inp;

    scanf("%d", &_);
    for (int i = 0; i < _; i++)
    {
        scanf("%d", &n);
        for (int j = 0; j < n; j++)
        {
            scanf("%d", &inp);
            printf("%s\n", tab[inp - 1]);
        }
    }
    return 0;
}