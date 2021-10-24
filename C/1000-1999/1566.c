#include <stdio.h>

int main(void){

	int z, m, n;
	int v[231] = {0};

	scanf(" %d", &z);

	while(z > 0){

		scanf(" %d", &m);

		for(int i = 0; i < m; i++){
			scanf(" %d", &n);
			v[n]++;
		}
		int q = 1;
		for(int i = 20; i < 231; i++){
			for(int j = 0; j < v[i]; j++){
				if(q){
					printf("%d", i);
					q = 0;
				}else{
					printf(" %d", i);
				}
			}
			v[i] = 0;
		}
		printf("\n");
		z--;
	}

}