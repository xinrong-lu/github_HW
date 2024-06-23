num = int(input("Enter the number of layers(2 to 5) =")) #輸入層數
length = int(input("Enter the side of the top layer =")) #輸入頂層邊數
grow = int(input("Enter the growth of each layer =")) #輸入每層增加邊數
width = int(input("Enter the trunk width(odd number, 3 to 9) =")) #輸入樹幹寬度
height = int(input("Enter the trunk height(4 to 10) =")) #輸入樹幹高度
center = int(length + grow * (num - 1)) #找中心點
j = 1
while j <= num:
	if j == 1:
		i = 1
	else:
		i =2 
	while i <= length:
		print(" " * (center - i), end = "") #印出空格
		if i == 1:
			print("#") #第一層印一個#
		elif (i >= 2) and (i < length):
			print("#", end = "") #每層最左邊的#
			print("@" * (2 * (i - 1) - 1), end = "") #每層中間的@
			print("#") #每層最右邊的#
		elif i == length:
			print("#" * (2 * i - 1)) #每個layer的底部	
		i += 1 #下一層
	j += 1
	length += grow #每次邊數多grow
k = 1
while k <= height: #印樹幹
	print(" " * int(center - (width + 1) / 2), end = "")
	print("|" * width)
	k += 1 #下一層