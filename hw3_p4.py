x, y, k = map(int, input("Enter index x, y, k (separated by whitespace):").split()) #輸入
print("Enter the matrix by multiple lines:")
matrix = []
matrix_input = input("")
while matrix_input.lower() != "q": #輸入q就break
	if not matrix_input:
		break
	matrix.append([int(x) for x in matrix_input.split(" ")])
	matrix_input = input("")

value = matrix[x][y]
matrix[x][y] = k
queue = [(x, y)]

while queue:
	x,y = queue.pop(0)
	matrix[x][y] = k
	if x > 0 and matrix[x-1][y] == value:
		queue.append((x-1,y))
	if x < len(matrix) - 1 and matrix[x+1][y] == value:
		queue.append((x+1, y))
	if y > 0 and matrix[x][y-1] == value:
		queue.append((x, y-1))
	if y < len(matrix[0]) - 1 and matrix[x][y+1] == value:
		queue.append((x, y+1))
for row in matrix:
	print(" ".join(str(x) for x in row)) #輸出