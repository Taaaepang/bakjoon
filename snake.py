from collections import deque

size = int(input())
apple = int(input())
maps = [[0 for i in range(size)] for j in range(size)]
# 9 사과.
if apple != 0:
    for i in range(apple):
        x, y = map(int, input().split())
        maps[x-1][y-1] = 9

move = int(input())
move_info = deque(list())
for i in range(move):
    move_info.append(list(map(str, input().split())))
    move_info[i][0] = int(move_info[i][0])

maps[0][0] = 1  # snake's start

# up = 0
# right = 1
# down = 2
# left = 3

direction = 1
head = [0, 0]
tail = [0, 0]
shadow = deque(list())

def moving(time, direction, head, tail):
    while True:
        if len(move_info) > 0 and time == list(move_info)[0][0]:
            init_direction = move_info.popleft()[1]
            if init_direction == 'L':
                if direction == 0:
                    direction = 3
                else:
                    direction -= 1
            if init_direction == 'D':
                if direction == 3:
                    direction = 0
                else:
                    direction += 1
        time += 1
        if direction == 0:
            if head[0] == 0 or maps[head[0]-1][head[1]] == 1:
                return time
            head[0] -= 1
            shadow.append([head[0], head[1]])
        elif direction == 1:
            if head[1] == size-1 or maps[head[0]][head[1]+1] == 1:
                return time
            head[1] += 1
            shadow.append([head[0], head[1]])
        elif direction == 2:
            if head[0] == size-1 or maps[head[0]+1][head[1]] == 1:
                return time
            head[0] += 1
            shadow.append([head[0], head[1]])
        else:
            if head[1] == 0 or maps[head[0]][head[1]-1] == 1:
                return time
            head[1] -= 1
            shadow.append([head[0], head[1]])

        if maps[head[0]][head[1]] == 9:
            pass
        else:
            maps[tail[0]][tail[1]] = 0
            tail = shadow.popleft()
        maps[head[0]][head[1]] = 1


def solve():
    time = moving(0, direction, head, tail)
    print(time)
solve()
