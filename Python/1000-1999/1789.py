while True:
	try:
		n = int(input())
		v = list(map(int, input().split()))
		maior = v[0]
		
		for i in range(1, n):
			if(maior < v[i]):
				maior = v[i]
		
		if(maior >= 20):
			print(3)
		
		elif(maior >= 10):
			print(2)
		
		else:
			print(1)
	
	except EOFError:
		break