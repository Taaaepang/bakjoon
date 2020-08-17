N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
visited = [False] * N
out = []
out_all = []
def solve(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))

    else:
        for i in range(len(visited)):
            if visited[i] is False:
                visited[i] = True
                out.append(num[i])
                solve(depth+1, N, M)
                visited[i] = False
                out.pop()

solve(0, N, M)
