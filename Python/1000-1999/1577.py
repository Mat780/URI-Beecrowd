from math import pow

def func(n):
	v = [[1 for c in range(n)] for c in range(n)]

	for c in range(1, n): # Faz a primeira linha
		v[0][c] = v[0][c-1] * 2

	for i in range(1, n): 
		v[i][0] = v[i - 1][0] * 2
		for j in range(1, n):
			v[i][j] = v[i][j-1] * 2
	
	return v

n = int(input())

while n != 0:
	v = func(n)
	if(n == 1 or n == 2):
		for i in range(n):
			for j in range(n - 1):
				print("%1d" % (v[i][j]) , end=" ")
			print("%1d" % (v[i][n-1]) )

	elif(n == 3 or n == 4):
		for i in range(n):
			for j in range(n - 1):
				print("%2d" % (v[i][j]) , end=" ")
			print("%2d" % (v[i][n-1]) )

	elif(n == 5):
		for i in range(n):
			for j in range(n - 1):
				print("%3d" % (v[i][j]) , end=" ")
			print("%3d" % (v[i][n-1]) )

	elif(n == 6 or n == 7):
		for i in range(n):
			for j in range(n - 1):
				print("%4d" % (v[i][j]) , end=" ")
			print("%4d" % (v[i][n-1]) )
	
	elif(n == 8 or n == 9):
		for i in range(n):
			for j in range(n - 1):
				print("%5d" % (v[i][j]) , end=" ")
			print("%5d" % (v[i][n-1]) )

	elif(n == 10):
		for i in range(n):
			for j in range(n - 1):
				print("%6d" % (v[i][j]) , end=" ")
			print("%6d" % (v[i][n-1]) )
	
	elif(n == 11 or n == 12):
		for i in range(n):
			for j in range(n - 1):
				print("%7d" % (v[i][j]) , end=" ")	
			print("%7d" % (v[i][n-1]) )

	elif(n == 13 or n == 14):
		for i in range(n):
			for j in range(n - 1):
				print("%8d" % (v[i][j]) , end=" ")	
			print("%8d" % (v[i][n-1]) )

	elif(n == 15):
		for i in range(n):
			for j in range(n - 1):
				print("%9d" % (v[i][j]) , end=" ")	
			print("%9d" % (v[i][n-1]) )
	print()
	n = int(input())



# 1 e 2
# 3 e 4
# 5
# 6 e 7
# 8 e 9
# 10
# 11 e 12
# 13 e 14
# 15