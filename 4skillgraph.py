from collections import deque
def solution(maps):
    answer = -1
    dfs = deque([(0, 0, 1)])
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visited[0][0] = True
    while len(dfs) > 0:
        current = dfs.popleft()
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            x, y = current[0] + dx, current[1] + dy
            if 0 <= x < len(maps) and 0 <= y < len(maps[0]) and maps[x][y] != 0:
                if x == len(maps)-1 and y == len(maps[0]) - 1:
                    answer = current[2] + 1
                    break
                if visited[x][y] == False:
                    visited[x][y] = True
                    dfs.append((x, y, current[2] + 1))
        if answer != -1:
            break
    return answer