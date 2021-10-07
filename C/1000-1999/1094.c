#include <stdio.h>

int main (void){
    float vez, qtd_animal, cob = 0, coelho = 0, rat = 0, sap = 0, percentual;
    char animal;

    scanf("%f", &vez);

    for (int c = 0; c < vez; c++){
        scanf(" %f %c", &qtd_animal, &animal);
        if (animal == 'C')
            coelho += qtd_animal;
        else if (animal == 'R')
            rat += qtd_animal;
        else if (animal == 'S')
            sap += qtd_animal;

        cob += qtd_animal;
    }

    printf("Total: %.0f cobaias\n", cob);
    printf("Total de coelhos: %.0f\n", coelho);
    printf("Total de ratos: %.0f\n", rat);
    printf("Total de sapos: %.0f\n", sap);

    percentual = (coelho/cob)*100;
    printf("Percentual de coelhos: %.2f %%\n", percentual);

    percentual = (rat/cob)*100;
    printf("Percentual de ratos: %.2f %%\n", percentual);

    percentual = (sap/cob)*100;
    printf("Percentual de sapos: %.2f %%\n", percentual);

    return 0;
}
