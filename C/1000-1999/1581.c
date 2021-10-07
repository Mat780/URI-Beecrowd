#include <stdio.h>

void copiarVetor(char vet1[], char vet2[]){
    int cont = 0;

    while (vet1[cont] != '\0'){
        vet2[cont] = vet1[cont];
        cont++;
    }
}

int comparar(char vet1[], char vet2[], int bol){
    int cont = 0;

    if (bol == 1){
        while (vet1[cont] != '\0'){
        if (vet1[cont] != vet2 [cont]){
            bol = 0;
        }
        cont++;
    }
    }

    return bol;
}

int main (void){
    char vet1[21], vet2[21];
    int Convez, vez, bol = 1;

    scanf("%d", &Convez);

    while (Convez > 0){
        bol = 1;
        scanf("%d", &vez);
        scanf(" %s", vet1);
        copiarVetor(vet1, vet2);
        while (vez > 1){
            scanf(" %s", &vet2);
            bol = comparar(vet1, vet2, bol);
            copiarVetor(vet1, vet2);
            vez--;
        }

        if (bol == 1){
            printf("%s\n", vet1);
        }else
            printf("ingles\n");

        Convez--;
    }

    return 0;
}
