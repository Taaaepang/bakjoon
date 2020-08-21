# 15686
import math
from itertools import combinations
from collections import deque
N, M = map(int, input().split())

maps = []
chicken_houses = []
houses = []

for i in range(N):
    maps.append(list(map(int, input().split())))
    for j in range(N):
        if maps[i][j] == 2:
            chicken_houses.append((i, j))
        if maps[i][j] == 1:
            houses.append((i, j))


mins = math.inf

def eat_chicken(depth, chicken):
    if depth == M + 1:
        return
    global mins
    distance = 0
    if depth == 1:
        for i in chicken:
            distance = 0
            for j in houses:
                distance += abs(i[0] - j[0]) + abs(i[1] - j[1])
            if mins > distance:
                mins = distance
    else:
        temp = deque(list(combinations(chicken, depth)))
        while len(temp) > 0:
            chick = temp.popleft()
            distance = 0
            for house in houses:
                distance_temp = []
                for c in chick:
                    distance_temp.append(abs(c[0] - house[0]) + abs(c[1] - house[1]))
                distance += min(distance_temp)
            if mins > distance:
                mins = distance
    return eat_chicken(depth + 1, chicken_houses)

def solve():
   eat_chicken(1, chicken_houses)


solve()
print(mins)






