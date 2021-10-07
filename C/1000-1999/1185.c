#include <stdio.h>
#define LMAX 12
#define CMAX 12

int main(void) {
    float num, vetor[LMAX][CMAX], soma = 0;
    int cont = 11, cont2 = 0;
    char op;

    scanf(" %c", &op);

    for(int i = 0; i < LMAX; i++){
        for(int j = 0; j < CMAX; j++){
            scanf(" %f", &num);
            vetor[i][j] = num;
            if(j < cont){
                soma += num;
                cont2++;
            }
        }
        cont--;
    }

    if(op == 'M'){
        soma /= cont2;
    }

    printf("%.1f\n", soma);

    return 0;
}
