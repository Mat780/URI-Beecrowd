#include <stdio.h>

void troca(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

void BubbleSort(int n, int *v, int *cont){
    int i, j;
    for (i = n - 1; i > 0; i--)
        for (j = 0; j < i; j++)
            if (v[j] > v[j+1]){
				troca(&v[j], &v[j+1]);
				*cont += 1;
			}
                
}


int main(void){

	int vezes, tamanho;

	scanf(" %d", &vezes);

	while(vezes > 0) {

		scanf(" %d", &tamanho);

		int v[tamanho], cont = 0;

		for(int c = 0; c < tamanho; c++) {
			scanf(" %d", &v[c]);
		}

		BubbleSort(tamanho, v, &cont);

		printf("Optimal train swapping takes %d swaps.\n", cont);

		vezes--;

	}

}