#include <stdio.h>

int main (void){
    int corte, numMax, cont = 1;

    scanf("%d %d", &corte, &numMax);

    while (cont <= numMax){
        if (cont%corte == 0)
            printf("%d\n", cont);
        else
            printf("%d ", cont);
        cont++;
    }

    return 0;
}
