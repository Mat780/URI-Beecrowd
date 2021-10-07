#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 1001


struct Estrutura{
    int ascii;
    int cont;
};

int comparaPalavra(const void * a, const void * b){
    return ( *(char*)a - *(char*)b );
}

int comparaEstrutura(const void * a, const void * b){
    // Defino como temporario para fazer a comparação abaixo
    struct Estrutura *tempA = (struct Estrutura *)a;
    struct Estrutura *tempB = (struct Estrutura *)b;

    if (tempA->cont != tempB->cont)
        return tempA->cont - tempB->cont;
    
    return tempB->ascii - tempA->ascii;
}


int main(void){
    int cont, len, contstr = 0; 
    char palavra[MAX];
    char asciiChar;

    // Primeiro colocamos While para ir até EOF
    while(scanf("%s", &palavra) != EOF){

        // Quando o código retornar ele vai imprimir uma linha vazia para separar as organizações
        if(contstr != 0)
            printf("\n");
        
        // Pega o tamanho da serie de letras/numeros
        len = strlen(palavra);
        // Faz um vetor de estruturas com o tamanho da leitura
        struct Estrutura v[len];

        // Reset de variaveis de contagem
        cont = 0;
        contstr = 0;

        // Um qsort para ordenar o vetor de char
        qsort(palavra, len, sizeof(char), comparaPalavra);

        // Uma variavel para armazenar o valor ascii
        asciiChar = palavra[0];
        // Primeira ocorrencia da variavel acima
        cont++;

        for (int c = 1; c < len; c++){
            // Se o comando ascii anterior for o mesmo do seguinte
            // Significa que a sequencia continua
            if(asciiChar == palavra[c]){
                cont++;
            
            // Senão, significa que a sequencia acabou
            } else {
                // Aqui armazena o valor tanto do ascii quanto da frequencia dele
                // Dentro do vetor de estruturas
                v[contstr].ascii = asciiChar;
                v[contstr].cont = cont;

                // Nova variavel ascii
                asciiChar = palavra[c];
                // Primeira Ocorrencia
                cont = 1;
                // Vai para a proxima estrutura dentro do vetor de estruturas
                contstr++;
            }

        }

        // Ultima sequencia
        v[contstr].ascii = asciiChar;
        v[contstr].cont = cont;

        // Adicionar o final para dizer o tamanho do vetor
        contstr++;

        // qsort para ordernar as estruturas pela frequencia
        qsort(v, contstr, sizeof(struct Estrutura), comparaEstrutura);

        // Imprimi os registros ordenados até eles acabarem
        for(int c = 0; c < contstr; c++){
            printf("%d %d\n", v[c].ascii, v[c].cont);
        }
    }
    return 0;
}