from collections import deque
from copy import deepcopy
Gears = []
# 12시 방향부터 순서대로
for _ in range(4):
    Gears.append(deque(input()))

cycle = int(input())
rules = deque()
for _ in range(cycle):
    rules.append(list(map(int, input().split())))

def moving(gear, dirs, init, prev, gearpos):
    prev_dir = prev
    init_dir = init
    if dirs == 'left':
        for i in range(gearpos, -1, -1):
            temp = gear.pop()
            counter = temp[2]
            dir_temp = temp[6]
            if counter != init_dir:
                if prev_dir == -1: # 전에 반시계 나는 시계
                    prev_dir = 1
                    cycle_temp = Gears[i].pop()
                    Gears[i].appendleft(cycle_temp)
                else:
                    prev_dir = -1
                    cycle_temp = Gears[i].popleft()
                    Gears[i].append(cycle_temp)
                init_dir = dir_temp
            else:
                return
    elif dirs =='right':
        for i in range(gearpos, 4):
            temp = gear.popleft()
            counter = temp[6]
            dir_temp = temp[2]
            if counter != init_dir:
                if prev_dir == -1:  # 전에 반시계 나는 시계
                    prev_dir = 1
                    cycle_temp = Gears[i].pop()
                    Gears[i].appendleft(cycle_temp)
                else:
                    prev_dir = -1
                    cycle_temp = Gears[i].popleft()
                    Gears[i].append(cycle_temp)
                init_dir = dir_temp
            else:
                return

def cycling(g, d):
    Gearleft = deque(Gears[:g])
    GearRight = deque(Gears[g+1:])
    left = Gears[g][6]
    right = Gears[g][2]
    if d == 1:  # 시
        temp = Gears[g].pop()
        Gears[g].appendleft(temp)
    elif d == -1:    # 반시
        temp = Gears[g].popleft()
        Gears[g].append(temp)
    moving(Gearleft, 'left', left, d, g-1)
    moving(GearRight, 'right', right, d, g+1)

def solve():
    while len(rules) > 0:
        Gear, dirs = rules.popleft()
        cycling(Gear-1, dirs)



solve()

score = 0
if Gears[0][0] == '1':
    score += 1
if Gears[1][0] == '1':
    score += 2
if Gears[2][0] == '1':
    score += 4
if Gears[3][0] == '1':
    score += 8

print(score)
