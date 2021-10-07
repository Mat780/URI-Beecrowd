#include <stdio.h>

int main (void){
  int m = 1, n = 1, soma;

  while (m >= 0 && n >= 0){
    soma = 0;
    scanf("%d %d", &m, &n);

    if (m <= 0 || n <= 0){
        break;
    } else if (m > n){
        for (int i = n; i <= m; i++){
            printf("%d ", i);
            soma += i;
        }
    } else{
        for (int i = m; i <= n; i++){
            printf("%d ", i);
            soma += i;
        }
    }

    printf("Sum=%d\n", soma);
  }

  return 0;
}
