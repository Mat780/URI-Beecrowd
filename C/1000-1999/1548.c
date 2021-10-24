#include <stdio.h>

typedef struct{
	int num;
	int posOrigin;
} aluno;

void Intercala(int p, int q, int r, aluno *v){
    int i, j, k;

	aluno w[r];

    i = p; j = q; k = 0;
	
    while (i < q && j < r){
        if (v[i].num >= v[j].num) {
            w[k] = v[i]; i++; 
        } else {
            w[k] = v[j]; j++;
        }
        k++;
    }
    while (i < q){
        w[k] = v[i];
		i++;
		k++;
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


void MergeSort(int p, int r, aluno *v)
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
	int vezes, tamanho, num;

	scanf(" %d", &vezes);

	while(vezes > 0){
		int soma = 0;
		scanf(" %d", &tamanho);

		aluno arrayAlunos[tamanho];

		for(int c = 0; c < tamanho; c++){
			scanf(" %d", &num);

			arrayAlunos[c].num = num;
			arrayAlunos[c].posOrigin = c;
		};

		MergeSort(0, tamanho, arrayAlunos);

		for(int c = 0; c < tamanho; c++){
			if(arrayAlunos[c].posOrigin == c){
				soma++;
			}
		}

		printf("%d\n", soma);
	
		vezes--;
	}
}

