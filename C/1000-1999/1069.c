#include <stdio.h>
#define MAX 1001

void empilha_seq(int *t, char *P, char y) {
    if (*t != 1000) {
        (*t)++;
        P[*t] = y;
    } 

}

int formado(char *palavra) {

    int t, res = 0; 
    char P[MAX];
    t = -1;

    for (int cont = 0; palavra[cont] != '\0'; cont++) {
        if ( palavra[cont] == '<' ) {
            empilha_seq(&t, P, palavra[cont]);

        } else if (t != -1) {
            if (palavra[cont] == '>') {
                t--;
                res++;
            }

        }
    }

    return res;

}

int main () {

    int vez, res;
    char frase[MAX];

    scanf("%d", &vez);

    while(vez){

        scanf(" %s", frase);

        res = formado(frase);

        printf("%d\n", res);

        vez--;
    }

}