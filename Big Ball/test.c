#include <stdio.h>
int main()
{
    int num1, num2;
    printf(" * switch control structure ***\n");
    printf("Enter 2 number : ");
    scanf("%d %d", &num1, &num2);
    int sum_num = num1 + num2;
    switch (sum_num)
    {
    case 0:
    case 1:
    case 2:
    case 3:
    case 4:
        printf("%d is Less than 5\n", num1 + num2);
        break;
    case 5:
        printf("Equals\n");
        break;
    case 6:
    case 7:
    case 8:
    case 9:
    case 10:
        printf("%d is More than 5\n", num1 + num2);
        break;

    default:
        printf("ERROR\n");
        break;
    }

    return 0;
}