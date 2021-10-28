#include <stdio.h>
#include <math.h>
#include <ctype.h>

int Newton_Raphson (double a, double b, double c, double err, double Xp, double *Xn)
{ 
  double delta;
  int count = 0;

  do { 
    if (2*a*Xp+b == 0){
      Xp = Xp+err;
    }else{
      delta = (a*Xp*Xp + b*Xp +c)/(2*a*Xp+b) ;
      *Xn = Xp - delta;
      Xp = *Xn;
      count++;
    }

  } while ((fabs(delta) > err) && count < 1000);

  if (count < 1000)
    return count;
  else
    return 0;
}

int main()
{   
  double x, x1,x2, a,b,c;
  char ch;
  int count = 0;

  do 
  {
    printf("\033[0;33mEnter parameter a = \033[0m");
    while (scanf("%lf%c", &a, &ch) == 0 || (isspace(ch) == 0))
    {
      rewind(stdin);
      printf("\033[0;31m    Input ERROR enter again: \033[0m");
    }
    rewind(stdin);

    printf("\033[0;33mEnter parameter b = \033[0m");
    while (scanf("%lf%c", &b, &ch) == 0 || (isspace(ch) == 0))
    {
      rewind(stdin);
      printf("\033[0;31m    Input ERROR enter again: \033[0m");
    }
    rewind(stdin);

    printf("\033[0;33mEnter parameter c = \033[0m");
    while (scanf("%lf%c", &c, &ch) == 0 || (isspace(ch) == 0))
    {
      rewind(stdin);
      printf("\033[0;31m    Input ERROR enter again: \033[0m");
    }
    rewind(stdin);

    count = Newton_Raphson (a, b, c, 0.000001, 123.456 , &x1);

    if (count == 0){
      printf("\033[0;31mError can't calculate\033[0m\n");
    }else{
      count = Newton_Raphson (a, b, c, 0.000001, -123.456 , &x2);

      if(fabs(x1-x2) < 0.00001){
        printf("\033[0;32manswer x = %g\033[0m\n", x1);
      }else{
        printf("\033[0;32manswer x1 = %g\033[0m\n", x1);
        printf("\033[0;32manswer x2 = %g\033[0m\n", x2);
      }
    }

    do { 
      printf("\033[0;36mEnter \033[0;32my\033[0;36m to calculate again or \033[0;31mn\033[0;36m to exit.\033[0m");
      scanf(" %c",&ch);
    } while(ch != 'n'&& ch != 'y');

  } while(ch == 'y');
}
