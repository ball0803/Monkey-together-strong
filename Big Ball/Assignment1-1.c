#include <stdio.h>

void main()
{
    char test = 0;
    char ch;
    do
    {
        printf("\nAssignment 1.1 Program Test specific format of variable\n");
        printf("Enter value of test: ");
        scanf(" %c", &test);

        printf("print format of test\n");
        printf("int %%d = %d\n", test);
        printf("float %%f =%f\ndouble %%lf = %lf\n", test, test);
        printf("exponent %%e = %e\nsignificant %%g = %g\n", test, test);
        printf("char %%c = %c\n", &test);
        printf("Enter y to run again or n to exit.");
        scanf(" %c", &ch);

    } while (ch == 'y');
    printf("End Program\n");
}
