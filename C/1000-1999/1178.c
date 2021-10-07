#include <stdio.h>

int main(void) {
    double val;

    scanf("%lf", &val);

    for (int c = 0; c < 100; c++){
        printf("N[%d] = %.4lf\n", c, val);
        val /= 2;
    }

    return 0;
}
