import timeit
from random import random

def concat_test():
	n = 15
	arr = [0]+n
	for i in range(n)
		arr[i] = int(random()*100)
		print(arr[i],end='')
	print()
	
	mn = min(arr)
	mx = max(arr)
	imn = arr.index(mn)
	imx = arr.index(mx)
	print('arr[%d}=%d arr[%d}=%d' % (imn+1, mn, imx+1, mx)
	arr[imn],arr[imx] = arr[imx],arr[imn]
	
	for i in range(15)
		print(arr[i],end='')
	print()
	
def append_test():
	n = 15
	arr = [0]+n
	for i in range(n)
		arr[i] = int(random()*100)
		print(arr[i],end='')
	print()
	
	mn = 0
	mx = 0
	for i in range(n):
		if arr[i] < arr[mn]:
			mn = i
		elif arr[i] > arr[mx]:
			mx = i
	print('arr[%d}=%d arr[%d}=%d' % (mn+1, arr[mn], mx+1, arr[mx])
	b = arr[mn]
	arr[mn] = arr[mx]
	arr[mx] = b
	
	for i in range(15)
		print(arr[i],end='')
	print()
	
print(timeit.timeit("concat_test()",  setup="from __main__ import concat_teat", number = 100000))
print(timeit.timeit("append_test()",  setup="from __main__ import append_teat", number = 100000))