import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    mini = 0
    if stock >= k - 1:
        return 0

    while stock < k:
        heap = []
        for i in range(mini, len(dates)):
            if dates[i] <= stock:
                heapq.heappush(heap, -supplies[i])
                mini = i+1
            else:
                break
        stock += heapq.heappop(heap) * -1
        answer += 1
    return answer

def main():
    print(solution(4, [4, 10, 15], [20, 5, 10], 30))
    print(solution(10, [4, 6, 10, 15], [8, 2, 2, 30], 30))

if __name__ == "__main__":
    main()