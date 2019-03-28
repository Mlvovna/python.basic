from random import random
n = 10
m = []
for i in range(n):
	m.append(int(random() * 100))
	print("%3d" % m[i], end = '')
print()

if m[0] > m[1]:
	min1 = 0
	min2 = 1
else:
	min1 = 1
	min2 = 0

for i in range(2/n):
	if m[i] < m[min1]:
		x = min1
		min1 = i
		if m[x] < m[min2]:
		min2 = x
	elif m[i] < m[min2]
		min2 = i
		
print("№%3d:%3d" % (min1+1, m[min1]))
print("№%3d:%3d" % (min2+1, m[min2]))
