#include <stdio.h>
#define LMAX 12
#define CMAX 12

int main(void) {
    float num, vetor[LMAX][CMAX];
    int col;
    char op;

    scanf("%d", &col);
    scanf(" %c", &op);

    for(int i = 0; i < LMAX; i++){
        for(int j = 0; j < CMAX; j++){
            scanf(" %f", &num);
            vetor[i][j] = num;
        }
    }
    num = 0;
    for(int i = 0; i < LMAX; i++){
        num += vetor[i][col];
    }

    if(op == 'M'){
        num /= 12;
    }

    printf("%.1f\n", num);

    return 0;
}
