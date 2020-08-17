N, M = map(int, input().split())
num = list(map(int,input().split()))
num.sort()
visited = [False] * N
out = []
out_all = []

def solve(depth, idx, N, M):
    if depth == M:
        temp = ' '.join(map(str, out))
        if temp not in out_all:
            out_all.append(temp)
    else:
        for i in range(idx ,len(visited)):
            if visited[i] is False:
                visited[i] = True
                out.append(num[i])
                solve(depth + 1, i + 1, N, M)
                visited[i] = False
                out.pop()
solve(0, 0, N, M)
for i in out_all:
    print(i)
