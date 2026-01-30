#include <stdio.h>
#include <string.h>

int main()
{
    char prod[10][20], left[10][5], right[10][20];
    int n, i, j;

    printf("Enter number of productions: ");
    scanf("%d", &n);

    printf("Enter productions (Example: A->abc|abd):\n");

    for(i = 0; i < n; i++)
    {
        scanf("%s", prod[i]);
        left[i][0] = prod[i][0];
        left[i][1] = '\0';
        strcpy(right[i], prod[i] + 3);
    }

    printf("\nAfter Left Factoring:\n");

    for(i = 0; i < n; i++)
    {
        char prefix[20];
        int k = 0;

        while(right[i][k] == right[i][k + 4])
        {
            prefix[k] = right[i][k];
            k++;
        }
        prefix[k] = '\0';

        printf("%s -> %s%s'\n", left[i], prefix, left[i]);
        printf("%s' -> %s | %s\n",
               left[i],
               right[i] + k,
               right[i] + k + 4);
    }

    return 0;
}
