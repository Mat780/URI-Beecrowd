#include <stdio.h>
#define MAX 301

void empilha(int *t, char P[MAX], char c){
    (*t)++;
    P[*t] = c;

}

int main(void){

    char caracter, P[MAX];
    int t = -1, cont = 0;

    while(scanf("%c", &caracter) != EOF){

        if(caracter == '\n'){
            printf("%d\n", cont);
            cont = 0;
            t = -1;

        } else if (caracter == 'B'){
            
            if(P[t] == 'S'){
                t--;
                cont++;
            } else {
                empilha(&t, P, caracter);
            }

        } else if (caracter == 'S'){

            if(P[t] == 'B'){
                t--;
                cont++;
            } else {
                empilha(&t, P, caracter);
            }

        } else if (caracter == 'C'){

            if(P[t] == 'F'){
                t--;
                cont++;
            } else {
                empilha(&t, P, caracter);
            }
        } else if (caracter == 'F'){

            if(P[t] == 'C'){
                t--;
                cont++;
            } else {
                empilha(&t, P, caracter);
            }
        }

    }

}