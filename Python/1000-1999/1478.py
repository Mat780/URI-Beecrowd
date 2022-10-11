n = int(input())

while n != 0:
	aux = 1

	for i in range(0, n):
		for j in range(0, n):
			if(aux <= j):
				if(j != n - 1):
					print("%3d" % (j - i + 1), end=" ")
				else:
					print("%3d" % (j - i + 1))
			
			else:
				if(j != n - 1):
					print("%3d" % (aux - j), end=" ")
				else:
					print("%3d" % (aux - j))
		aux += 1		

	print()

	n = int(input())	