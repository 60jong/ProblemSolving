def countTargetCells(cheeboard,start):
    count = 0


    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                if cheeboard[i][j] != start:
                    count += 1
            else:
                if cheeboard[i][j] == start:
                    count += 1
    return count

n,m = map(int,input().split())
countList = []

board = []
for _ in range(n):
    board.append(list(map(str,input())))

for i in range(n-7):
    for j in range(m-7):
        chessBoard = [row[j:j+8] for row in board[i:i+8]]
        countList.append(countTargetCells(chessBoard,'B'))
        countList.append(countTargetCells(chessBoard, 'W'))

print(min(countList))
