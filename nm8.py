N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
out = []
def solve(depth, idx, N, M):
    if depth == M:
        print(' '.join(map(str,out)))
    else:
        for i in range(idx, N):
            out.append(num[i])
            solve(depth+1, i, N, M)
            out.pop()

solve(0, 0, N, M)