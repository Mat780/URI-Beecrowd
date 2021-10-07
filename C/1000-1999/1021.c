#include <stdio.h>

int main(void){
    double din, ftemp = 0;
    int temp = 0;

    scanf("%lf", &din);
    printf("NOTAS:\n");

    if (din >= 100){
        temp = din/100;
        din -= temp*100;
    }

    printf("%i nota(s) de R$ 100.00\n", temp);
    temp = 0;

    if (din >= 50){
        temp = din/50;
        din -= temp*50;
    }

    printf("%i nota(s) de R$ 50.00\n", temp);
    temp = 0;

    if (din >= 20){
        temp = din/20;
        din -= temp*20;
    }

    printf("%i nota(s) de R$ 20.00\n", temp);
    temp = 0;

    if (din >= 10){
        temp = din/10;
        din -= temp*10;
    }

    printf("%i nota(s) de R$ 10.00\n", temp);
    temp = 0;

    if (din >= 5){
        temp = din/5;
        din -= temp*5;
    }

    printf("%i nota(s) de R$ 5.00\n", temp);
    temp = 0;

    if (din >= 2){
        temp = din/2;
        din -= temp*2;
    }

    printf("%i nota(s) de R$ 2.00\n", temp);
    temp = 0;

    printf("MOEDAS:\n");

    if (din >= 1){
        temp = din;
        din -= temp;
    }

    printf("%i moeda(s) de R$ 1.00\n", temp);
    temp = 0;
    din *= 100;

    if (din >= 50){
        temp = din/50;
        din -= temp*50;
    }

    printf("%i moeda(s) de R$ 0.50\n", temp);
    temp = 0;

    if (din >= 25){
        temp = din/25;
        din -= temp*25;
    }

    printf("%i moeda(s) de R$ 0.25\n", temp);
    temp = 0;

    if (din >= 10){
        temp = din/10;
        din -= temp*10;
    }

    printf("%i moeda(s) de R$ 0.10\n", temp);
    temp = 0;

    if (din >= 5){
        temp = din/5;
        din -= temp*5;
    }

    printf("%i moeda(s) de R$ 0.05\n", temp);
    temp = din;

    printf("%i moeda(s) de R$ 0.01\n", temp);

    return 0;
}
