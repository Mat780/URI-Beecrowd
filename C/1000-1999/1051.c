#include <stdio.h>

int main(void){
    double num, res;
    scanf("%lf", &num);

    if (num >= 4500){
        res = 1000*0.08;
        res += 1500*0.18;
        res += (num-4500)*0.28;
        printf("R$ %.2lf\n", res);
    } else if (num >= 3000.01){
        res = 1000*0.08;
        res += (num - 3000)*0.18;
        printf("R$ %.2lf\n", res);
    } else if (num >= 2000.01){
        res = (num-2000)*0.08;
        printf("R$ %.2lf\n", res);
    } else{
        printf("Isento\n");
    }

    return 0;
}
