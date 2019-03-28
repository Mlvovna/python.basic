from random import random
n = 15
m = [0] * n
for i in range(n):
	m.append(int(random() * 100) - 50)
print()

i = 0
j = -1
while i < n:
	if m[i] < 0 and j == -1:
		j = i
	elif m[i] < 0 and m[i] > m[j]:
		j = i
	i += 1
	
print(j+1,':',m[j])