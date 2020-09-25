from collections import deque
answer = 0
N, L, R = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

while True:
    moving = []
    dfs = []
    visited = [[False for _ in range(N)] for _ in range(N)]
    check = False
    for i in range(N):
        for j in range(N):
            for dx, dy in (0, -1), (0, 1), (-1, 0), (1, 0):
                x, y = i - dx, j - dy
                if 0 <= x <= N-1 and 0 <= y <= N-1:
                    if L <= abs(maps[i][j] - maps[x][y]) <= R:
                        if visited[x][y] == False:
                            check = True
                            visited[x][y] = True
                            population = maps[x][y]
                            peoples = 1
                            town = []
                            queue = deque()
                            queue.append((x, y))
                            while len(queue) != 0:
                                temp = queue.popleft()
                                town.append(temp)
                                for dx, dy in (0, -1), (0, 1), (-1, 0), (1, 0):
                                    x, y = temp[0] + dx, temp[1] + dy
                                    if 0 <= x <= N-1 and 0 <= y <= N-1:
                                        if L <= abs(maps[temp[0]][temp[1]]-maps[x][y]) <= R:
                                            if visited[x][y] == False:
                                                visited[x][y] = True
                                                queue.append((x, y))
                                                population += maps[x][y]
                                                peoples += 1
                            move_people = population // peoples
                            moving.append((town, move_people))
    for move in moving:
        for x, y in move[0]:
            maps[x][y] = move[1]

    if check:
        answer += 1
    else:
        break

print(answer)