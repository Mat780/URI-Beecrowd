#include <stdio.h>

int main (void){
  int cod, uni, cod2, uni2;
  float valor, valor2, res;

  scanf("%d %d %f", &cod, &uni, &valor);
  scanf("%d %d %f", &cod2, &uni2, &valor2);

  res = uni*valor + uni2*valor2;

  printf("VALOR A PAGAR: R$ %.2f\n", res);


  return 0;
}
