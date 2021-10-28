#include <stdio.h>
#include <math.h>
int main()
{
    double a, b, c, d; // รับinputเป็นจำนงนจริง
    double x, x1, x2, Re, Im;
    char ch;
    do
    {
        a = b = c = 0;
        printf("\nProgram calculate root of Equation ax^2+bx+c = 0\n");
        printf("Enter parameter a : ");
        // แก้format-character ให้ตรงกับตั;แปร
        scanf("%lf", &a);
        printf("Enter parameter b : ");
        scanf("%lf", &b);
        printf("Enter parameter c : ");
        scanf("%lf", &c); // เป็นpointer

        if (a == 0)
        {
            if (b != 0)
            {
                x = -c / b; //ตั;แปร X ผิด
                printf("This is linear equation\n");
                printf("Answer of %gx%+g=0 is\n", b, c);
                printf("x = %g\n", x); //""ปิดเกิน
            }
            else
            {
                printf("Error! invalid equation\n");
            }
        } //ร;มblock คำสั่ง
        else
        {
            if (pow(b, 2) - 4 * (a * c) >= 0)                       //ลืมเครื่องหมาย* cไม่มี ^
            {                                                       //ชื้อตั;แปรผิด
                x1 = (-b + sqrt((b * b - 4 * a * c))) / (2 * a);    //ลำดับการคูณผิดกับ * ข้างหน้า
                x2 = (-b - sqrt((b * b - 4 * a * c))) / (2 * a);    //ปิด;งเล็บผิด
                printf("root of %gx^2 %+gx %+g = 0 is\n", a, b, c); //ลืม;
                printf("x1 = %g\nx2 = %g\n", x1, x2);
            }
            else
            {
                Re = -b / 2 * a;                                                     //ลืม;
                Im = sqrt(fabs(((b * b) - (4 * a * c)))) / (2 * a);                  //ปิด;งเล็บผิด
                printf("root of %gx^2 + %gx + %g = 0 is complex number\n", a, b, c); //ตั;แปรแสดงผลผิด
                printf("x1 = %g + %gi\n", Re, Im);
                printf("x2 = %g - %gi\n", Re, Im);
                printf("i is square root of -1\n");
            }
        }
        do
        {
            printf("Enter y to calculate again or n to exit."); //ลืมปิดstring และ;
            scanf(" %c", &ch);
        } while (ch != 'y' && ch != 'n');
    } while (ch == 'y'); //char ใช้ '' ไม่ใช้ ""
    printf("\nEnd Program\n");
    return 0;
}
