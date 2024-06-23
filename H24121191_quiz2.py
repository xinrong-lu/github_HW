input_shopping_amount = float(input("Enter the shopping amount: "))
input_membership_level = input("Enter the membership level: ")
#購物金額以及會員等級

if input_membership_level == "Regular":
	if 1000 < input_shopping_amount <=2000:
		amount = input_shopping_amount * (0.9)
	if 2000 <input_shopping_amount <= 3000:
		amount = input_shopping_amount * (0.85)
	if input_shopping_amount > 3000:
		amount = input_shopping_amount * (0.8)
#若等級為Regular,則根據以下金額範圍有不同的折扣

if input_membership_level == "Gold":
	if 1000 < input_shopping_amount <= 2000:
		amount = input_shopping_amount * (0.85)
	if 2000 < input_shopping_amount <= 3000:
		amount = input_shopping_amount * (0.8)
	if input_shopping_amount > 3000:
		amount = input_shopping_amount * (0.75)
#若等級為Gold,則根據以下金額範圍有不同的折扣

print("input_membership_level", "$",amount)
#印出會員等級及最終應付金額
