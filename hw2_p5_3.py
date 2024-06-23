num = int(input("The number of the requested element in Fibonacci (n)=")) #輸入計算到第幾個費波那契數
s1 = str(input("The first string for Palindromic detection (s1)=")) #輸入第一個字串
s2 = str(input("The second string for Palindromic detection (s2)=")) #輸入第二個字串
text = str(input("The plaintext to be encrypted:")) #輸入密文
code = [] #設定空陣列
ptext = [] #設定空陣列
plaintext = "" #設定空字串

k0 = 0 #第零項
k1 = 1 #第一項
k2 = 0 #第二項開始為零 
i = 2 #從第二項開始套公式
while i <= num: #根據餘數判斷哪兩項相加
	if(i % 3 == 2):
		k2 = k0 + k1
	elif (i % 3 == 0):
		k0 = k2 + k1
	elif (i % 3 == 1):
		k1 = k2 + k0
	i += 1

ans1 = "" #設定空字串
ansLen1 = 0 #設定初始字串長度為0
ans2 = "" #設定空字串
ansLen2 = 0 #設定初始字串長度為0
for j in range(len(s1)):	
	l,r = j, j #奇數字串從中間向兩邊搜索
	while l >= 0 and r < len(s1) and s1[l] == s1[r]: #字串相符
		if (r - l + 1) > ansLen1: #字串長度大於當前最長長度
			ans1 = s1[l:r + 1] #丟入設定字串
			ansLen1 = r - l + 1 #更改字串最長長度
		l -= 1 #向左1
		r += 1 #向右1
	l,r = j, j + 1 #偶數字串從中間向兩邊搜索
	while l >= 0 and r < len(s1) and s1[l] == s1[r]: #字串相符
		if (r - l + 1) > ansLen1: #字串長度大於當前最長長度
			ans1 = s1[l:r + 1] #丟入設定字串
			ansLen1 = r - l + 1 #更改字串最長長度
		l -= 1 #向左1
		r += 1 #向右1 #
for j in range(len(s2)):	
	l,r = j, j #奇數字串從中間向兩邊搜索
	while l >= 0 and r < len(s2) and s2[l] == s2[r]: #字串相符
		if (r - l + 1) > ansLen2: #字串長度大於當前最長長度
			ans2 = s2[l:r + 1] #丟入設定字串
			ansLen2 = r - l + 1 #更改字串最長長度
		l -= 1 #向左1
		r += 1 #向右1
	l,r = j, j + 1 #偶數字串從中間向兩邊搜索
	while l >= 0 and r < len(s2) and s2[l] == s2[r]: #字串相符
		if (r - l + 1) > ansLen2: #字串長度大於當前最長長度
			ans2 = s2[l:r + 1] #丟入設定字串
			ansLen2 = r - l + 1 #更改字串最長長度
		l -= 1 #向左1
		r += 1 #向右1
for k in range(len(text)):
	code.append(ord(text[k]))
	if (num % 3 == 0): 
		code[k] += k0
	elif (num % 3 == 1): 
		code[k] += k1
	elif(num % 3 == 2): 
		code[k] += k2
	code[k] = code[k] * ansLen1 + ansLen2
	if code[k] >= 90:
		code[k] = ((code[k] - 65) % 26) + 65
	plaintext += chr(code[k])

print("----- extract key for encrypt method -----")
print("The " + str(num) + "-th Fibonacci sequence number is:", end = "")
if (num % 3 == 0): #若餘數為0,則會停在k0
	print(k0)
elif (num % 3 == 1): #若餘數為1,則會停在k1
	print(k1)
elif(num % 3 == 2): #若餘數為2,則會停在k2
	print(k2)
print("Longest palindrome substring within first string is:", ans1)
print("Length is:", ansLen1)
print("Longest palindrome substring within second string is:", ans2)
print("Length is:", ansLen2)
print("----- encryption completed -----")
print("The encrypted text is:", plaintext)