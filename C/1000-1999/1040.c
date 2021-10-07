#include <stdio.h>

int main(void){
    float n1, n2, n3, n4, med;

    scanf("%f %f %f %f", &n1, &n2, &n3, &n4);
    med = (n1*2 + n2*3 + n3*4 + n4)/10;
    printf("Media: %.1f\n", med);

    if (med >= 7){
        printf("Aluno aprovado.\n");
    } else if (med >= 5){
        printf("Aluno em exame.\n");
        scanf("%f", &n1);
        printf("Nota do exame: %.1f\n", n1);
        med = (med+n1)/2;
        if (med >= 5){
            printf("Aluno aprovado.\n");

        } else{
            printf("Aluno reprovado.\n");
        }
        printf("Media final: %.1f\n", med);
    } else{
        printf("Aluno reprovado.\n");
    }

    return 0;
}
