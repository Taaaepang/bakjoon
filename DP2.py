def solution(triangle):
    temp = [[] for _ in range(len(triangle))]
    for i in range(len(triangle)-1, -1, -1):
        if i == 0:
            temp[i] = triangle[i][0] + max(temp[i + 1])
            break
        elif i == len(triangle)-1:
            temp[i] = triangle[i]
        else:
            for j in range(len(triangle[i])):
                temp[i].append(max(temp[i+1][j], temp[i+1][j+1]))
                temp[i][j] += triangle[i][j]

    return temp[0]



if __name__ == '__main__':
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))