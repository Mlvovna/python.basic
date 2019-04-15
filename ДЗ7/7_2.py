import random
def m_sort(A):
	if len(A) <= 1:
		return A
		
	left = m_sort(A[:len(A) // 2])
	right = m_sort(A[len(A) // 2:])
	i, j = 0, 0
	
	while len(left) > i and len(right) > j:
		if left[i] < right[j]:
			A[i+j] = left[i]
			i += 1
		else:
			A[i+j] = right[j]
			j += 1
	
	while len(left) > i:
		A[i+j] = left[i]
		i += 1
	while len(right) > j:
		A[i+j] = right[j]
		j += 1
		
	return A
	
print(m_sort(A))