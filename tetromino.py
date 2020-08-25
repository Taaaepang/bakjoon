import math
from copy import deepcopy

row, column = map(int, input().split())

maps = []

for i in range(row):
    maps.append(list(map(int, input().split())))
maxsum = -math.inf

tetrominos = [
    [   # ㅡ 모양
        [[0, 0], [0, 1], [0, 2], [0, 3]],
        [[0, 0], [1, 0], [2, 0], [3, 0]]
    ],
    [   # ㅁ 모양
        [[0, 0], [0, 1], [1, 0], [1, 1]],
    ],
    [   # ㄴ 모양
        [[0, 0], [1, 0], [2, 0], [2, 1]],
        [[0, 0], [0, 1], [0, 2], [1, 0]],
        [[0, 0], [0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 0], [1, 1], [1, 2]],
        [[2, 0], [0, 1], [1, 1], [2, 1]],
        [[0, 0], [0, 1], [0, 2], [1, 2]],
        [[0, 0], [0, 1], [1, 0], [2, 0]],
        [[0, 0], [1, 0], [1, 1], [1, 2]]
    ],
    [   # 번
        [[0, 0], [1, 0], [1, 1], [2, 1]],
        [[0, 1], [0, 2], [1, 0], [1, 1]],
        [[0, 1], [1, 1], [1, 0], [2, 0]],
        [[0, 0], [0, 1], [1, 1], [1, 2]]
    ],
    [   #
        [[0, 0], [0, 1], [0, 2], [1, 1]],
        [[1, 0], [0, 1], [1, 1], [2, 1]],
        [[0, 1], [1, 0], [1, 1], [1, 2]],
        [[0, 0], [1, 0], [2, 0], [1, 1]],
    ]
]



def searchMax(tetromino):
    global maxsum
    for i in range(row):
        check2 = False
        tet_temp = deepcopy(tetromino)
        for i in range(column):
            check = False
            temp = 0
            for j in range(4):
                temp += maps[tet_temp[j][0]][tet_temp[j][1]]
                tet_temp[j][1] += 1
                if tet_temp[j][1] >= column:
                    check = True
            if maxsum < temp:
                maxsum = temp
            if check == True:
                break
        for i in range(4):
            tetromino[i][0] += 1
            if tetromino[i][0] >= row:
                check2 = True
        if check2 == True:
            return 0

def solve():
    for i in range(2):
        searchMax(tetrominos[0][i])
    searchMax(tetrominos[1][0])
    for i in range(8):
        searchMax(tetrominos[2][i])
    for i in range(4):
        searchMax(tetrominos[3][i])
        searchMax(tetrominos[4][i])

solve()
print(maxsum)
