#include <stdio.h>


int main (void){
    int di, di2;
    float num;

    scanf("%f %d %d", &num, &di, &di2);

    di += di2;
    num /= di;

    printf("%.2f\n", num);

  return 0;
}
