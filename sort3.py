def solution(c):
    answer = 0
    c.sort(reverse=True)
    for idx, value in enumerate(c):
        if idx > value:
            return idx
    return len(c)