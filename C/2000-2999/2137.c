#include <stdio.h>

void selectSort(int *v, int n){
	int temp, min;

	for(int c = 0; c < n; c++){
		min = c;
		for(int i = c+1; i < n; i++)
			if(v[i] < v[min])
                min = i;
		temp = v[c];
		v[c] = v[min];
		v[min] = temp;
	}
}

int main(void){
    int vezF;

    while (scanf("%d", &vezF) != EOF){
        int v[vezF];
        for (int c = 0; c < vezF; c++){
            scanf("%d", &v[c]);
        }
        selectSort(v, vezF);

        for (int c = 0; c < vezF; c++){
            printf("%04d\n", v[c]);
        }
    }
    return 0;
}
