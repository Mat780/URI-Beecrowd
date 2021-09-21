#include <stdio.h>
#define MAX 100

void intercala(int p, int q, int r, int v[MAX])
{
    int i, j, k, w[MAX];
    i = p; j = q; k = 0;
    while (i < q && j < r) {
        if (v[i] <= v[j]) {
            w[k] = v[i]; i++; }
        else {
            w[k] = v[j]; j++; }
        k++;
    }
    while (i < q) {
        w[k] = v[i]; i++; k++; }
    while (j < r) {
        w[k] = v[j]; j++; k++; }
    for (i = p; i < r; i++)
        v[i] = w[i-p];
}

void mergesort(int p, int r, int v[MAX])
{
    int q;
    if (p < r - 1) {
        q = (p + r) / 2;
        mergesort(p, q, v);
        mergesort(q, r, v);
        intercala(p, q, r, v);
    }
}

int main(void){
    int vez, num, par = 0, impar = 0;
    int vP[MAX], vIP[MAX];
    scanf("%d", &vez);

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

    mergesort();
    mergesort(vIP, impar);

    for(int c = 0; c < par; c++){
        printf("%d\n", vP[c]);
    }

    for(int c = impar-1; c > -1; c--){
        printf("%d\n", vIP[c]);
    }

}
