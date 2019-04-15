import sys
from random import random

n = 15
a = [0]+n
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

print(sys.getsizeof(n))
print(sys.getsizeof(arr))
print(sys.getsizeof(mn))
print(sys.getsizeof(mx))
print(sys.getsizeof(imn))
print(sys.getsizeof(imx))

#Python 3.7.2
#ОС 64-разрядная