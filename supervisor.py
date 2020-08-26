di==
classroom = int(input())
if classroom == 1:
    tester = [int(input())]
else:
    tester = list(map(int, input().split()))
availabe_visor = list(map(int, input().split())) # senior, junior
answer = 0

for i in range(len(tester)):
    tester[i] -= availabe_visor[0]
    answer += 1
    if tester[i] > 0:
        answer += tester[i] // availabe_visor[1]
        if tester[i] % availabe_visor[1]:
            answer += 1
print(answer)














