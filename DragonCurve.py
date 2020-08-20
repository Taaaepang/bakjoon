from copy import deepcopy
from collections import deque

N = int(input())
info = []
for i in range(N):
    info.append(list(map(int, input().split())))

map = [[0 for i in range(101)] for j in range(101)]
visited = [False]*N
#def check():

# 방향
# 0 위
# 1 오른
# 2 밑
# 3 왼

def getpos(d, g):
    pos = []
    def get(depth, d, g, pos):
        if depth == g+1:
            return pos
        if depth == 0:
            if d == 0:
                pos.append(1)
            elif d == 1:
                pos.append(0)
            elif d == 2:
                pos.append(3)
            else:
                pos.append(2)
        else:
            length = len(pos) / 2
            if depth == 1:
                if pos[0] == 0:
                    pos.append(3)
                else:
                    pos.append(pos[0]-1)
            else:
                for i in range(0, len(pos)):
                    if i < length:
                        temp = pos[i]
                        if temp > 1:
                            temp -= 2
                        else:
                            temp += 2
                        pos.append(temp)
                    else:
                        pos.append(pos[i])
        return get(depth+1, d, g, pos)
    return get(0, d, g, pos)

def drawingDragonCurve(pos, x, y):
    draw = map
    pos = deque(pos)
    draw[x][y] = 1
    for i in range(len(pos)):
        temp = pos.popleft()
        if temp == 0:
            draw[x-1][y] = 1
            x, y = x-1, y
        elif temp == 1:
            draw[x][y+1] = 1
            x, y = x, y+1
        elif temp == 2:
            draw[x+1][y] = 1
            x, y = x+1, y
        elif temp == 3:
            draw[x][y-1] = 1
            x, y = x, y-1
    return draw

def getSquare(draw):
    square = 0
    for i in range(len(draw)-1):
        for j in range(len(draw[0])-1):
            if draw[i][j] == 1 and draw[i+1][j] == 1 and draw[i][j+1] == 1 and draw[i+1][j+1] == 1:
                square += 1
    return square


def solve():
    for i in range(len(info)):
        x, y, d, g = info[i]
        pos = getpos(d, g)
        draw = drawingDragonCurve(pos, y, x)
    squarezone = getSquare(draw)
    print(squarezone)

solve()