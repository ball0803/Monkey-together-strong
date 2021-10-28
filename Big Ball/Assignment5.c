#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>

int getInt(int min, int max)
{
    int number;
    char ch;
    rewind(stdin);
    if (scanf("%d%c", &number, &ch) == 0)
    {
        printf("\033[0;31mNo number given enter again: \033[0m ");
        number = getInt(min, max);
    }
    else if (!isspace(ch))
    {
        printf("\033[0;31mNot a number enter again: \033[0m ");
        number = getInt(min, max);
    }
    else if (number < min || number > max)
    {
        printf("\033[0;31mNumber out off range enter number between %d - %d: \033[0m ", min, max);
        number = getInt(min, max);
    }
    rewind(stdin);
    return number;
}

int factorial(int n)
{
    int answer = 1;
    for (int i = 0; i <= n; i++)
    {
        if (i <= 1)
        {
            answer *= 1;
        }
        else
        {
            answer *= i;
        }
    }
    return answer;
}

int getMenu()
{
    int select;
    printf(" \033[0;36m***********************************************\n");
    printf(" \033[0;36m*              \033[0;33mMy Test function\033[0m               \033[0;36m*\n");
    printf(" \033[0;36m***********************************************\n");
    printf(" \033[0;36m* \033[0;33m1. Fibonacci function\033[0m                       \033[0;36m*\n");
    printf(" \033[0;36m* \033[0;33m2. Combination number\033[0m                       \033[0;36m*\n");
    printf(" \033[0;36m* \033[0;33m3. Find GCD(x,y)\033[0m                            \033[0;36m*\n");
    printf(" \033[0;36m* \033[0;33m4. Random Guess Number\033[0m                      \033[0;36m*\n");
    printf(" \033[0;36m* \033[0;31m0. exit\033[0m                                     \033[0;36m*\n");
    printf(" \033[0;36m***********************************************\n");
    printf(" \033[0;33mEnter menu number:\033[0m ");
    select = getInt(0, 4);
    return select;
}

int fibonacci(int n, int *memory)
{

    if (memory[n] == -1)
    {
        memory[n] = fibonacci(n - 1, memory) + fibonacci(n - 2, memory);
    }
    return memory[n];
}

int GCD(int m, int n)
{
    int answer = m;
    while (m % answer != 0 || n % answer != 0)
        answer -= 1;
    return answer;
}

int nCr(int n, int r)
{
    return factorial(n) / (factorial(r) * factorial(n - r));
}

void main()
{
    int select, n, r, count, guessNum, randomNum;
    int memory[46];
    char ch;

    do
    {
        select = getMenu();
        switch (select)
        {
        case 1:
            printf("\n\033[0;36mCalculate fibonacci number\033[0m\n");
            printf("\033[0;33mEnter fibonacci term f(n)(0-45) : \033[0m");
            n = getInt(0, 45);

            for (int i = 0; i < 45; i++)
            {
                memory[i] = -1;
            }

            memory[0] = 0;
            memory[1] = 1;
            printf("\033[0;32mFibonacci of %d is : %d\033[0m\n", n, fibonacci(n, memory));
            break;

        case 2:
            printf("\n\033[0;36mCalculate Combination number \033[0m\n");
            printf("Enter n : ");
            while (scanf("%d%c", &n, &ch) == 0 || (isspace(ch) == 0) || n < 0)
            {
                rewind(stdin);
                printf("\033[0;31m    Input ERROR enter again: \033[0m");
            }
            rewind(stdin);
            printf("Enter r : ");
            while (scanf("%d%c", &r, &ch) == 0 || (isspace(ch) == 0) || r < 0 || r > n)
            {
                rewind(stdin);
                printf("\033[0;31m    Input ERROR enter again: \033[0m");
            }
            rewind(stdin);

            printf("\033[0;32mCombination number of %d and %d : %d\033[0m\n", n, r, nCr(n, r));
            break;

        case 3:
            printf("\n\033[0;36mCalculate Greatest Common Divisor \033[0m\n");
            printf("Enter first number : ");
            while (scanf("%d%c", &n, &ch) == 0 || (isspace(ch) == 0))
            {
                rewind(stdin);
                printf("\033[0;31m    Input ERROR enter again: \033[0m");
            }
            rewind(stdin);
            printf("Enter second number : ");
            while (scanf("%d%c", &r, &ch) == 0 || (isspace(ch) == 0) || r < 0)
            {
                rewind(stdin);
                printf("\033[0;31m    Input ERROR enter again: \033[0m");
            }
            rewind(stdin);

            printf("\033[0;32mGreatest Common Divisor of %d and %d : %d\033[0m\n", n, r, GCD(n, r));
            break;

        case 4:
            srand(time(0));
            randomNum = rand() % 100 + 1;
            count = 0;
            // printf("answer is %d\n", randomNum);
            printf("\n");
            do
            {
                count++;
                printf("%d). Guess number between 1-100: ", count);

                while (scanf("%d%c", &guessNum, &ch) == 0 || (isspace(ch) == 0) || guessNum < 1 || guessNum > 100)
                {
                    rewind(stdin);
                    printf("\033[0;31m    Input ERROR enter again: \033[0m");
                }
                rewind(stdin);

                if (guessNum == randomNum)
                {
                    printf("\033[0;32mNice one! you guess is right!\033[0m\n");
                }
                else
                {
                    if (guessNum > randomNum)
                    {
                        printf("\033[0;33m    %d is higher than actual answer\033[0m\n", guessNum);
                    }
                    else
                    {
                        printf("\033[0;33m    %d is lower than actual answer\033[0m\n", guessNum);
                    }
                    if (count == 7)
                    {
                        printf("\033[0;31mToo bad the number is %d\033[0m\n", randomNum);
                    }
                }
            } while (guessNum != randomNum && count != 7);
            break;
        }
    } while (select != 0);
}
