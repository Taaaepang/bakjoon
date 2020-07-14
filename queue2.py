class Queue:
    queue = list()
    size = 0
    def __init__(self, q):
        self.queue = q
        self.size = len(q)
    def push(self, num):
        self.queue.append(num)
    def pop(self):
        if self.size == 0:
            return -1
        else:
            temp = self.queue.pop(0)
            self.size -= 1
            return temp

def solution(priorities, location):
    answer = 0
    queue = priorities.copy()
    s_queue = sorted(queue, reverse=True)
    locate = location
    cnt = 0
    while len(queue) != 0:
        temp = queue.pop(0)
        if temp == s_queue[0]:
            if locate == 0:
                cnt += 1
                break
            s_queue.pop(0)
            cnt += 1
            locate -= 1
        elif temp < s_queue[0]:
            if locate == 0:
                queue.append(temp)
                locate = len(queue) - 1
            else:
                queue.append(temp)
                locate -= 1
    return cnt






def main():
    print(solution([2, 1, 3, 2], 2))
    print(solution([1, 1, 9, 1, 1, 1], 0))

if __name__ == "__main__":
    main()

'''
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
'''