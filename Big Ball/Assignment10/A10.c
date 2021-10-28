#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <string.h>
#include <conio.h>

typedef struct info{
    long id;
    char name[50];
    double mid, final, accum, total, grade;
    char gradeLetter[3];
} student_info;

int read_file(char *filename, student_info table[]){
    FILE* fp = fopen(filename, "r");
    int i = 0, count = 0;
    student_info temp;
    if (fp != NULL){
        while(fscanf(fp, "%ld, %[^,], %lf, %lf, %lf", &temp.id, &temp.name, &temp.mid, &temp.final, &temp.accum) == 5){
            temp.total = temp.mid + temp.final + temp.accum;
            table[count++] = temp;
        }
        fclose(fp);
        return count;

    }else{
        printf("error can't open the file");
        return 0;
    }
}

int split(char *buff, char token[][20]){
    char *tok;
    int count = 0;
    tok = strtok(buff, ",");
    while(tok != NULL){
        strcpy(token[count++], tok);
        tok = strtok(NULL, ",");
    }
    return count;
}

int getInt(int Lower, int Upper){
    int input;
    char ch;

    while(scanf("%d%c", &input, &ch) != 2 || isspace(ch) == 0 || input > Upper || input < Lower){
      rewind(stdin);
      printf("\033[0;31m    Input ERROR enter again(%d - %d): \033[0m", Lower, Upper);
    }
}

int get_menu(){
    int select;
    
    printf("\n************************************************************\n");
    printf("*                 Score Calculator Function                *\n");
    printf("************************************************************\n");
    printf("*  1. Read file                                            *\n");
    printf("*  2. Set grade                                            *\n");
    printf("*  3. Statics (Min, Max, Mean, SD)                         *\n");
    printf("*  4. Statics (Grade classes)                              *\n");
    printf("*  5. Average GPA                                          *\n");
    printf("*  6. Show all data                                        *\n");
    printf("*  7. Sort data form score (High to low)                   *\n");
    printf("*  8. Sort data form Student ID                            *\n");
    printf("*  9. Show data from score in rang                         *\n");
    printf("* 10. Show data from Grade                                 *\n");
    printf("* 11. Search by part of name                               *\n");
    printf("*             0. exist                                     *\n");
    printf("************************************************************\n");
    printf("   Enter menu number: ");

    select = getInt(0, 11);

    return select;
}

void set_grade(student_info table[], int student_amount){

    int count, gradeRange[8], A, Bp, B, Cp, C, Dp, D;
    char string[255], buff[255], token[20][20];

    printf("enter grading range in csv('','',''): ");
    gets(string);
    strcpy(buff, string);
    
    count = split(buff, token);
    for (int i = 0; i < count; i++){
        sscanf(token[i], "%d", &gradeRange[i]);
    }

    A = gradeRange[0];
    Bp = gradeRange[1];
    B = gradeRange[2];
    Cp = gradeRange[3];
    C = gradeRange[4];
    Dp = gradeRange[5];
    D = gradeRange[6];
    
    for (int i = 0; i < student_amount; i++){
        if(table[i].total >= A){
            table[i].grade = 4.0;
            strcpy(table[i].gradeLetter, "A");
        }else if(table[i].total >= Bp){
            table[i].grade = 3.5;
            strcpy(table[i].gradeLetter, "B+");
        }else if(table[i].total >= B){
            table[i].grade = 3.0;
            strcpy(table[i].gradeLetter, "B");
        }else if(table[i].total >= Cp){
            table[i].grade = 2.5;
            strcpy(table[i].gradeLetter, "C+");
        }else if(table[i].total >= C){
            table[i].grade = 2.0;
            strcpy(table[i].gradeLetter, "C");
        }else if(table[i].total >= Dp){
            table[i].grade = 1.5;
            strcpy(table[i].gradeLetter, "D+");
        }else if(table[i].total >= D){
            table[i].grade = 1.0;
            strcpy(table[i].gradeLetter, "D");
        }else{
            table[i].grade = 0;
            strcpy(table[i].gradeLetter, "F");
        }
    }
}

