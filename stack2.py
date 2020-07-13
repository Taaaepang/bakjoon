def solution(heights):
    answer = []
    stack = heights.copy()
    size = len(stack) - 1
    for j in range(size):
        temp = stack.pop(size)
        size -= 1
        i = size
        check = len(answer)
        while i > 0:
            if stack[i] > temp:
                answer.append(i + 1)
                break
            i -= 1
        if check == len(answer):
            answer.append(0)
    answer.append(0)
    answer.reverse()
    return answer

heights = [6, 9, 5, 7, 4]
print(solution(heights))