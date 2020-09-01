import math
from collections import deque
from copy import deepcopy
size = int(input())
maps = []
for i in range(size):
    maps.append(deque(list(map(int, input().split()))))

# 0 up
# 1 right
# 2 down
# 3 left
maxs = -math.inf
def moving(dir, mapd):
    map_temp = deepcopy(mapd)
    if dir == 3: # left
        for i in range(size):
            answer = deque()
            temp = map_temp[i].popleft()
            while True:
                if len(map_temp[i]) == 0:
                    answer.append(temp)
                    break
                elif temp == 0 and map_temp[i][0] == 0:
                    map_temp[i].popleft()
                    if len(map_temp[i]) == 0:
                        break
                    temp = map_temp[i].popleft()
                elif temp == map_temp[i][0]:
                    map_temp[i].popleft()
                    answer.append(temp * 2)
                    if len(map_temp[i]) == 0:
                        break
                    temp = map_temp[i].popleft()
                elif temp != map_temp[i][0]:
                    if temp == 0:
                        temp = map_temp[i].popleft()
                    elif map_temp[i][0] == 0:
                        map_temp[i].popleft()
                    else:
                        answer.append(temp)
                        if len(map_temp[i]) == 0:
                            break
                        temp = map_temp[i].popleft()
            for j in range(size - len(answer)):
                answer.append(0)
            map_temp[i] = deepcopy(answer)
    elif dir == 1: # right
        for i in range(size):
            answer = deque()
            temp = map_temp[i].pop()
            while True:
                size1 = len(map_temp[i]) - 1
                if len(map_temp[i]) == 0:
                    answer.appendleft(temp)
                    break
                elif temp == 0 and map_temp[i][size1] == 0:
                    map_temp[i].pop()
                    if len(map_temp[i]) == 0:
                        break
                    temp = map_temp[i].pop()
                elif temp == map_temp[i][size1]:
                    map_temp[i].pop()
                    answer.appendleft(temp * 2)
                    if len(map_temp[i]) == 0:
                        break
                    temp = map_temp[i].pop()
                elif temp != map_temp[i][size1]:
                    if temp == 0:
                        temp = map_temp[i].pop()
                    elif map_temp[i][size1] == 0:
                        map_temp[i].pop()
                    else:
                        answer.appendleft(temp)
                        if len(map_temp[i]) == 0:
                            break
                        temp = map_temp[i].pop()
            for j in range(size - len(answer)):
                answer.appendleft(0)
            map_temp[i] = deepcopy(answer)
    elif dir == 0 or dir == 2:
        for i in range(size):
            m_temp = deque()
            for j in range(size):
                m_temp.append(map_temp[j][i])
            if dir == 0:
                answer = []
                temp = m_temp.popleft()
                while True:
                    if len(m_temp) == 0:
                        answer.append(temp)
                        break
                    elif temp == 0 and m_temp[0] == 0:
                        m_temp.popleft()
                        if len(m_temp) == 0:
                            break
                        temp = m_temp.popleft()
                    elif temp == m_temp[0]:
                        m_temp.popleft()
                        answer.append(temp * 2)
                        if len(m_temp) == 0:
                            break
                        temp = m_temp.popleft()
                    elif temp != m_temp[0]:
                        if temp == 0:
                            temp = m_temp.popleft()
                        elif m_temp[0] == 0:
                            m_temp.popleft()
                        else:
                            answer.append(temp)
                            if len(m_temp) == 0:
                                break
                            temp = m_temp.popleft()
                for _ in range(size - len(answer)):
                    answer.append(0)
            elif dir == 2:
                answer = deque()
                temp = m_temp.pop()
                while True:
                    size_t = len(m_temp) - 1
                    if len(m_temp) == 0:
                        answer.appendleft(temp)
                        break
                    elif temp == 0 and m_temp[size_t] == 0:
                        m_temp.pop()
                        if len(m_temp) == 0:
                            break
                        temp = m_temp.pop()
                    elif temp == m_temp[size_t]:
                        m_temp.pop()
                        answer.appendleft(temp*2)
                        if len(m_temp) == 0:
                            break
                        temp = m_temp.pop()
                    elif temp != m_temp[size_t]:
                        if temp == 0:
                            temp = m_temp.pop()
                        elif m_temp[size_t] == 0:
                            m_temp.pop()
                        else:
                            answer.appendleft(temp)
                            if len(m_temp) == 0:
                                break
                            temp = m_temp.pop()
                for _ in range(size - len(answer)):
                    answer.appendleft(0)
            for j in range(size):
                map_temp[j][i] = answer[j]
    return map_temp

def move(depth, map_t):
    global maxs
    if depth == 5:
        for i in map_t:
            temp = max(i)
            if maxs < temp:
                maxs = temp
        return
    for i in range(4):
        map_tt = moving(i, map_t)
        move(depth + 1, map_tt)


def solve():
    move(0, maps)

solve()
print(maxs)