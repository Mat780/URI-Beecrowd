from math import sqrt

v = list(map(int, input().split()))

while v[0] != 0:

	res = sqrt((v[0] * v[1] / v[2]) * 100)

	print("%d" % (res))

	v = list(map(int, input().split()))