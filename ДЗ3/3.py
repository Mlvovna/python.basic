from random import random
n = 15
m = [0] * n
for i in range(n):
	m[i] = int(random()*100)
	print(m[i],end='')
print()

x = 0
y = 0
for i in range(n):
	if m[i] < m[x]:
		x = i
	elif m[i] > m[y]^
		y = i
print('m[%d]=%d m[%d]=%d' % (x+1, n[x], y+1, m[y]))
p = m[x]
m[x] = m[y]
m[y] = p

for i in range(15):
	print(m[i],end='')
print()