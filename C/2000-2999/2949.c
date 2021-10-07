#include <stdio.h>
#define max 100

int main (void){
  int vez, hob = 0, hum = 0, elf = 0, ana = 0, mag = 0;
  char lt, nome[max];

  scanf("%d", &vez);

  for (int i = 0; i < vez; i++){
    scanf("%s %c", &nome, &lt);

    switch(lt){
        case 'X':
            hob += 1;
            break;
        case 'M':
            mag += 1;
            break;
        case 'H':
            hum += 1;
            break;
        case 'A':
            ana += 1;
            break;
        case 'E':
            elf += 1;
            break;
    }

  }
  printf("%d Hobbit(s)\n", hob);
  printf("%d Humano(s)\n", hum);
  printf("%d Elfo(s)\n", elf);
  printf("%d Anao(s)\n", ana);
  printf("%d Mago(s)\n", mag);

  return 0;
}
