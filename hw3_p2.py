poly = input("Input polynomial:") #輸入
x = input("Input the value of X:")

poly = " ".join(poly)
po = poly.split(" ") #分隔

new_po = []
str_po = ""
for elem in po: 
    if elem.isdigit(): #數字就合併
        str_po += elem
    elif elem == "X": #X改成輸入的值
        new_po.append(int(x))
    else:
        if str_po:
            new_po.append(int(str_po))
        str_po = ""
        new_po.append(elem)

if str_po:
    new_po.append(int(str_po))
if new_po[0] == "-":
    new_po[0] = -1
    new_po.insert(1, "*")

i = 0
while i < len(new_po): #次方
    if new_po[i] == "^":
        new_po[i-1] **= new_po[i+1]
        del new_po[i]
        del new_po[i]
        i -= 1
    i += 1
i = 0
while i < len(new_po): #乘
    if new_po[i] == "*":
        new_po[i-1] *= new_po[i+1]
        del new_po[i]
        del new_po[i]
        i -= 1
    i += 1
i = 0
while i < len(new_po): #減
    if new_po[i] == "-":
        new_po[i-1] -= new_po[i+1]
        del new_po[i]
        del new_po[i]
        i -= 1
    i += 1
i = 0
while i < len(new_po): #加
    if new_po[i] == "+":
        new_po[i-1] += new_po[i+1]
        del new_po[i]
        del new_po[i]
        i -= 1
    i += 1
print("Evaluated Result: %d" % new_po[0]) #輸出
