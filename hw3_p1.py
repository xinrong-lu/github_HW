num = int(input("Input the total number of students (n>0):")) #輸入
i = 1
count = 0
ID = []
while i <= num: #編號加到陣列裡
	ID += [i]
	i += 1
j = 0
while len(ID) > 1:
	count += 1
	if count == 3: #數到3的就刪掉
		ID[j] = 0
		count = 0
	j += 1
	if j == len(ID):
		j = 0
		for k in range(ID.count(0)):
			ID.remove(0)
print("The last ID is :", ID[0]) #輸出