#include <stdio.h>

int main(void) {
    int num, vez;
    double fib1, fib2, nvfib;
    scanf("%d", &num);
    for (int c = 0; c < num; c++){
        scanf("%d", &vez);
        fib1 = 0;
        fib2 = 1;
        nvfib = 1;
        for (int i = 0; i < vez; i++){
            fib1 = fib2;
            fib2 = nvfib;
            nvfib = fib1 + fib2;
        }
        printf("Fib(%d) = %.0lf\n", vez, fib1);

    }
    return 0;
}
