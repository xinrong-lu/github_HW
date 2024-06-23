import random

def generate_board(width, height, num_candy_types):  # 生成儲存糖果的紀錄板
    board = []
    for _ in range(height):
        row = [random.randint(1, num_candy_types) for _ in range(width)]
        board.append(row)
    return board

def print_board(board):  # 打印紀錄板
    for row in board:
        print(row)
    print()

def calculate_score(crushes):  # 計算分數 
    return len(crushes) * 10

def candyCrush(board):  # 主程式碼
    rows, cols = len(board), len(board[0])
    is_stable = False
    score = 0

    def crush(board, crushes):  # 消除函數
        for i, j in crushes:
            board[i][j] = 0

    def drop(board):  # 掉落函數
        for j in range(cols):
            idx = rows - 1
            for i in range(rows - 1, -1, -1):
                if board[i][j] != 0:
                    board[idx][j] = board[i][j]    # 糖果交換位置
                    idx -= 1
            for i in range(idx, -1, -1):
                board[i][j] = random.randint(1, num_candy_types)  # 生成新

    crushed_candies = []
    print_board(board)
    while not is_stable:  # 判斷還有沒有糖果可消除
        is_stable = True
        crushes = []

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 0:
                    continue

                if j < cols - 2 and board[i][j] == board[i][j+1] == board[i][j+2]:
                    crushes.extend([(i, j), (i, j+1), (i, j+2)])

                if i < rows - 2 and board[i][j] == board[i+1][j] == board[i+2][j]:
                    crushes.extend([(i, j), (i+1, j), (i+2, j)])

        if crushes:  # 需要消除
            is_stable = False
            crush(board, crushes)
            crushed_candies.extend(crushes)  
            score += calculate_score(crushes)
            drop(board)
            print_board(board)

    return crushed_candies, score

 # 使用者輸入紀錄板長寬以及糖果種類數量
width = int(input("Enter the width of the board: "))
height = int(input("Enter the height of the board: "))
num_candy_types = int(input("Enter the number of candy types: "))

 # 生成初始紀錄板
candy_board = generate_board(width, height, num_candy_types)

 # 打印紀錄板
print("Initial Board:")
print_board(candy_board)

 # 遊戲進行
score = 0
while True:  # 使用者輸入要交換的糖果位置
    row1 = int(input("Enter the row number of the first candy to switch(0 ~ %d)(-1 to exit): " % (height-1)))  # -1結束遊戲
    if row1 == -1:
        break
    col1 = int(input("Enter the column number of the first candy to switch(0 ~ %d): " % (width-1)))
    row2 = int(input("Enter the row number of the second candy to switch(0 ~ %d): " % (height-1)))
    col2 = int(input("Enter the column number of the second candy to switch(0 ~ %d): " % (width-1)))

     # 交換糖果位置
    candy_board[row1][col1], candy_board[row2][col2] = candy_board[row2][col2], candy_board[row1][col1]

     # 處理移動並打印出來
    print("After Switch:")
    crushed_candies, move_score = candyCrush(candy_board)
    score += move_score  # 計算分數
    num_crushed = len(crushed_candies)
    print("Number of candies crushed:", num_crushed)
    print("Score obtained:", move_score)

print("Exiting the game.")
print("Final Score:", score)
