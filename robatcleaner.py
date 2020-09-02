row, column = map(int, input().split())
x, y, d = map(int, input().split())
maps = []
for _ in range(row):
    maps.append(list(map(int, input().split())))
cleanSuccess = 0
depth = 1
def move(x, y, d, count):
    global depth
    depth += 1
    global cleanSuccess
    if count == 4:
        if maps[x][y] == 1:
            print(cleanSuccess)
            exit(0)
        else:
            move(x, y, d, 0)
    elif maps[x][y] == 0:
        cleanSuccess += 1
        maps[x][y] = depth
    else:
        pass
    for i in range(3, -2, -1):
        if (d+i) % 4 == 0:
            if count == 4:
                move(x, y-1, d, 4)
            else:
                if maps[x-1][y] == 0:
                    move(x-1, y, (d+i)%4, 0)
                else:
                    count += 1
        elif (d+i) % 4 == 1:
            if count == 4:
                move(x-1, y, d, 4)
            else:
                if maps[x][y+1] == 0:
                    move(x, y+1, (d+i)%4, 0)
                else:
                    count += 1
        elif (d+i)%4 == 2:
            if count == 4:
                move(x, y+1, d, 4)
            else:
                if maps[x+1][y] == 0:
                    move(x+1, y, (d+i)%4, 0)
                else:
                    count += 1
        elif (d+i)%4 == 3:
            if count == 4:
                move(x+1, y, d, 4)
            else:
                if maps[x][y-1] == 0:
                    move(x, y-1, (d+i)%4, 0)
                else:
                    count += 1

def solve():
    move(x, y, d, 0)
solve()

