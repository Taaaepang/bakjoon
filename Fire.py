
task = int(input())

tp = []
max_money = [0]*task
for _ in range(task):
    tp.append(list(map(int, input().split())))

for i in range(task-1, -1, -1):
    t = tp[i][0]
    p = tp[i][1]
    if t > task-i:
        if i != task-1:
            max_money[i] = max_money[i+1]
        continue

    if i == task-1:
        max_money[i] = p
    elif i + p == task:
        max_money[i] = max(p, max_money[i+1])
    else:
        max_money[i] = max(p + max_money[i+t], max_money[i+1])

if task == 0:
    print(0)
else:
    print(max_money[0])