void stat_dump(student_info table[], int student_amount){
    char ch;
    double midMin, midMax, midMean, midSD, midSum = 0, midSumSqrt = 0;
    double finalMin, finalMax, finalMean, finalSD, finalSum = 0, finalSumSqrt = 0;
    double accumMin, accumMax, accumMean, accumSD, accumSum = 0, accumSumSqrt = 0;
    double totalMin, totalMax, totalMean, totalSD, totalSum = 0, totalSumSqrt = 0;

    midMin = midMax = table[0].mid;
    finalMin = finalMax = table[0].final;
    accumMin = accumMax = table[0].accum;
    totalMin = totalMax = table[0].total;

    do{
        for(int i = 0; i < student_amount; i++){
            if(table[i].mid < midMin){
                midMin = table[i].mid;
            }
            if(table[i].mid > midMax){
                midMax = table[i].mid;
            }

            if(table[i].final < finalMin){
                finalMin = table[i].final;
            }
            if(table[i].final > midMax){
                finalMax = table[i].final;
            }

            if(table[i].accum < midMin){
                accumMin = table[i].accum;
            }
            if(table[i].accum > midMax){
                accumMax = table[i].accum;
            }
            if(table[i].total < midMin){
                totalMin = table[i].total;
            }
            if(table[i].total > midMax){
                totalMax = table[i].total;
            }
            midSum   = midSum + table[i].mid;
            finalSum = finalSum + table[i].final;
            accumSum = accumSum + table[i].accum;
            totalSum = totalSum + table[i].total;

            midSumSqrt   = midSumSqrt + pow(table[i].mid, 2);
            finalSumSqrt = finalSumSqrt + pow(table[i].final, 2);
            accumSumSqrt = accumSumSqrt + pow(table[i].accum, 2);
            totalSumSqrt = totalSumSqrt + pow(table[i].total, 2);
        }

        midMean   = midSum/student_amount;
        finalMean = finalSum/student_amount;
        accumMean = accumSum/student_amount;
        totalMean = totalSum/student_amount;

        midSD   = sqrt(midSumSqrt/student_amount - pow(midMean, 2));
        finalSD = sqrt(finalSumSqrt/student_amount - pow(finalMean, 2));
        accumSD = sqrt(accumSumSqrt/student_amount - pow(accumMean, 2));
        totalSD = sqrt(totalSumSqrt/student_amount - pow(totalMean, 2));

        printf("\n************************************************************\n");
        printf("*                    Statics (Grade info)                  *\n");
        printf("************************************************************\n");
        printf("* Score *   Midterm  *   Final    * Accumulate*   Total    *\n", midMin, finalMin, accumMin, totalMin);
        printf("************************************************************\n");
        printf("* min   *   %6.2lf   *   %6.2lf   *  %6.2lf   *   %6.2lf   *\n", midMin, finalMin, accumMin, totalMin);
        printf("* max   *   %6.2lf   *   %6.2lf   *  %6.2lf   *   %6.2lf   *\n", midMax, finalMax, accumMax, totalMax);
        printf("* mean  *   %6.2lf   *   %6.2lf   *  %6.2lf   *   %6.2lf   *\n", midMean, finalMean, accumMean, totalMean);
        printf("* SD    *   %6.2lf   *   %6.2lf   *  %6.2lf   *   %6.2lf   *\n", midSD, finalSD, accumSD, totalSD);
        printf("************************************************************\n");
        printf("\nPress any key to continue: ");

        ch = getch();
    }while(ch == 'c');

}

void stat_grade(student_info table[], int student_amount){
    int A = 0, Bp = 0, B = 0, Cp = 0, C = 0, Dp = 0, D = 0, F = 0;
    char ch;

    do{
        for(int i = 0; i < student_amount; i++){
            if(strcmp(table[i].gradeLetter, "A") == 0){
                A++;
            }else if(strcmp(table[i].gradeLetter, "B+") == 0){
                Bp++;
            }else if(strcmp(table[i].gradeLetter, "B") == 0){
                B++;
            }else if(strcmp(table[i].gradeLetter, "C+") == 0){
                Cp++;
            }else if(strcmp(table[i].gradeLetter, "C") == 0){
                C++;
            }else if(strcmp(table[i].gradeLetter, "D+") == 0){
                Dp++;
            }else if(strcmp(table[i].gradeLetter, "D") == 0){
                D++;
            }else{
                F++;
            }
        }

        printf("\n************************************************************\n");
        printf("*                    Statics (Grade info)                  *\n");
        printf("************************************************************\n");
        printf("*         *      *     *     *     *     *     *     *     *\n");
        printf("*         *   A  *  B+ *  B  * C+  *  C  *  D+ *  D  *  F  *\n");
        printf("*         *      *     *     *     *     *     *     *     *\n");
        printf("************************************************************\n");
        printf("*         *      *     *     *     *     *     *     *     *\n");
        printf("*  count  *  %3d * %3d * %3d * %3d * %3d * %3d * %3d * %3d *\n", A, Bp, B, Cp, C, Dp, D, F);
        printf("*         *      *     *     *     *     *     *     *     *\n");
        printf("************************************************************\n");
        printf("\nPress any key to continue: ");

        ch = getch();
    } while (ch == 'c');
}

void GPAprint(student_info table[], int student_amount){
    double GPA = 0.00, sum = 0.00;
    char ch;
    do{
        for(int i = 0; i < student_amount; i++){
            sum += table[i].grade;
        }
        GPA = sum/student_amount;

        printf("\n GPA Mean: %4.2lf \n", GPA);
        printf("\n Press any key to continue: ");
        ch = getch();
    } while (ch == 'c');
}

