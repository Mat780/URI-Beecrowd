#include <stdio.h>

int main (void){
  int n1, n2, soma = 0, maior, menor;

  scanf("%d", &n1);
  scanf("%d", &n2);

  if (n1 > n2){
    maior = n1;
    menor = n2;
  } else{
    maior = n2;
    menor = n1;
  }

  for (int i = menor; i <= maior; i++){
    if (i % 13 != 0){
        soma += i;
    }
  }

  printf("%d\n", soma);
  return 0;
}
