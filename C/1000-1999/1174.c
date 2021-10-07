#include <stdio.h>

int main(void) {
    float num;
    for (int c = 0; c <= 99; c++){
        scanf("%f", &num);
        if (num <= 10)
            printf("A[%d] = %.1f\n", c,num);
    }
    return 0;
}
