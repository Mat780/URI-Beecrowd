n = int(input())
aux = list(map(int, input().split()))
menor = aux[0]
index = 1

for i in range(n):
	if(menor > aux[i]):
		menor = aux[i]
		index = i + 1

print(index)