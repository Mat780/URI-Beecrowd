#include <stdio.h>

int main (void){
  float a, b, c, res;

  scanf("%f", &a);
  scanf("%f", &b);
  scanf("%f", &c);

  res = (a*2+b*3+c*5)/10;

  printf("MEDIA = %.1f\n", res);

  return 0;
}
