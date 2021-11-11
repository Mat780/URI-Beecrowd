#include <stdio.h>
#include <stdlib.h>

typedef struct cel {
    int chave;
    struct cel *ant;
    struct cel *prox;
} celula;


void insere_dup_C (int y, celula *lst) {

    celula *p, *q, *nova;
    nova = (celula *) malloc(sizeof (celula));

    nova->chave = y;
    p = lst;
    q = lst->prox;

    while (q != NULL) {
        p = q;
        q = q->prox;
    }

    nova->ant = p;
    nova->prox = q;
    p->prox = nova;

    if (q != NULL)
        q->ant = nova;
}


void imprime_lista (celula *lst) {

    celula *p;

    for (p = lst; p != NULL; p = p->prox) {
        printf("%d\n", p->chave);
    }

}

void org_list(celula *lst) {
	celula *p, *q;

	p = lst;
	q = lst->prox;
	
    while (q != NULL) {
        p = q;
        q = q->prox;
    }

	while(p != NULL){


		q = p;
		p = p->ant;
		
	}

}

void remover(celula *p){

    celula *temp;

    while(p != NULL){
        temp = p;
        p = p->prox;
        free(temp);
    }

}


int main (void) {

    celula *lista;
    lista = (celula *) malloc(sizeof (celula));
    
    lista->ant = NULL;
    lista->prox = NULL;
		
	while (scanf("%c", &c) != EOF) {

		// ENQUANTO TIVER RECEBENDO VAI COLOCANDO NO REGISTRO
		// SENÃO ORGANIZA, IMPRIME E REINICIA A CELULA
		if (c != '\n') {
			insere_dup_C(c, lista);
		} 

        else {
			org_list(lista);
			imprime_lista(lista);
			remover(lista);

			celula *lista;
			lista = (celula *) malloc(sizeof (celula));
			
			lista->ant = NULL;
			lista->prox = NULL;
		}

	}

	org_list(lista);
	imprime_lista(lista);
    

	return 0;

}