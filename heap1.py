import heapq

def solution(scoville, K):
    answer = 0
    heap = heapq.heapify(scoville)
    while True:
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        answer += 1
        tmp = heapq.heappop(scoville)
        tmp1 = heapq.heappop(scoville)
        heapq.heappush(scoville, tmp + tmp1 * 2)

        if scoville[0] >= K:
            return answer



def main():
    print(solution([1, 2, 3, 9, 10, 12], 7))


if __name__ == "__main__":
    main()