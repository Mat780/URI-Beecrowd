#include <stdio.h>
#define MAX 1001

void empilha_seq(int *t, char *P, char y) {
    if (*t != 1000) {
        (*t)++;
        P[*t] = y;
    } 

}

void ta_correto(char *palavra) {

    int t; 
    char P[MAX];
    t = -1;

    for (int cont = 0; palavra[cont] != '\0'; cont++) {
        if ( palavra[cont] == '(' ) {
            empilha_seq(&t, P, palavra[cont]);

        } else if (palavra[cont] == ')') {
            if (t != -1) {
                t--;

            } else {
                printf("incorrect\n");
                return;

            }
        }
    }

    if(t == -1){
        printf("correct\n");
        
    } else {
        printf("incorrect\n");

    }
    
    return;

}

int main () {

    char frase[MAX];

    while( scanf(" %s", frase) != EOF){

        ta_correto(frase);

    }

}