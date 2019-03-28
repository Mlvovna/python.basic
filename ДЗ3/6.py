from random import random
n = 10
m = [0] * n
for i in range(n):
	m[i] = int(random() * 50)
print()

min_id = 0
max_id = 0
for i in range(1,n):
	if m[i] < m[min_id]:
		min_id = i
	elif m[i] > m[max_id]:
		max_id = i
print(m[min_id], m[max_id])

if min_id > max_id:
	min_id, max_id = max_id, min_id
	
s = 0
for i in range(min_id+1, max_id):
	s += m[i]
print(s)