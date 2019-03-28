from random import random
n = 10
m = 10
x = []
for i in range(m):
	y = []
	for j in range(n):
		m = int(random() * 200)
		y.append(m)
		print('%4d' % m,end='')
	x.append(y)
	print()
	
mx = -1
for j in range(n):
	mn = 200
	for i in range(m):
		if a[i][j] < mn:
			mn = x[i][j]
	if mn > mx:
		mx = mn
print(mx)