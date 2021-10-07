#include <stdio.h>
# define max 100

int buscarVetor(char vetChar[], int vetInt[], char letra, int vezRun){
  char let = vetChar[0];
  int cont = -1;
  int c;
  for (c = 0; vezRun > c && let != letra ; c++){
    let = vetChar[c];
    cont++;
  }
  if (c == 0){
    return vetInt[c];
  } else if (c == vezRun-1){
    return vetInt[vezRun-1];
  } else
    return vetInt[cont];
}

int main(void){
  int vez, vezRun, pmin, pont[max], lmax, cont = 0, pontitos = 0;
  char let[max], runas[max];

  scanf("%i %i", &vez, &pmin);

  for (int c = 0; vez > c; c++){
    scanf(" %c %i", &let[c], &pont[c]);
  }
  scanf("%i", &vezRun);
  scanf(" %[^\n]", runas);
  lmax = (vez*2)-2;

  for (int c = 0; vezRun > c; c++){
    pontitos += buscarVetor(let, pont, runas[cont], vez);
    cont += 2;
  }
  printf("%i\n", pontitos);
  if (pmin <= pontitos){
    printf("You shall pass!\n");
  } else{
    printf("My precioooous\n");
  }
  return 0;
}
