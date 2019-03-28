from random import random
n = 10
m = [0] * n
even = []
for i in range(n)
	m[i] = int(random() * 10 ) + 10
	if m[i] % 2 == 0:
		even.append(i)
print(m)
print('Индексы четных элементов массива: ',even)