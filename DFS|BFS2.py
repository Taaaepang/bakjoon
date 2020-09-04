import math
# 네트워크

net = math.inf
def dfs(idx, coms, visited):
    visited[idx] = True
    for i in range(len(coms)):
        if idx != i and coms[idx][i] == 1 and visited[i] == False:
            visited = dfs(i, coms, visited)
    return visited


def solution(n, computers):
    visited = [False] * n
    answer = 0
    for i in range(n):
        if visited[i] == False:
            dfs(i, computers, visited)
            answer += 1
    return answer
def main():
    print(solution(3, [[1,1,1], [1, 1, 0], [1, 0, 1]]))
    print(solution(3, [[1, 1, 0],[1, 1, 1], [0, 1, 1]]))
    print(solution(4, [[1,0,0,0], [0,1,0,0], [0, 0, 1, 0], [0, 0, 0, 1]]))

if __name__ == '__main__':
    main()