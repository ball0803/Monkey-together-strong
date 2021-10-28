#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <ctype.h>

#define g 9.81

void main()
{
    double speed, angle, distance, time, height;
    char answer, ch;
    printf("\033[0;36mThis program calcultae outcome of shooting of the to the goal with react time of 0.5 sec\033[0m");
    do
    {
        printf("\nEnter speed(m/s): ");
        while (scanf("%lf%c", &speed, &ch) == 0 || (isspace(ch) == 0))
        {
            rewind(stdin);
            printf("\033[0;31m    Input ERROR enter again: \033[0m");
        }
        rewind(stdin);

        printf("Enter angle(degree 1-90): ");
        while (scanf("%lf%c", &angle, &ch) == 0 || (isspace(ch) == 0) || angle < 1 || angle > 90)
        {
            rewind(stdin);
            printf("\033[0;31m    Input ERROR enter again: \033[0m");
        }
        rewind(stdin);
        angle = angle * M_PI / 180;

        printf("Enter distance(m): ");
        while (scanf("%lf%c", &distance, &ch) == 0 || (isspace(ch) == 0))
        {
            rewind(stdin);
            printf("\033[0;31m    Input ERROR enter again: \033[0m");
        }
        rewind(stdin);

        time = distance / (speed * cos(angle));
        height = (speed * sin(angle) * time) - ((g * (time * time)) / 2);
        if (height > 0)
        {
            if (height < 2.44)
            {
                if (time <= 0.5)
                {
                    printf("\n\033[0;36mAt goal line\033[0;33m ( %0.2lf m, %0.2lf sec)\033[0m\n", height, time);
                    printf("\033[0;32mGOAL!!\033[0m\n");
                }
                else
                {
                    printf("\n\033[0;36mAt goal line\033[0;33m ( %0.2lf m, %0.2lf sec)\033[0m\n", height, time);
                    printf("\033[0;31mGoalkeeper catch it\033[0m\n");
                }
            }
            else
            {
                printf("\n\033[0;36mAt goal line\033[0;33m ( %0.2lf m, %0.2lf sec)\033[0m\n", height, time);
                printf("\033[0;31mOvershoot :(\033[0m\n");
            }
        }
        else
        {
            time = (2 * speed * sin(angle)) / g;
            printf("\n\033[0;36mAt goal line\033[0;33m (it fall before reach goal %0.2lf m, %0.2lf sec)\033[0m\n", distance - ((speed * speed / g) * sin(2 * angle)), time);
            printf("\033[0;31mUndershoot :(\033[0m\n");
        }

        do
        {
            printf("\033[0;36mDo you wanna enter again? \033[0;32m[y]\033[0;36m for yes and \033[0;31m[n]\033[0;36m otherwise: \033[0m");
            rewind(stdin);
            scanf(" %c", &answer);
        } while (answer != 'y' && answer != 'n');
    } while (answer == 'y');
}