n = int(input())
v = map(int, input().split())
result = 0

for c in v:
	if(c == n):
		result += 1

print(result)