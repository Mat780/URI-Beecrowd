#include <stdio.h>

void achar(int *v, int caso, int n){
    for (int c = 0; c < n; c++){
        if (v[c] == caso){
            printf("%d found at %d\n", caso, c+1);
            return;
        }
    }
    printf("%d not found\n", caso);
}

void insercao(int *v, int n){
    int c, i, temp;

    for (c = 1; c < n; c++) {
        temp = v[c];

        for (i = c - 1; i >= 0 && v[i] > temp; i--)
            v[i+1] = v[i];

        v[i+1] = temp;
    }
}



int main(void){
    int n, cons, marm, caso, cont = 1, temp;

    scanf("%d %d", &n, &cons);
    while (n > 0 && cons > 0){
        int v[n];

        printf("CASE# %d:\n", cont);

        for (int c = 0; c < n; c++){
            scanf(" %d", &temp);
            if (temp > 0 && temp < 10000)
                v[c] = temp;
            else
                c--;
        }

        insercao(v, n);

        for (int c = 0; c < cons; c++){
            scanf(" %d", &caso);
            achar(v, caso, n);
        }
        scanf("%d %d", &n, &cons);
        cont++;
    }
}
