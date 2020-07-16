def solution(array, commands):
    answer = []
    temp = array.copy()
    for command in commands:
        temp2 = temp[command[0] - 1:command[1]]
        temp2 = sorted(temp2)
        answer.append(temp2[command[2]-1])

    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))