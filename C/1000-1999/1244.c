#include <stdio.h>
#include <string.h>
#define MAX 10000

void sort(int n, char con_wrd[MAX][MAX], int cont[MAX]){
    int i, aux;
    char temp[MAX];
    for (i = 0; i < n - 1; i++){

        for (int j = 0; j < n - i - 1; j++){

            if (cont[j] < cont[j+1]){

                strcpy(temp, con_wrd[j]);
                strcpy(con_wrd[j], con_wrd[j+1]);
                strcpy(con_wrd[j+1], temp);

                aux = cont[j];
                cont[j] = cont[j+1];
                cont[j+1] = aux;
            }
        }
    }
}

int main(void){
    int vez, j, k;

    scanf("%d", &vez);

    while(vez > 0){
        char wrd[MAX], con_wrd[MAX][MAX] = { '\0' };
        int cont[MAX] = {0}, strL;
        j = k = 0;

        scanf(" %[^\n]", wrd);

        strL = strlen(wrd);

        for(int c = 0; c < strL; c++){
            if(wrd[c] != ' '){
                con_wrd[j][k] = wrd[c];
                k++;
                cont[j]++;
            } else {
                con_wrd[j][k] = '\0';

                j++;
                k = 0;
            }
        }

        sort(strL, con_wrd, cont);

        j = 0;
        while(cont[j+1] != 0){
            printf("%s ", con_wrd[j]);
            j++;
        }
        printf("%s\n", con_wrd[j]);

        vez--;
    }

}