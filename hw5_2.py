import random

def create_board():
	game_board = []
	for i in range(30):
		if random.random() < 0.3:
			game_board.append("P")
		else:
			game_board.append("_")
	return game_board

def print_board():
	global A_location, B_location
	board = []
	for i in range(30):
		board.append("_")
	if A_location <= 29 and B_location <= 29:
		if A_location == B_location:
			if safe("A"):
				board[A_location] = "X"
			else:
				board[A_location] = "x"
		else:
			if safe("A"):
				board[A_location] = "A"
			else:
				board[A_location] = "a"
			if safe("B"):
				board[B_location] = "B"
			else:
				board[B_location] = "b"
	else:
		if A_location > 29:
			A_location = 29
		if B_location > 29:
			B_location = 29
		print_board()
		return

	for i in range(30):
		print(board[i], end="")

def step():
	#if 
	step = random.randint(1, 6)
	return step

def safe(player):
	if player == "A":
		if game_board[A_location] == "P":
			return False
		else:
			return True
	if player == "B":
		if game_board[B_location] == "P":
			return False
		else:
			return True
	
game_board = create_board()
A_location = 0
B_location = 0
safeA_count = 0
safeB_count = 0

stepA = step()
A_location += stepA
stepB = step()
B_location += stepB
print_board()
print("(A: %d, B: %d)" % (stepA, stepB))
while A_location < 29 or B_location < 29:
	if safeA_count == 1:
		stepA = step()
		A_location += stepA
		safeA_count -= 1
	elif safe("A"):
		stepA = step()
		A_location += stepA
	else:
		safeA_count += 1
		stepA = 0
		A_location += 0
	if safeB_count == 1:
		stepB = step()
		B_location += stepB
		safeB_count -= 1
	elif safe("B"):
		stepB = step()
		B_location += stepB
	else:
		safeB_count += 1
		stepB = 0
		B_location += 0

	print_board()
	print("(A: %d, B: %d)" % (stepA, stepB))

	if A_location >= 29 and B_location < 29:
	    print("Player A wins!")
	    break
	elif B_location >= 29 and A_location < 29:
	    print("Player B wins!")
	    break
	elif A_location >= 29 and B_location >= 29:
	    print("Both players win!")
	    break
for elem in game_board:
	print(elem, end="")