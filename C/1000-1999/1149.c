#include <stdio.h>

int main (void){
    int x = 0, y = 0, temp = 0;

    scanf("%d", &x);

    while (y<=0){
        scanf("%d", &y);
    }

    if (x < y){

    } else{
        for (int c = 0; y > c; c++){
        temp += x + c;
        }
    }

    printf("%d\n", temp);

    return 0;
}
