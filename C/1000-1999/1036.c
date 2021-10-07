#include <stdio.h>
#include <math.h>

int main (void){
  double a, b, c, r1, r2, sq;

  scanf("%lf %lf %lf", &a, &b, &c);

  sq = b*b - 4*a*c;

  if (sq <= 0 || a == 0){
    printf("Impossivel calcular\n");
  } else {
    r1 = (b*-1 + sqrt(sq))/(2*a);
    r2 = (b*-1 - sqrt(sq))/(2*a);

    printf("R1 = %.5lf\n", r1);
    printf("R2 = %.5lf\n", r2);
  }

  return 0;
}
