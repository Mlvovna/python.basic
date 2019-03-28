n = 5
m = 4
x = []
for i in range(m):
	y = []
	s = 0
	print("%d-я строка = " % i)
	for j in range(n-1):
		m = int(input())
		s += m
		y.append(m)
	y.append(s)
	x.append(y)
	
for i in x:
	print(i)
	