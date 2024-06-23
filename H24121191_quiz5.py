row = int(input("Enter the number of rows:"))
column = int(input("Enter the number of columns:"))
reserved_seat = input("Enter the reserved seats:").split("|")
reserved = [["", ""] for i in range(len(reserved_seat))]
outrange = []
for i in range(len(reserved_seat)):
	reserved[i][0], reserved[i][1] = map(int, reserved_seat[i].split(","))
	if reserved[i][0] > row or reserved[i][1] > column or reserved[i][0] < 1 or reserved[i][1] < 1:
		outrange.append(reserved[i])
		reserved[i] = []
for i in range(reserved.count([])):
	reserved.remove([])
if outrange:
	print("Out-of-range reserved seats: ", end="")
	for i in range(len(outrange)-1):
		print(outrange[i][0], end=",")
		print(outrange[i][1], end="|")
	print(outrange[len(outrange)-1][0], end= ",")
	print(outrange[len(outrange)-1][1])
arrange = [["A" for i in range(column)] for j in range(row)]
for i in range(len(reserved)):
	arrange[reserved[i][0]-1][reserved[i][1]-1] = "R"
print("Seating Arrangement:")
for i in range(len(arrange)):
	for j in range(len(arrange[i])):
		print(arrange[i][j], end=" ")
	print()

