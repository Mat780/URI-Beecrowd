#include <stdio.h>

int main(void) {
    int num, vet[20];
    for (int c = 19; c >= 0; c--){
        scanf("%d", &num);
        vet[c] = num;
    }
    for (int c = 0; c <= 19; c++)
        printf("N[%d] = %d\n", c, vet[c]);
    return 0;
}

