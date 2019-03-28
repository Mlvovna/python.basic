from random import random
n = 15
m = [0] * n
for i in range(n):
	m[i] = int(random()*100)
print()

x = m[0]
y = 1
for i in range(n-1):
	z = 1
	for k in range(i+1,n):
		if m[i] == m[k]:
			z += 1
	if z > y:
		y = z
		x = m[i]
		
if y > 1:
	print('число ', x, 'встречается в массиве ', x, ' раз')
else:
	print('В массиве нет повторяющихся элементов')