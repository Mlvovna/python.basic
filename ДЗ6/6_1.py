from pympler import asizeof
import sys

a = [0]*8
for i in range(2,100):
	for j in range(2,10):
		if i%j == 0:
			a[j-2] += 1
i = 0
while i < len(a):
	print(a[i])
	i += 1

print(sys.getsizeof(a))