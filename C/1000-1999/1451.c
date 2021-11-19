#include <stdio.h>
#include <stdlib.h>

typedef struct cel{
	char caractere;
	struct cel *prox;
}celula;

void insere(int y, celula **lst)
{
	celula *nova;
	nova = (celula *) malloc(sizeof (celula));
	nova->caractere = y;
	nova->prox = (*lst)->prox;
	(*lst)->prox = nova;
	*lst = nova;
}

void imprime_lista(celula *lst) {

    celula *p;

    for (p = lst; p->prox != NULL; p = p->prox) {
        printf("%c", p->caractere);
    }
	
    printf("%c\n", p->caractere);

}

void remover(celula *p){
    celula *temp;
    while(p != NULL){
        temp = p;
        p = p->prox;
        free(temp);
    }

}

int main(void){

	char c;
	celula *lista, *frente, *aux;
	lista = (celula *) malloc(sizeof (celula));

	lista->prox = NULL;

	frente = lista;
	aux = lista;
	
	while(scanf("%c", &c) != EOF){

		if(c == '\n'){

			if(lista->prox != NULL){
				imprime_lista(lista->prox);
				remover(lista);

				lista = (celula *) malloc(sizeof (celula));
				lista->prox = NULL;
				frente = lista;
				aux = lista;
			}
			
		} else if(c == '['){
			aux = lista;

		} else if(c == ']'){
			aux = frente;

		} else {
			insere(c, &aux);

			if(aux->prox == NULL){
				frente = aux;
			}

		}
	}

	return 0;

}