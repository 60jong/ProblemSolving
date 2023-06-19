# 5
# 3
# 0 0 0 0 0
# 10 0 4 0 0
# 0 0 7 0 0
# 0 0 0 0 0
# 0 0 2 0 0
# 1 5 1

# 5
# 5
# 0 0 7 0 0
# 0 0 5 20 20
# 0 6 7 0 0
# 0 1 0 0 0
# 0 0 2 0 0
# 2 3 1 1 1

# 7
# 10
# 0 0 7 0 0 0 '1'1
# 0 0 5 9 '20'
# 0 6 7 0 0 3 8
# 0 1 0 0 0 0 0
# 0 0 2 0 0 0 1
# 0 1 0 0 0 0 0
# 0 0 2 0 0 0 1

# 2 3 '1' 5 7 '1' 1
class Node:
    def __init__(self, initScore):
        self.initScore = initScore
        self.leftScore = initScore
        self.isBonus = True if initScore > 10 else False


class Bullet:
    def __init__(self, attackScore):
        self.attackScore = attackScore


n = int(input())
k = int(input())

board = list()
for _ in range(n):
    nodeScores = list(map(int, input().split()))
    row = list()
    for score in nodeScores:
        node = Node(score)
        row.append(Node(score))
    board.append(row)

bullets = list(map(int, input().split()))

def getBonuses(board):
    bonuses = 0
    for row in board:
        for node in row:
            bonuses = bonuses + 1 if node.isBonus else bonuses
    return bonuses

def findBulletsForBonus(bonuses, bullets):
    forBonusIndex = list()
    bullets
def findTarget(board, bullet):

def shootTarget(board, i, j,bullet):


myScore = 0
for bullet in bullets:
    i, j = findTarget(board, bullet)


print(myScore)