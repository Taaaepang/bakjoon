from copy import deepcopy
def solution(n, times):
    answer = 0
    times.sort()
    high = n*times[len(times)-1]
    mid = high // 2
    while True:
        process = 0
        for i in range(len(times)):
            process += mid // times[i]
        if process > n :
            mid -= 1
        elif process < n:
            mid += 1
        else:
            answer = mid
            break
    return answer