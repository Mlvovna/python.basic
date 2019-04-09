company = {}
n = int(input("Количество компаний: "))
m = 4
s = 0
p = 0
for i in range(n):
	cname = input(str(i+1) + "-я компания: ")
	print("Введите прибыль за каждый квартал")
	for j in range(m):
		kv[j] = int(input())
		s += kv[j]
		company[cname] = s
		p += s
		

avrg = p / n
for i in company:
	if company[i] > avrg:
		Print("Прибыль выше среднего у компании: ", company[i])
	elif company[i] < avrg:
		Print("Прибыль ниже среднего у компании: ", company[i])