#include <stdio.h>

int fib(int *cont,int n){
    if (n==0){
        *cont = *cont + 1;
        return 0;
    }
    else if (n==1){
        *cont = *cont + 1;
        return 1;
    }
    else{
        *cont = *cont + 1;
        return fib(*&cont, n-1) + fib(*&cont, n-2);
    }
}

int main(void){
    int n, vez, res, cont;

    scanf("%d", &vez);

    while (vez > 0){
        cont = 0;

        scanf(" %d", &n);
        res = fib(&cont, n);

        printf("fib(%d) = %d calls = %d\n", n, cont-1, res);

        vez--;
    }

}
