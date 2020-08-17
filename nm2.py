N, M = map(int, input().split())
visited = [False] * N

out = []
out_all = []

def solve(depth, n, m):
    if depth == m:
        temp = ' '.join(map(str, sorted(out)))
        if temp not in out_all:
            out_all.append(temp)

    else:
        for i in range(len(visited)):
            if visited[i] is False:
                visited[i] = True
                out.append(i+1)
                solve(depth+1, n, m)
                visited[i] = False
                out.pop()
solve(0, N, M)
for i in out_all:
    print(i)
