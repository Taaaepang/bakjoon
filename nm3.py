N, M = map(int, input().split())
visited = [False] * N
out = []

def solve(depth, n, m):
    if depth == m:
        print(' '.join(map(str, out)))
        return
    else:
        for i in range(len(visited)):
            if visited[i] is False:
                out.append(i+1)
                solve(depth+1, n, m)
                out.pop()
solve(0, N, M)