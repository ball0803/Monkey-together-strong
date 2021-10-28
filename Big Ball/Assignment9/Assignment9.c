#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int cmpfunc(const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

int read_binary_file(char *filebin, int array_data[], int *count){
    FILE* fp = fopen(filebin, "r");
    int temp;
    if (fp == NULL){
        printf("error can't open the file");
    }else{
        while(!feof(fp)){
            if(fread(&temp, sizeof(int), 1, fp)==1){
                array_data[*count] = temp;
                *count = *count + 1;
            }
        }
        fclose(fp);
    }
}

int read_text_file(char *filetext, int array_data[], int *count){
    FILE* fp = fopen(filetext, "r");
    int temp;
    if (fp == NULL){
        printf("error can't open the file");
        return 0;
    }else{
        while(fscanf(fp, "%d", &array_data[*count]) != EOF){
            *count = *count + 1;
        }
        fclose(fp);
    }
}

void compare_binsearch(int data1[],int count1, int data2[], int count2){
    int k =0;
    int *item;
    for (int i = 0; i < count1; i++ ){
        item = (int*) bsearch (&data1[i], data2, count2, sizeof(int), cmpfunc);
        if(item != NULL){
            k++;
            printf("    Found[%d] = %d\n", k, data1[i]);
        }
        else{
            printf("    Item = %d could not be found\n", data1[i]);
        }
    }
}

void compare_search(int data1[],int count1, int data2[], int count2){
    int k = 0;
    int find = 0;
    for(int i = 0; i < count1; i++){
        for(int j =0; j < count2; j++){
            if(data1[i] == data2[k]){
                k++;
                printf("    Found[%d] = %d\n", k, data1[i]);
                break;
                find = 1;
            }
        }
        if(find != 1){
            printf("    Item = %d could not be found\n", data1[i]);
        }
        find = 0;
    }
}
void main(){
    int data1[100000];
    int data2[100001];
    int count1 = 0;
    int count2 = 0;
    clock_t t;

    read_binary_file("bin100000.bin", data1, &count1);
    read_text_file("txt100000.txt", data2, &count2);
    qsort(data2, count2, sizeof(int), cmpfunc);

    printf("Method 1: for loop scan\n");
    t = clock();
    compare_search(data1, count1, data2, count2);
    t = clock() - t;
  
    printf("Took %g seconds to execute \n", ((double)t)/CLOCKS_PER_SEC);

    printf("Method 2: Quick sort and Binary search\n");
    t = clock();
    compare_binsearch(data1, count1, data2, count2);
    t = clock() - t;
  
    printf("Took %g seconds to execute \n", ((double)t)/CLOCKS_PER_SEC);

}
