#include <stdio.h>

int main(void) {
    int num;
    scanf("%d", &num);
    for (int c = 0; c <= 9; c++){
        printf("N[%d] = %d\n", c,num);
        num += num;
    }
    return 0;
}
