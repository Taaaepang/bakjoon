N, M = map(int, input().split())
visited = [False] * N
out = []
out_all = []
def solve(depth, idx, n, m):
    if depth == m:
        temp = ' '.join(map(str, out))
        if temp not in out_all:
            out_all.append(temp)
    else:
        for i in range(idx, len(visited)):
            out.append(i+1)
            solve(depth + 1, i, n, m)
            out.pop()

solve(0, 0, N, M)
for i in out_all:
    print(i)