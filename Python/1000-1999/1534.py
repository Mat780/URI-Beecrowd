while True:
	try:
		n = int(input())

		conI = 0
		conJ = n-1

		for i in range(n):
			for j in range(n):
				if(conI == i and conJ == j):
					print("2", end="")
				
				elif(i == j):
					print("1", end="")
				
				else:
					print("3", end="")
			
			print()
			conI += 1
			conJ -= 1


	except EOFError:
		break