#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

void add_space(char *String){
    char output[strlen(String)*3];
    int j=0;
    for (int i = 0; i < strlen(String); i++){
        if(strchr("()+-*/^", String[i]) != NULL){
            output[j++] = *" ";
            output[j++] = String[i];
            output[j++] = *" ";
        }else{
            output[j++] = tolower(String[i]);
        }
    }
    output[j] = *"\0";
    strcpy(String, output);
}

int isNumber(char *String){
    char ch;
    double n;
    if(sscanf(String, " %lf%c", &n, &ch) == 1){
        return 1;
    }else{
        return 0;
    }
}


int varlid_check(char letter){
    if(strchr("0123456789_abcdefghijklmnopqrstuvwxyz", letter) != NULL){
        return 1;
    }
    return 0;
}

int find_func(char *temp){
    char func[10][5] = {"sin", "cos", "tan", "asin", "acos", "atan", "sqrt", "log", "exp", "pow"};
    for (int i = 0; i < 10; i++){
        if(!strcmp(temp, func[i])){
            return 1;
        }
    }
    return 0;
}



void main(){

    char temp[50];
    char array[50][50];
    char *token, ans[20];
   
    do{
        char buff[50];
        int j = 0;
        int k = 0;
        int quan = 0;
        int op = 0;
        int func = 0;
        int iden = 0;
        int err = 0;
        
        printf("enter token: ");
        gets(buff);
        add_space(buff);

        printf("%s\n\n", buff);
        //  split string to array
        //  get the first token
        token = strtok(buff, " ");
    
        // walk through other tokens
        while( token != NULL ) {
            strcpy(array[k++], token);
            quan++;

            token = strtok(NULL, " ");
        }


        // analyse information
        for(int i = 0; i < quan; i++){

            if(find_func(array[i])){
                func++;
            }else if(strchr("()+-*/^", *array[i]) != NULL){
                op++;
            }
            else if(isNumber(array[i]) == 0 && strchr("+-*/^", *array[i]) == NULL){
                iden++;
                for(int j = 0; j < strlen(*array); j++){
                    if(isdigit(array[i][0]) != 0  || !varlid_check(array[i][j]) ){
                        iden--;
                        err++;
                        break;
                    }
                }
            }
        }
        
        printf("    Count of String = %d\n", quan);
        printf("    Count of Number = %d\n", quan-op-func-iden-err);
        printf("    Count of Operation = %d\n", op);
        printf("    Count of Function = %d\n", func);
        printf("    Count of Identifier = %d\n", iden);
        printf("    Cout of Syntax error = %d\n", err);

        printf("\nEnter end/exist to end program: ");
        gets(ans);
    }while(strcmp(ans, "end") != 0 &&  strcmp(ans, "exist") != 0);
}

