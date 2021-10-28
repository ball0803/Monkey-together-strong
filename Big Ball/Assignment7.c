#include <stdio.h>
#include <math.h>
#include <string.h>
#include <ctype.h>

int getint(int min,int max){ 
    int num=0;
    char ch;
    rewind(stdin);
    while (scanf("%d%c",&num,&ch)==0||(ch!='\n'&&ch!=' ')||num<min||num>max)
    {
        rewind(stdin);
        printf("Invaid input please enter number again.(%d - %d)",min,max);
    }
    return num;
}
int get_menu(){ 
    int sel;
    printf(" \n************************************************\n");
    printf(" *          Assignment 7 Test Array             *\n");
    printf(" ************************************************\n");
    printf(" * 1.Add data                                   *\n");
    printf(" * 2.Show data                                  *\n");
    printf(" * 3.Sort data                                  *\n");
    printf(" * 4.Delete data                                *\n");
    printf(" * 5.Calculate statistic                        *\n");
    printf(" * 0.Exit                                       *\n");
    printf(" ************************************************\n");
    printf(" Select menu number : ");
    sel = getint(0,5);

    return sel;
}

void add_data(double array[], int size){
    int index = 0;
    int result;
    char ch;
    double number;

    printf("enter number: ");

    for (int i = 0; i < size; i++){
        if(array[i]==-1){
            break;
        }
        index++;
    }

    while(scanf("%lf%c", &number, &ch) != 0 && (isspace(ch) != 0) && number >= 0){
        array[index] = number;
        index++;
        if (ch == '\n'){
            break;
        }
    }
}

void show_data(double array[]){
    int index = 0;
    printf("[");
    while(array[index] != -1){
        printf("%.2g ", array[index]);
        index++;
    };
    printf("]\n");
}

void delete_data(double array[], int size){
    char ch;
    int j = 0;
    double num;
    double temp_array[size];
    for (int i = 0; i < size; i++){
        temp_array[i] = -1;
    }
    printf("Enter number you want to delete: ");
    scanf("%lf", &num);
    for (int i = 0; i < size; i++){
        if(array[i]==-1){
            break;
        }
        if (array[i] == num){
            printf("Are you sure you wanna delete? [y/n] ");
            while(scanf(" %c", &ch) == 0 || (ch != 'y' && ch != 'n')){
                printf("Invalid input enter again: ");
            }
            if(ch == 'y'){
                continue;
            }
        }
        temp_array[j] = array[i];
        j++;
    }

    for (int i = 0; i < size; i++){
        if(array[i]==-1){
            break;
        }
        array[i] = temp_array[i];
    }
}

void sort_data(double element_list[], int low, int high)
{
    int pivot, value1, value2, temp;
    if (low < high){
        pivot = low;
        value1 = low;
        value2 = high;

        while (value1 < value2){
            while (element_list[value1] <= element_list[pivot] && value1 <= high){
                value1++;
            }

            while (element_list[value2] > element_list[pivot] && value2 >= low){
                value2--;
            }

            if (value1 < value2){
                temp = element_list[value1];
                element_list[value1] = element_list[value2];
                element_list[value2] = temp;
            }
        }

        temp = element_list[value2];
        element_list[value2] = element_list[pivot];
        element_list[pivot] = temp;
        sort_data(element_list, low, value2 - 1);
        sort_data(element_list, value2 + 1, high);
    }
}

int sizeOfArray(double array[], int size){
    int count = 0;
    for (int i = 0; i < size; i++){
        if(array[i]==-1){
            break;
        }
        count++;
    }
    return count;
}

void stat_data(double array[], int size){
    double min = array[0];
    double max = array[0];
    double sum = 0;
    double sumS= 0;
    double SD;

    for( int i = 0; i < sizeOfArray(array, size); i++){
        sum += array[i];
        if(array[i] < min){
            min = array[i];
        }
        if(array[i] > max){
            max = array[i];
        }
    }

    for( int i = 0; i < sizeOfArray(array, size); i++){
        sumS += (array[i] - sum/sizeOfArray(array, size))*(array[i] - sum/sizeOfArray(array, size));
    }
    SD = sqrt(sumS/sizeOfArray(array, size));

    printf("min = %g max = %g mean = %g SD = %g\n", min, max, sum/sizeOfArray(array, size), SD);
}

void main(){
    double list[100], min, max, sum, SD;
    int Select;
    for (int i = 0; i < 100; i++){
        list[i] = -1;
    }


    do{
        Select = get_menu();
        switch(Select){
            case 1:
                add_data(list, 100);
                show_data(list);
                break;
            case 2:
                if(sizeOfArray(list, 100) == 0){
                    printf("there are no data yet\n");
                }else{
                    show_data(list);
                }
                break;
            case 3:
                if(sizeOfArray(list, 100) == 0){
                    printf("there are no data yet\n");
                }else{
                    sort_data(list, 0, sizeOfArray(list, 100) -1 );
                    show_data(list);
                }
                break;
            case 4:
                if(sizeOfArray(list, 100) == 0){
                    printf("there are no data yet\n");
                }else{
                    delete_data(list, 100);
                    show_data(list);
                }
                break;
            case 5:
                if(sizeOfArray(list, 100) < 2){
                    printf("there are no enough data yet\n");
                }else{
                    show_data(list);
                    stat_data(list, 100);
                }
                break;
        }
    }while(Select != 0);
}