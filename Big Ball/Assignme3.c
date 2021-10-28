#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>

void main()
{
    int randomNum, guessNum, count;
    char answer, ch, name[20];

    printf("What is your name: ");
    gets(name);
    printf("\n\033[0;36mHello %s this program is a guessing game it will random numbers between 1-100\nyou have 7 turns to guess and you have to guess it if your guess is higher than the answer if lower otherwise\n\033[0m", name);

    do
    {

        srand(time(0));
        randomNum = rand() % 100 + 1;
        count = 0;
        printf("answer is %d\n", randomNum);

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
                printf("\033[0;32mNice one! %s you guess is right!\033[0m\n", name);
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
                    printf("\033[0;31mToo bad %s the number is %d\033[0m\n", name, randomNum);
                }
            }
        } while (guessNum != randomNum && count != 7);
        do
        {
            printf("\033[0;36mDo you wanna play again? enter \033[0;32m[y]\033[0;36m for yes and \033[0;31m[n]\033[0;36m otherwise: \033[0m");
            scanf(" %c", &answer);

        } while (answer != 'y' && answer != 'n');
    } while (answer == 'y');
    printf("Good bye");
}