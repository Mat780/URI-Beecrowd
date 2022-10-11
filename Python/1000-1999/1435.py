n = int(input())

while n != 0:

	yCIMA = 1
	yBAIXO = n

	for i in range(0, n):
		xESQ = 1
		xDIR = n
		for j in range(0, n):
			if(xDIR <= xESQ and xDIR <= yCIMA and xDIR <= yBAIXO): # xDIR menor q todos
				if(xDIR != 1):
					print("%3d" % (xDIR), end=" ")
				else:
					if(yBAIXO != 1):
						print("%3d" % (xDIR))
					else:
						print("%3d\n" % (xDIR))

			elif (xESQ <= yCIMA and xESQ <= yBAIXO): # xESQ menor q todos
				print("%3d" % (xESQ), end=" ")
				
			elif (yCIMA <= yBAIXO): # yCIMA menor q todos
				print("%3d" % (yCIMA), end=" ")

			else: # yBAIXO menor q todos
				print("%3d" % (yBAIXO), end=" ")
			
			xESQ += 1
			xDIR -= 1
			
		yCIMA += 1
		yBAIXO -= 1
			
	n = int(input())