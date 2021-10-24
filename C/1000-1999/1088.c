#include <stdio.h>

typedef struct{
    int num;
    int changPos;
} numeros;

void Intercala(int p, int q, int r, numeros *v){
    int i, j, k;

    numeros w[r];

    i = p; j = q; k = 0;

    while (i < q && j < r){
        if (v[i].num <= v[j].num) {
            w[k] = v[i]; i++; 
        } else {
            // q = Ultima posicao  -  i = Iteravel      
            v[i].changPos += q-i;
            w[k] = v[j]; j++;
        }
        k++;
    }
    while (i < q){
        w[k] = v[i]; i++; k++;
    }
    while (j < r){
        w[k] = v[j];
        j++;
        k++;
    }
    for (i = p; i < r; i++){
        v[i] = w[i-p];
    }
}


void MergeSort(int p, int r, numeros *v)
{
    int q;
    if (p < r - 1) {
        q = (p + r) / 2;
        MergeSort(p, q, v);
        MergeSort(q, r, v);
        Intercala(p, q, r, v);
    }
}

int main(void){
    
    int vezes, cont = 0;

    scanf(" %d",&vezes);

    while(vezes > 0){

        numeros v[vezes];
        cont = 0;

        for(int i=0; i < vezes; i++){
            scanf(" %d", &v[i].num);
            v[i].changPos = 0;
        }

        MergeSort(0, vezes, v);

        for(int i=0; i < vezes; i++){

            cont += v[i].changPos;

        }
        if(cont % 2 == 0){
            printf("Carlos\n");
        }else{
            printf("Marcelo\n");
        }

        scanf(" %d",&vezes);
    }


}