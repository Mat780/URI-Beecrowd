#include <stdio.h>

int main (void){
  int km;
  float lt, res;

  scanf("%d", &km);
  scanf("%f", &lt);

  res = km/lt;

  printf("%.3f km/l\n", res);

  return 0;
}
