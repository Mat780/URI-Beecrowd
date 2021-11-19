#include <stdio.h>
#include <stdlib.h>

typedef struct celula{
    int chave;
    struct celula *prox;
} celula;

void empilha(int y, celula *t){
    celula *nova;
    nova = (celula *) malloc(sizeof (celula));
    nova->chave = y;
    nova->prox = t->prox;
    t->prox = nova;
}

int excluir(celula *t){
    int inteiro;
    celula *p;
    // Cabeça 1 2 
    if (t->prox != NULL) {
        p = t->prox; // 1
        t->prox = p->prox; // Cabeça -> 2
        inteiro = p->chave;
        free(p); // Tchau 1
    }

    return inteiro;

}

void joga_pra_tras(celula *c, celula **f){

    celula *aux;
    
    aux = c->prox;

    // Cabeça aponta...
    c->prox = c->prox->prox;

    aux->prox = (*f)->prox;

    (*f)->prox = aux;

    *f = aux;
}

void discarte(int n, celula *t) {

    int bo = 1, exc;
    celula *f, *c;
    c = t;

    // Para pegar a ultima posição
    empilha(n, c);
    f = c->prox;

    // Para formar o resto da lista
    for (int cont = n-1; cont > 0; cont--){
        empilha(cont, c);
    }

    printf("Discarded cards:");

    while(bo){
        exc = excluir(c);

        if(c->prox->prox != NULL){
            printf(" %d,", exc);
            joga_pra_tras(c, &f);
        } else {
            printf(" %d\n", exc);
            bo = 0;
        }
        
    }
    return;

}

int main () {

    int n;
    celula *t;
    t = (celula *) malloc(sizeof (celula));
    t->prox = NULL;

    scanf(" %d", &n);
    while(n != 0){

        discarte(n, t);
        printf("Remaining card: %d\n", t->prox->chave);
        n = excluir(t);
        scanf(" %d", &n);
    }

}