#include <stdio.h>

int main (void){
    int res, soma = 0;
    scanf("%d", &res);
    while (res != 0){
        soma = 0;
        for (int c = res; c < res+10; c++){
            if (c%2 == 0)
                soma += c;
        }
        printf("%d\n", soma);
        scanf("%d", &res);
    }

    return 0;
}
