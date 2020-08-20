from collections import defaultdict
from copy import deepcopy
import math
row, column = map(int, input().split())
cameras = []
space = []
for i in range(row):
    temp = (list(map(int, input().split())))
    for j in range(column):
        if temp[j] <= 5 and temp[j] >= 1:
            cameras.append((i, j, temp[j]))  # camera 종류, 위치, 방향
    space.append(temp)
out = []
mins = math.inf
# 0 위
# 1 오른쪽
# 2 아래
# 3 왼
def supervise(space, pos, y, x):
    space = deepcopy(space)
    for p in pos:
        if p == 0:
            for i in range(y-1, -1, -1):
                if space[i][x] == 6:
                    break
                elif space[i][x] != 0:
                    continue
                else:
                    space[i][x] = '#'
        elif p == 1:
            for i in range(x+1, len(space[0])):
                if space[y][i] == 6:
                    break
                elif space[y][i] != 0:
                    continue
                else:
                    space[y][i] = '#'
        elif p == 2:
            for i in range(y+1, len(space)):
                if space[i][x] == 6:
                    break
                elif space[i][x] != 0:
                    continue
                else:
                    space[i][x] = '#'
        elif p == 3:
            for i in range(x-1, -1, -1):
                if space[y][i] == 6:
                    break
                elif space[y][i] != 0:
                    continue
                else:
                    space[y][i] = '#'
    return space

def solve(depth, space, cameras):
    global mins

    if depth == len(cameras):
        value = 0
        for i in range(len(space)):
            value += space[i].count(0)
        mins = min(mins, value)
        return

    camera = cameras[depth]
    y, x, kinds_camera = camera
    if kinds_camera == 1:
        for i in range(4):
            next_space = supervise(space, [i], y, x)
            solve(depth+1, next_space, cameras)
    if kinds_camera == 2:
        for i in [(0,2),(1, 3)]:
            next_space = supervise(space, i, y, x)
            solve(depth+1, next_space, cameras)
    if kinds_camera == 3:
        for i in [(0,1), (1,2), (2,3), (3,0)]:
            next_space = supervise(space,i, y, x)
            solve(depth+1, next_space, cameras)
    if kinds_camera == 4:
        for i in [(0,1,2), (1,2,3), (2,3,0), (3,0,1)]:
            next_space = supervise(space, i, y, x)
            solve(depth+1, next_space, cameras)
    if kinds_camera == 5:
        next_space = supervise(space, (0, 1, 2, 3), y, x)
        solve(depth+1, next_space, cameras)

solve(0, space,cameras)
print(mins)


