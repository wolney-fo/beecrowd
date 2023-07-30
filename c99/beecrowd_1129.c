#include <stdio.h>

int main()
{

    int quests = 1;
    int counter, answer;
    char ans[6] = "ABCDE*";
    int inp[5];

    while (quests != 0)
    {
        scanf("%d", &quests);

        for (int i = 0; i < quests; i++)
        {
            scanf("%d %d %d %d %d", &inp[0], &inp[1], &inp[2], &inp[3], &inp[4]);
            counter = 0;

            for (int i = 0; i <= 5; i++)
            {

                if (inp[i] <= 127)
                {
                    answer = i;
                    counter++;
                }
            }

            (counter == 1) ? printf("%c\n", ans[answer]) : printf("%c\n", ans[5]);
        }
    }
    return 0;
}