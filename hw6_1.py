candy_board = []
with open("candy_input2.txt", "r") as candy:  # 匯入檔案
    for line in candy:
        line = line.strip().split(",")
        line = list(map(int, line))
        candy_board.append(line)
        
def candyCrush(board):  # 主程式碼
    rows, cols = len(board), len(board[0])
    is_stable = False  # 添加標誌變量

    def crush(board, crushes):  # 定義消除函數
        for i, j in crushes:
            board[i][j] = 0

    def drop(board, drops):  # 定義掉落函數
        for j in range(cols):
            idx = rows - 1
            for i in range(rows - 1, -1, -1):
                if board[i][j] != 0:
                    board[idx][j] = board[i][j] #糖果交換位置
                    idx -= 1
            for i in range(idx, -1, -1): #上層糖果為0
                board[i][j] = 0

    while not is_stable:  #判斷還有沒有糖果可消除
        is_stable = True
        crushes = []
        drops = []

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 0:
                    continue

                if j < cols - 2 and board[i][j] == board[i][j+1] == board[i][j+2]:
                    crushes.extend([(i, j), (i, j+1), (i, j+2)])

                if i < rows - 2 and board[i][j] == board[i+1][j] == board[i+2][j]:
                    crushes.extend([(i, j), (i+1, j), (i+2, j)])

        if crushes: #需要消除
            is_stable = False
            crush(board, crushes)

        if not is_stable:
            for j in range(cols):
                idx = rows - 1
                for i in range(rows - 1, -1, -1):
                    if board[i][j] != 0:
                        board[idx][j] = board[i][j]
                        idx -= 1
                for i in range(idx, -1, -1):
                    board[i][j] = 0

    return board

 # 調用函數進行糖果消除和掉落
board = candyCrush(candy_board)

 # 打印結果
for row in board:
    print(row)
