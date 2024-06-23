import random
import time

def play_minesweeper():
    def map(): #印出整個圖的函數
        print("    a   b   c   d   e   f   g   h   i")
        print("  " + "+---" * 9 + "+")
        for i in range(9):
            print(i + 1, end =" |")
            for j in range(9):
                print(" " + location[(i, j)] + " |", end ="")
            print()
            print("  " + "+---" * 9 + "+")
        print() 

    def reveal(row, col): #打開格子的函數
        nonlocal location, bomb_location, again, mine, first, flag_location
        if location[(row, col)] == "F": #撤掉旗子
            if flag:
                location[(row, col)] = " "
                flag_location.remove((row, col))
                mine += 1
                return
            else: #是旗子就不打開
                return
        elif location[(row, col)] != " ": #已打開
            return
        elif flag: #插旗
            location[(row, col)] ="F"
            flag_location.append((row, col))
            mine -= 1
            return
        elif (row, col) in bomb_location: #踩到炸彈
            for (bomb_row, bomb_col) in bomb_location:
                location[(bomb_row, bomb_col)] = "X"
            print("Game Over")
            print()
            map()
            again = input("Play again? (y/n):") #重來 重新初始化
            if again == "y":
                location = {(i, j): " " for i in range(9) for j in range(9)}
                bomb_location = []
                mine = 10
                map()
                print("Enter the column followed by the row(ex: a5). To add or remove a flag, add 'f' to the cell (ex: a5f). Type 'help' th show this message again.")
                print()
                first = True
                again = True
                return
            elif again == "n": #不重來 遊戲結束
                again = False
            return
        else:
            count = 0 #算該格九宮格內有幾個炸彈
            for i in range(max(row-1, 0), min(row+2, 9)):
                for j in range(max(col-1, 0), min(col+2, 9)):
                    if (i, j) in bomb_location:
                        count += 1
            location[(row, col)] = str(count) 
            if count == 0: #為0則繼續找下一格
                for i in range(max(row-1, 0), min(row+2, 9)):
                    for j in range(max(col-1, 0), min(col+2, 9)):
                        if (i, j) != (row, col):
                            reveal(i, j)
            return
    
    location = {(i, j): " " for i in range(9) for j in range(9)} #初始化
    bomb_location = []
    flag_location = []
    mine = 10
    map()
    print("Enter the column followed by the row(ex: a5). To add or remove a flag, add 'f' to the cell (ex: a5f). Type 'help' th show this message again.")
    print()
    first = True
    again = True
    while again:
        flag = False
        command = input("Enter the cell(%d mines left):" % mine)
        if command == "help": #help指令
            map()
            print("Enter the column followed by the row(ex: a5). To add or remove a flag, add 'f' to the cell (ex: a5f).")
            print()
            continue
        col, row = command[0], command[1]
        col = ord(col) -97
        row = int(row) - 1    
        if (col or row) not in [0, 1, 2, 3, 4, 5, 6, 7, 8]: #錯誤位置
            map()
            print("Invalid cell.", end=" ")
            print("Enter the column followed by the row(ex: a5). To add or remove a flag, add 'f' to the cell (ex: a5f).")
            print()
            continue
        elif len(command) == 3: #是否插旗
            flag = True
        if flag:
            if location[(row, col)] != "F" and location[(row, col)] != " ": #錯誤插旗位置
                map()
                print("Cannot put a flag there")
                print()
                continue
        else:
            if location[(row, col)] == "F": #已有旗子位置
                map()
                print("There is a flag there")
                print()
                continue
            elif location[(row, col)] != " ": #格子已揭開位置
                map()
                print("That cell is already shown")
                print()
                continue
        if first: #第一次要設定炸彈位置
            safe = [] #第一格九宮格內不能有炸彈
            for i in range(max(row-1, 0), min(row+2, 9)):
                for j in range(max(col-1, 0), min(col+2, 9)):
                    safe.append((i, j))
            for _ in range(10):
                bomb_col, bomb_row = random.randint(0, 8), random.randint(0, 8)
                while (bomb_row, bomb_col) in safe:
                    bomb_col, bomb_row = random.randint(0, 8), random.randint(0, 8)
                while (bomb_row, bomb_col) in bomb_location: #重複格子
                    bomb_col, bomb_row = random.randint(0, 8), random.randint(0, 8)
                bomb_location.append((bomb_row, bomb_col))
            reveal(row, col)
            map()
            first = False
        else:
            reveal(row, col)
            map()
        if mine == 0: #確認有沒有插錯旗
            win = True
            for (flag_row, flag_col) in flag_location:
                if (flag_row, flag_col) not in bomb_location:
                    win = False
                    continue
            if win: #贏則將所有炸彈位置變成X 並打開未打開的格子
                for (bomb_row, bomb_col) in bomb_location:
                    location[(bomb_row, bomb_col)] = "X"
                map()
                print("Congratulations! You won!")
                print()
                again = input("Play again? (y/n):") #重來 重新初始化
                if again == "y":
                    location = {(i, j): " " for i in range(9) for j in range(9)}
                    bomb_location = []
                    mine = 10
                    map()
                    print("Enter the column followed by the row(ex: a5). To add or remove a flag, add 'f' to the cell (ex: a5f). Type 'help' th show this message again.")
                    print()
                    first = True
                    again = True
                    continue
                elif again == "n": #不重來 遊戲結束
                    again = False
                    continue
            else:
                print("Not all flags are correctly placed. Keep trying!") #插錯旗
                print()

play_minesweeper()