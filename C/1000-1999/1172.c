#include <stdio.h>

int main(void) {
    int vet[10], num;
    for (int c = 0; c <= 9; c++){
        scanf("%d", &num);
        if (num > 0)
            vet[c] = num;
        else
            vet[c] = 1;
        printf("X[%d] = %d\n", c, vet[c]);
    }

    return 0;
}
