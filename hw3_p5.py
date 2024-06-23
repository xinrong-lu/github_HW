seat_input = (input("Input the sequence of seats:").split()) #輸入
seat = list(map(int, seat_input))
i = 0
left, right = 0, len(seat) - 1
left_max, right_max = 0, 0
water = 0
while left < right: 從左右兩邊算
	if seat[left] <= seat[right]:
		if seat[left] >= left_max:
			left_max = seat[left]
		else:
			water += left_max - seat[left]
		left += 1
		print("Water: %d" % water)
	else:
		if seat[right] >= right_max:
			right_max = seat[right]
		else:
			water += right_max - seat[right]
		right -= 1
print("Water: %d" % water) #輸出