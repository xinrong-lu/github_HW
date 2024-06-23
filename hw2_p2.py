num = int(input("Input the range number:")) #輸入數值
j = 1
perfect = [] #設定空陣列
while (j <= num):
	divisors = [] #設定因數空陣列
	for i in range(1, j + 1):
		if (j % i) == 0: #找因數
			divisors.append(i) 
	if (j == sum(divisors) / 2) #計算是否為因數相加:
		perfect.append(j)
	j += 1
print(perfect)