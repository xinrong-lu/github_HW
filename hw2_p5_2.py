s = str(input("Enter a string:")) #輸入字串
ans = "" #設定空字串
ansLen = 0 #設定初始字串長度為0
for i in range(len(s)):	
	l,r = i, i #奇數字串從中間向兩邊搜索
	while l >= 0 and r < len(s) and s[l] == s[r]: #字串相符
		if (r - l + 1) > ansLen: #字串長度大於當前最長長度
			ans = s[l:r + 1] #丟入設定字串
			ansLen = r - l + 1 #更改字串最長長度
		l -= 1 #向左1
		r += 1 #向右1
	l,r = i, i + 1 #偶數字串從中間向兩邊搜索
	while l >= 0 and r < len(s) and s[l] == s[r]: #字串相符
		if (r - l + 1) > ansLen: #字串長度大於當前最長長度
			ans = s[l:r + 1] #丟入設定字串
			ansLen = r - l + 1 #更改字串最長長度
		l -= 1 #向左1
		r += 1 #向右1
print("Longest palindrome substring is:", ans)
print("Length is:", ansLen)