void printStudent(student_info s, int i){
    printf(" %2d). %ld %-30s %7.1lf %7.1lf %7.1lf %7.1lf %7.1lf  %s\n", i, s.id, s.name, s.mid, s.final, s.accum, s.total, s.grade, s.gradeLetter);
}

void printStudentWOGrade(student_info s, int i){
    printf(" %2d). %ld %-30s %7.1lf %7.1lf %7.1lf %7.1lf\n", i, s.id, s.name, s.mid, s.final, s.accum, s.total);
}

void printAllStudent( student_info s[] , int student_amount){
    char ch;
    do{
        for (int i = 0; i < student_amount; i++){
            printStudent(s[i], i+1);
        }
        printf("\nPress any key to continue: ");
        ch = getch();
    }while(ch == 'c');
}

void printAllStudentWOGrade( student_info s[] , int student_amount){
    char ch;
    do{
        for (int i = 0; i < student_amount; i++){
            printStudentWOGrade(s[i], i+1);
        }
        printf("\nPress any key to continue: ");
        ch = getch();
    }while(ch == 'c');
}

void sortByScore(student_info table[], int student_amount){
    student_info temp;
    for (int i = 0; i < student_amount; i++){
        for(int j = 0; j < student_amount; j++){
            if(table[j].total > table[i].total){
                temp = table[i];
                table[i] = table[j];
                table[j] = temp;
            }
        }
    }
}

void sortById(student_info table[], int student_amount){
    student_info temp;
    for (int i = 0; i < student_amount; i++){
        for(int j = 0; j < student_amount; j++){
            if(table[j].id > table[i].id){
                temp = table[i];
                table[i] = table[j];
                table[j] = temp;
            }
        }
    }
}

void searchScore(student_info table[], int student_amount){
    double min, max;
    int count = 0;
    char ch;
    
    do{
        printf("\n Enter min score: ");
        min = getInt(0, 100);
        printf("\n Enter mac score: ");
        max = getInt(0, 100);

        for(int i = 0; i < student_amount; i++){
            if(table[i].total >= min && table[i].total <= max){
                printStudent(table[i], count+1);
                count++;
            }
        }
        printf("%d Total people in range (%.2lf - %.2lf)\n", count, min, max);
        printf("Enter y to search again: ");
        ch = getch();
    } while (ch == 'y');
}

void searchGrade(student_info table[], int student_amount){
    char Grade[3];
    int count = 0;
    char ch;
    
    do{
        printf("\n Search grade (A, B+, B, C+, D+, D, F): ");
        gets(Grade);

        for(int i = 0; i < student_amount; i++){
            if(strcmp(table[i].gradeLetter, Grade) == 0){
                printStudent(table[i], count+1);
                count++;
            }
        }
        printf("%d Total people grade %2s \n", count, Grade);
        printf("Enter y to search again: ");
        ch = getch();
    } while (ch == 'y');
}

void searchName(student_info table[], int student_amount){
    char Name[50];
    char ch;
    
    do{
        int count = 0;
        printf("\n Search name: ");
        gets(Name);

        for(int i = 0; i < student_amount; i++){
            if(strstr(table[i].name, Name) != NULL){
                printStudent(table[i], count+1);
                count++;
            }
        }
        printf("%d Total people name %s\n", count, Name);
        printf("Enter y to search again: ");
        ch = getch();
    } while (ch == 'y');
}

void main(){
    char ch;
    student_info student, table[100];
    int student_amount, select, read_status = 0, set_grade_status = 0;
    do{
        select = get_menu();

        if(select == 1){
            student_amount = read_file("SCORE.CSV", table);
            printf("\n total read: %d \n", student_amount);
            printAllStudentWOGrade(table, student_amount);
            read_status = 1;
        }else if (select == 2){
            if(read_status == 1){
                set_grade(table, student_amount);
                printAllStudent(table, student_amount);
                set_grade_status = 1;
            }else{
                continue;
            }
        }else if (select == 3 && read_status == 1 && set_grade_status == 1){
            stat_dump(table, student_amount);
        }else if (select == 4 && read_status == 1 && set_grade_status == 1){
            stat_grade(table, student_amount);
        }else if (select == 5 && read_status == 1 && set_grade_status == 1){
            GPAprint(table, student_amount);
        }else if (select == 6 && read_status == 1 && set_grade_status == 1){
            printAllStudent(table, student_amount);
        }else if (select == 7 && read_status == 1 && set_grade_status ==1){
            sortByScore(table, student_amount);
            printAllStudent(table, student_amount);
        }else if (select == 8 && read_status == 1 && set_grade_status ==1){
            sortById(table, student_amount);
            printAllStudent(table, student_amount);
        }else if (select == 9 && read_status == 1 && set_grade_status ==1){
            searchScore(table, student_amount);
        }else if (select == 10 && read_status == 1 && set_grade_status ==1){
            searchGrade(table, student_amount);
        }else if (select == 11 && read_status == 1 && set_grade_status ==1){
            searchName(table, student_amount);
        }
            
        
    }while(select != 0);
}