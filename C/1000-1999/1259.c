#include <stdio.h>
#define MAX 1000

void troca(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}


int separa(int p, int r, int v[MAX]){
    int x, i, j;
    x = v[p];
    i = p - 1;
    j = r + 1;
    while (i < j) {
        do {
            j--;
        } while (v[j] > x);
        do {
            i++;
        } while (v[i] < x);
        if (i < j)
            troca(&v[i], &v[j]);
    }
    return j;
}

void quicksort(int p, int r, int v[MAX])
{
    int q;
    if (p < r) {
        q = separa(p, r, v);
        quicksort(p, q, v);
        quicksort(q+1, r, v);
    }
}


int main(void){
    int vez, num, par = 0, impar = 0;
    scanf("%d", &vez);

    int vP[vez], vIP[vez];

    for (int c = 0; c < vez; c++){
        scanf("%d", &num);

        if (num % 2 == 0){
            vP[par] = num;
            par++;
        }else{
            vIP[impar] = num;
            impar++;
        }
    }

    quicksort(0, par-1, vP);
    quicksort(0, impar-1, vIP);

    for(int c = 0; c < par; c++){
        printf("%d\n", vP[c]);
    }

    for(int c = impar-1; c > -1; c--){
        printf("%d\n", vIP[c]);
    }

}
