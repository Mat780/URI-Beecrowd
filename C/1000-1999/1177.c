#include <stdio.h>

int main(void) {
    int corte, df;

    scanf("%d", &corte);
    df = corte;

    for (int c = 0; c < 1000; c++){
        if (corte == df){
            corte = 0;
        }
        printf("N[%d] = %d\n", c, corte);
        corte++;
    }

    return 0;
}
