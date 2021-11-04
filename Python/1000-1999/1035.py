def main():
	
	continua = True

	while continua:
		try:
			aux = float(input())

			aux = str(aux)
			aux = aux.split(".")

			num = int(aux[0])
			vir = float('0.' + aux[1])
			
			aux = float(input())

			if aux < vir:
				num += 1
			
			print("%.0f" %(num) )
		
		except EOFError:
			continua = False
		
		except:
			continua = False
main()