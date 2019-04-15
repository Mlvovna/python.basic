import random

n = 1000
A = [random.randint(-100, 99) for _ in range(n)]

def b_sort(A):
	for i in range(1, len(A)):
		sort = False
		for j in range(len(A) - i):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
				sort = True
		if not sort:
			break
			
print(b_sort(A))