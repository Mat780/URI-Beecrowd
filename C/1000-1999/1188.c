#include <stdio.h>
#define LMAX 12
#define CMAX 12

int main(void) {
    double num, soma = 0;
    float vetor[LMAX][CMAX];
    int contE = 0, contD = 11, cont2 = 0;
    char op;

    scanf(" %c", &op);

    for(int i = 0; i < LMAX; i++){
        for(int j = 0; j < CMAX; j++){
            scanf(" %lf", &num);
            vetor[i][j] = num;
            if(j < contE && j > contD){
                soma += num;
                cont2++;
            }
        }
        contE++;
        contD--;
    }

    if(op == 'M'){
        soma /= cont2;
    }

    printf("%.1lf\n", soma);

    return 0;
}
