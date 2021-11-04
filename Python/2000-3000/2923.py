def main():

	continua = True

	while continua:
		try:
			t, a, w, c = map(int, input().split())

			por = (a/t) * 100

			if( por >= c ):
				print("critical")
			
			elif( por >= w ):
				print("warning")
			
			else:
				print("OK")
		except:
			continua = False

main()