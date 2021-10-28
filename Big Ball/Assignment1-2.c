#include <stdio.h>

void main()
{
    char test[40];
    char ch;

    do
    {
        printf("\nAssignment 1.2 Program Test specific format of variable\n");
        printf("Enter value of test: ");
        scanf("%s", test);

        printf("print format of test\n");
        printf("string %%s = \"%s\"\n", test);
        printf("char %%c = \"%c\"\n", test);
        printf("int %%d = \"%d\"\n", test);
        printf("double %%lf = %lf\n", test);
        printf("Enter y to run again or n to exit.");
        scanf(" %c", &ch);

    } while (ch == 'y');
    printf("End Program\n");
}