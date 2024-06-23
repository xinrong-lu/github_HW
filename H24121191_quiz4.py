lst = input("Enter a sequence of numbers separated by whitespace:").split() #輸入數值並將其改做串列
compare = []
for i in range(len(lst)):
	inc_lst = []
	inc_lst.append(lst[i])
	now = 0
	for j in range(i, len(lst)): #找從哪個數字開始前項比後項小
		if lst[j] > inc_lst[now]:
			inc_lst.append(lst[j])
			now += 1
	if len(compare) < len(inc_lst):
		compare = list(inc_lst)
print(len(lst))
print("LICS: [", end="") #將其印出至前項比後項大
for i in range(len(compare)):
	if i < len(compare) - 1:
		print(compare[i], end=" ")
	elif i == len(compare) - 1:
		print(compare[i], end="]")

